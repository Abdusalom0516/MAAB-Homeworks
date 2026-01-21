from typing import Union # helps to accept multiple types of value. Or we can write date_created | str
from datetime import datetime


class Note:
    def __init__(self, id: int, text: str, date_created: Union[datetime, str]):
        self.id = id
        self.text = text
        self.date_created = date_created