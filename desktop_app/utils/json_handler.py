import json
from pathlib import Path

class JsonHandler:
    def load_json(file_path: str) -> dict:
        
        path = Path(file_path)
        if not path.exists():
            return {}
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
        
    def save_json(file_path: str, data: dict) -> None:
        path = Path(file_path)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)