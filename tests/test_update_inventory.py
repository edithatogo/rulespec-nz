import pathlib
import yaml

from _update_inventory import extract_rule_info

def test_extract_rule_info_happy_path(tmp_path: pathlib.Path):
    # Setup
    test_file = tmp_path / "test_module.yaml"
    rel_path = "nz/statutes/test_module.yaml"

    yaml_content = {
        "rules": [
            {
                "name": "rule1",
                "kind": "parameter",
                "source_family": "custom_family"
            },
            {
                "name": "rule2",
                "kind": "formula"
                # missing source_family, should fall back to rel_path's name
            }
        ]
    }
    test_file.write_text(yaml.dump(yaml_content), encoding="utf-8")

    # Execute
    result = extract_rule_info(test_file, rel_path)

    # Verify
    assert len(result) == 2

    assert result[0] == {
        "id": "nz:statutes/test_module#rule1",
        "name": "rule1",
        "kind": "parameter",
        "source_family": "custom_family",
    }

    assert result[1] == {
        "id": "nz:statutes/test_module#rule2",
        "name": "rule2",
        "kind": "formula",
        "source_family": "test_module",
    }

def test_extract_rule_info_empty_rules(tmp_path: pathlib.Path):
    test_file = tmp_path / "empty.yaml"
    rel_path = "nz/empty.yaml"
    test_file.write_text(yaml.dump({"rules": []}), encoding="utf-8")

    result = extract_rule_info(test_file, rel_path)
    assert result == []

def test_extract_rule_info_no_rules_key(tmp_path: pathlib.Path):
    test_file = tmp_path / "no_rules.yaml"
    rel_path = "nz/no_rules.yaml"
    test_file.write_text(yaml.dump({"other_key": "value"}), encoding="utf-8")

    result = extract_rule_info(test_file, rel_path)
    assert result == []

def test_extract_rule_info_invalid_rule_type(tmp_path: pathlib.Path):
    test_file = tmp_path / "invalid.yaml"
    rel_path = "nz/invalid.yaml"
    # A rule that is not a dict
    yaml_content = {
        "rules": [
            "this is just a string, not a dict",
            {
                "name": "valid_rule",
            }
        ]
    }
    test_file.write_text(yaml.dump(yaml_content), encoding="utf-8")

    result = extract_rule_info(test_file, rel_path)
    assert len(result) == 1
    assert result[0]["name"] == "valid_rule"
