from exam.models.device_model import Device
from exam.models.family_model import Family
from exam.models.skills_model import Skills


class Profile:
    def __init__(self, hobbies, skills, family, devices):
        self.hobbies = hobbies              # list[str]
        self.skills = skills                # Skills object
        self.family = family                # Family object
        self.devices = devices              # list[Device]

    def to_dict(self):
        return {
            "hobbies": self.hobbies,
            "skills": self.skills.to_dict(),
            "family": self.family.to_dict(),
            "devices": [d.to_dict() for d in self.devices]
        }

    @classmethod
    def from_dict(cls, data):
        skills = Skills.from_dict(data["skills"])
        family = Family.from_dict(data["family"])
        devices = [Device.from_dict(d) for d in data["devices"]]

        return cls(data["hobbies"], skills, family, devices)