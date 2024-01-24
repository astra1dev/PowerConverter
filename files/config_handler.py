import json


def path_to_ffmpeg():
    try:
        with (open("config.json", "r") as cfg):
            path = json.load(cfg).get("anything", False)  # default to false if key not found
            if path is False:
                return None
            return path
    except (FileNotFoundError, json.JSONDecodeError):
        return None
