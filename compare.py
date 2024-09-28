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


def extract_usernames(data: list[dict]) -> dict:
    """
    Extract usernames from the given list of user dictionaries.

    :param data: List of dictionaries containing user data, type List[dict]
    :return: A set of usernames extracted from the user data, type dict
    """
    return {
        item.get("string_list_data")[0]
        .get("value"): item.get("string_list_data")[0]
        .get("href")
        for item in data
    }


def compare_followers_and_followings(followers: dict, followings: dict) -> None:
    """
    Compare followers and followings to find those who don't follow you back.

    :param followers: A dictionary with usernames as keys and profile links as values who follow you, type dict
    :param followings: A dictionary with usernames as keys and profile links as values whom you follow, type dict
    :return: None
    """

    not_following_back = {
        user: followings[user] for user in followings if user not in followers
    }

    if not not_following_back:
        print("All the people you follow are following you back!\n")
    else:
        print("People who don't follow you back:\n")

        for user, link in not_following_back.items():
            print(f"{user}: {link}")

        print("\n")


def main() -> None:
    """
    Main function to execute the script. Loads the configuration,
    reads followers and followings data, and compares them to find
    discrepancies.

    :return: None
    """

    config = load_yaml_config()

    followers_data = load_json_data(config["followers_file"])
    followings_data = load_json_data(config["followings_file"])

    if not followers_data or not followings_data:
        print("Error loading data files.")
        return

    followers = extract_usernames(data=followers_data)
    followings = extract_usernames(data=followings_data.get("relationships_following"))

    compare_followers_and_followings(followers=followers, followings=followings)


if __name__ == "__main__":
    main()
