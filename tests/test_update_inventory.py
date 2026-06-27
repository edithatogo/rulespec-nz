from pathlib import Path
import yaml

from _update_inventory import extract_rule_info

def test_extract_rule_info_with_explicit_source_family(tmp_path: Path):
    yaml_content = {
        "rules": [
            {
                "name": "rule1",
                "kind": "variable",
                "source_family": "custom_family"
            }
        ]
    }
    file_path = tmp_path / "test.yaml"
    file_path.write_text(yaml.dump(yaml_content), encoding="utf-8")

    result = extract_rule_info(file_path, "nz/test.yaml")

    assert len(result) == 1
    assert result[0] == {
        "id": "nz:test#rule1",
        "name": "rule1",
        "kind": "variable",
        "source_family": "custom_family"
    }

def test_extract_rule_info_implicit_source_family(tmp_path: Path):
    yaml_content = {
        "rules": [
            {
                "name": "rule2",
                # no kind, should default to "parameter"
                # no source_family, should default to filename "test2"
            }
        ]
    }
    file_path = tmp_path / "test2.yaml"
    file_path.write_text(yaml.dump(yaml_content), encoding="utf-8")

    result = extract_rule_info(file_path, "prefix/target/test2.yaml")

    assert len(result) == 1
    assert result[0] == {
        "id": "prefix:target/test2#rule2",
        "name": "rule2",
        "kind": "parameter",
        "source_family": "test2"
    }

def test_extract_rule_info_empty_or_missing_rules(tmp_path: Path):
    yaml_content = {} # Missing rules
    file_path = tmp_path / "test3.yaml"
    file_path.write_text(yaml.dump(yaml_content), encoding="utf-8")

    result = extract_rule_info(file_path, "nz/test3.yaml")
    assert result == []

    yaml_content_empty = {"rules": []} # Empty rules
    file_path_empty = tmp_path / "test4.yaml"
    file_path_empty.write_text(yaml.dump(yaml_content_empty), encoding="utf-8")

    result_empty = extract_rule_info(file_path_empty, "nz/test4.yaml")
    assert result_empty == []

def test_extract_rule_info_non_dict_rule(tmp_path: Path):
    yaml_content = {
        "rules": [
            "this is a string, not a dict",
            {
                "name": "rule3"
            }
        ]
    }
    file_path = tmp_path / "test5.yaml"
    file_path.write_text(yaml.dump(yaml_content), encoding="utf-8")

    result = extract_rule_info(file_path, "nz/test5.yaml")

    assert len(result) == 1
    assert result[0]["name"] == "rule3"
