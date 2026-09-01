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

from google.adk.skills import load_skill_from_dir

from app.agent import MODEL, _SKILLS_DIR, app, root_agent


def _load_skills_from_dir(skills_dir: pathlib.Path) -> list:
    if not skills_dir.is_dir():
        return []
    return [
        load_skill_from_dir(skill_path)
        for skill_path in sorted(skills_dir.iterdir())
        if skill_path.is_dir() and (skill_path / "SKILL.md").exists()
    ]


def test_root_agent_is_harbor() -> None:
    assert root_agent.name == "harbor"


def test_app_name_unchanged() -> None:
    assert app.name == "app"


def test_model_unchanged() -> None:
    assert root_agent.model.model == MODEL


def test_load_skills_empty_dir(tmp_path: pathlib.Path) -> None:
    assert _load_skills_from_dir(tmp_path) == []


def test_load_skills_ignores_dirs_without_skill_md(tmp_path: pathlib.Path) -> None:
    (tmp_path / "empty-dir").mkdir()
    (tmp_path / "file.txt").write_text("x", encoding="utf-8")
    assert _load_skills_from_dir(tmp_path) == []


def test_load_skills_loads_valid_skill(tmp_path: pathlib.Path) -> None:
    skill_dir = tmp_path / "demo-skill"
    skill_dir.mkdir()
    (skill_dir / "SKILL.md").write_text(
        "---\nname: demo-skill\ndescription: Demo skill for tests.\n---\n\n"
        "## Instructions\n\nDo the demo thing.\n",
        encoding="utf-8",
    )
    skills = _load_skills_from_dir(tmp_path)
    assert len(skills) == 1
    assert skills[0].name == "demo-skill"
    assert load_skill_from_dir(skill_dir).name == "demo-skill"


def test_all_domain_skills_load() -> None:
    skills = _load_skills_from_dir(_SKILLS_DIR)
    names = {skill.name for skill in skills}
    assert names == {
        "coffee-menu",
        "escalate",
        "faqs",
        "food-menu",
        "locations",
        "promotions",
    }


def test_skills_have_l3_references_where_expected() -> None:
    skills = _load_skills_from_dir(_SKILLS_DIR)
    by_name = {s.name: s for s in skills}
    assert "addresses.md" in by_name["locations"].resources.list_references()
    assert "sizes-prices.md" in by_name["coffee-menu"].resources.list_references()
    assert "pastries.md" in by_name["food-menu"].resources.list_references()
    assert by_name["escalate"].resources.references == {}
