{% if cookiecutter.variant == "synapse_team" -%}
# Copyright {% now 'utc', '%Y' %} The Matrix.org Foundation C.I.C.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

{% endif -%}
from asyncio import Future
from typing import Any, Awaitable, Dict, Optional, TypeVar
from unittest.mock import Mock

import attr
from synapse.module_api import ModuleApi

from {{ cookiecutter.package_name }} import {{ cookiecutter.module_class_name }}

TV = TypeVar("TV")


def make_awaitable(result: TV) -> Awaitable[TV]:
    """
    Makes an awaitable, suitable for mocking an `async` function.
    This uses Futures as they can be awaited multiple times so can be returned
    to multiple callers.
    This function has been copied directly from Synapse's tests code.
    """
    future = Future()  # type: ignore
    future.set_result(result)
    return future


@attr.s(auto_attribs=True)
class MockEvent:
    """Mocks an event. Only exposes properties the module uses."""

    sender: str
    type: str
    content: Dict[str, Any]
    room_id: str = "!someroom"
    state_key: Optional[str] = None

    def is_state(self) -> bool:
        """Checks if the event is a state event by checking if it has a state key."""
        return self.state_key is not None

    @property
    def membership(self) -> str:
        """Extracts the membership from the event. Should only be called on an event
        that's a membership event, and will raise a KeyError otherwise.
        """
        membership: str = self.content["membership"]
        return membership


def create_module() -> {{ cookiecutter.module_class_name }}:
    # Create a mock based on the ModuleApi spec, but override some mocked functions
    # because some capabilities are needed for running the tests.
    module_api = Mock(spec=ModuleApi)

    # If necessary, give parse_config some configuration to parse.
    config = {{ cookiecutter.module_class_name }}.parse_config({})

    return {{ cookiecutter.module_class_name }}(config, module_api)
