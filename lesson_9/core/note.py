from typing import Union # helps to accept multiple types of value. Or we can write date_created | str
from datetime import datetime
from __future__ import annotations

class Note:
    def __init__(self, *, id: int, text: str, date_created: Union[datetime, str]):
        self.id = id
        self.text = text
        self.date_created = date_created

    def __str__(self):
        return f"Note(id={self.id}, text={self.text}, date_created={self.date_created})"

    @staticmethod
    def from_json(jsonData: dict[str, str]) -> Note:
        return Note(id=jsonData["id"], text=jsonData["text"], date_created=jsonData["date_created"])

    @staticmethod
    def from_tuple(tupleData: tuple) -> Note:
        return Note(id=tupleData[0], text=tupleData[1], date_created=tupleData[2])