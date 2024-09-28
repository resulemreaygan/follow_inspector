"""
Author: Resul Emre AYGAN
"""

import json

import yaml


def load_yaml_config(yaml_path: str = "config.yaml") -> dict:
    """
    Load configuration settings from a YAML file.

    :param yaml_path: Path to the YAML configuration file. Default is "config.yaml", type str
    :return: Configuration settings, type dict
    """

    with open(yaml_path, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)
    return config


def load_json_data(file_path: str) -> list | dict | None:
    """
    Load data from a JSON file.

    :param file_path: Path to the JSON file, type str
    :return: JSON data as a dictionary. Returns None if file not found or invalid JSON, type dict
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file: {file_path}")
        return None
