import json

PATH = "data/notes.json"

def load_notes():
    with open(PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def save_notes(notes):
    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2,ensure_ascii=False)

    