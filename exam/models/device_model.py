class Device:
    def __init__(self, type_, brand, year):
        self.type = type_
        self.brand = brand
        self.year = year

    def to_dict(self):
        return {
            "type": self.type,
            "brand": self.brand,
            "year": self.year
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["type"], data["brand"], data["year"])