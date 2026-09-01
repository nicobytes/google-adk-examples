# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from app.prompt import HARBOR_PROMPT
from app.tools import STORE_TZ, get_now


def test_get_now_uses_pacific_timezone() -> None:
    result = get_now()
    assert "PDT" in result or "PST" in result or "-07" in result or "-08" in result
    assert str(STORE_TZ) == "America/Los_Angeles"


def test_harbor_prompt_covers_core_rules() -> None:
    lowered = HARBOR_PROMPT.lower()
    assert "harbor" in lowered
    assert "load_skill" in lowered
    assert "inactive" in lowered
    assert "get_now" in lowered
    assert "escalate" in lowered
