class Family:
    def __init__(self, siblings, income):
        self.siblings = siblings
        self.income = income

    def to_dict(self):
        return {
            "siblings": self.siblings,
            "income": self.income
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["siblings"], data["income"])