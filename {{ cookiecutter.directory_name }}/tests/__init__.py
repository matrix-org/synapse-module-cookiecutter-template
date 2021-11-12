from typing import Optional

import attr
from mock import Mock
from synapse.module_api import ModuleApi

from {{ cookiecutter.package_name }} import {{ cookiecutter.module_class_name }}


@attr.s(auto_attribs=True)
class MockEvent:
    """Mocks an event. Only exposes properties the module uses."""
    sender: str
    type: str
    content: dict
    room_id: str = "!someroom"
    state_key: Optional[str] = None

    def is_state(self):
        """Checks if the event is a state event by checking if it has a state key."""
        return self.state_key is not None

    @property
    def membership(self):
        """Extracts the membership from the event. Should only be called on an event
        that's a membership event, and will raise a KeyError otherwise.
        """
        return self.content["membership"]


def create_module() -> {{ cookiecutter.module_class_name }}:
    # Create a mock based on the ModuleApi spec, but override some mocked functions
    # because some capabilities are needed for running the tests.
    module_api = Mock(spec=ModuleApi)

    # If necessary, give parse_config some configuration to parse.
    config = {{ cookiecutter.module_class_name }}.parse_config({})

    return {{ cookiecutter.module_class_name }}(config, module_api)