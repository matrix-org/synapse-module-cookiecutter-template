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
from typing import Any, Dict

import attr
from synapse.module_api import ModuleApi


@attr.s(auto_attribs=True, frozen=True)
class {{ cookiecutter.module_class_name }}Config:
    pass


class {{ cookiecutter.module_class_name }}:
    def __init__(self, config: {{ cookiecutter.module_class_name }}Config, api: ModuleApi):
        # Keep a reference to the config and Module API
        self._api = api
        self._config = config

    @staticmethod
    def parse_config(config: Dict[str, Any]) -> {{ cookiecutter.module_class_name }}Config:
        # Parse the module's configuration here.
        # If there is an issue with the configuration, raise a
        # synapse.module_api.errors.ConfigError.
        #
        # Example:
        #
        #     some_option = config.get("some_option")
        #     if some_option is None:
        #          raise ConfigError("Missing option 'some_option'")
        #      if not isinstance(some_option, str):
        #          raise ConfigError("Config option 'some_option' must be a string")
        #
        return {{ cookiecutter.module_class_name }}Config()
