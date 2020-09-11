from dataclasses import dataclass


@dataclass
class Award:
    name: str
    min_score: int
    subtitle: str = None
    cash: int = 0

    def to_dict(self):
        return {
            "name": self.name,
            "min_score": self.min_score,
            "subtitle": self.subtitle,
            "cash": self.cash,
        }


awards = [
    Award(
        name="Gold",
        subtitle="Commando/Diver/Guards",
        cash=500,
        min_score=90,
    ),
    Award(
        name="Gold",
        cash=500,
        min_score=85,
    ),
    Award(
        name="Sliver",
        cash=300,
        min_score=75,
    ),
    Award(
        name="Pass",
        subtitle="NSMen incentive",
        min_score=61,
    ),
    Award(
        name="Pass*",
        subtitle="NSMen only",
        min_score=51,
    ),
    Award(
        name="Fail",
        min_score=0,
    ),
]
