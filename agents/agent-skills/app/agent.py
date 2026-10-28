# ruff: noqa
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

import pathlib

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.skills import load_skill_from_dir
from google.adk.tools import skill_toolset
from google.genai import types

from app.prompt import HARBOR_PROMPT
from app.tools import get_now

MODEL = "gemini-flash-latest"
_SKILLS_DIR = pathlib.Path(__file__).parent / "skills"

_skills = [
    load_skill_from_dir(skill_path)
    for skill_path in sorted(_SKILLS_DIR.iterdir())
    if skill_path.is_dir() and (skill_path / "SKILL.md").exists()
]
skill_tools = skill_toolset.SkillToolset(skills=_skills)

root_agent = Agent(
    name="harbor",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction=HARBOR_PROMPT,
    tools=[skill_tools, get_now],
)

app = App(
    root_agent=root_agent,
    name="app",
)
