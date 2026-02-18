class Skills:
    def __init__(self, tech, soft):
        self.tech = tech      # dict
        self.soft = soft      # list

    def to_dict(self):
        return {
            "tech": self.tech,
            "soft": self.soft
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["tech"], data["soft"])