#   Copyright 2020-2020 Exactpro (Exactpro Systems Limited)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.


from typing import List

from google.protobuf.message import Message

from th2_common.schema.filter.strategy.filter_strategy import FilterStrategy
from th2_common.schema.message.configuration.field_filter_configuration import FieldFilterConfiguration
from th2_common.schema.message.configuration.router_filter import RouterFilter
from th2_common.schema.strategy.field_extraction.impl.th2_batch_msg_field_extraction import Th2BatchMsgFieldExtraction


class DefaultFilterStrategy(FilterStrategy):

    def __init__(self, extract_strategy=Th2BatchMsgFieldExtraction()) -> None:
        self.extract_strategy = extract_strategy

    def verify(self, message: Message, router_filter: RouterFilter = None, router_filters: List[RouterFilter] = None):
        if router_filters is None:
            msg_field_filters = dict(router_filter.get_message())
            msg_field_filters.update(router_filter.get_metadata())
            return self.check_values(self.extract_strategy.get_fields(message), msg_field_filters)
        else:
            if len(router_filters) == 0:
                return True
            for fields_filter in router_filters:
                if self.verify(message=message, router_filter=fields_filter):
                    return True
            return False

    def check_values(self, message_fields: {str: str}, field_filters: {str: FieldFilterConfiguration}) -> bool:
        for field_name in field_filters.keys():
            field_filter = field_filters[field_name]
            msg_field_value = message_fields[field_name]
            if not self.check_value(msg_field_value, field_filter):
                return False
        return True

    def check_value(self, value1, filter_configuration: FieldFilterConfiguration):
        if len(value1) == 0:
            return False

        value2 = filter_configuration.value
        if filter_configuration.operation == "EQUAL":
            return value1 == value2
        elif filter_configuration.operation == "NOT_EQUAL":
            return value1 != value2
        elif filter_configuration.operation == "EMPTY":
            return len(value1) == 0
        elif filter_configuration.operation == "NOT_EMPTY":
            return len(value1) != 0
        else:
            return False
