import json


def write_json(target_filename: str, data: object) -> None:
    """Записать строку в файл json"""
    if data is None:
        return
    try:
        with open(target_filename, "w", encoding="utf8") as f:
            json.dump(data, f, indent=2, skipkeys=True, allow_nan=False, sort_keys=True)
    except Exception as e:
        print(f"Error during write jsom -> {e}")
        raise e
