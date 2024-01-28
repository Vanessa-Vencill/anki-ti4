"""
Model for cards. Each card model contains a render_template() function
which specifies how the card should be rendered.
"""

from dataclasses import dataclass
from typing import List

@dataclass
class Mech:
    """
    Data class for mech information
    """
    faction: str
    name: str
    ability: str
    keywords: List[str]
    tags: List[str]

    def render_template(self) -> str:
        """
        Render the card template.
        """
        title = f"Complete the Mech Unit Card."
        c1 = "<br><b>Faction</b>: {{c1::" + self.faction + " }}"
        c2 = "<br><b>Name</b>: {{c2::" + self.name + " }}"
        c3 = "<br><b>Ability</b>: {{c3::" + self.ability + " }}"
        c4 = "<br><b>Keywords</b>: {{c4::" + ",".join(self.keywords) + " }}"
        return f"{title}{c1}{c2}{c3}{c4}"


@dataclass
class Flagship:
    """
    Data class for flagship information
    """
    faction: str
    name: str
    combat: str
    move: str
    capacity: str
    ability: str
    keywords: List[str]
    tags: List[str]

    def render_template(self) -> str:
        """
        Render the card template.
        """
        title = f"Complete the Flagship Unit Card."
        c1 = "<br><b>Faction</b>: {{c1::" + self.faction + " }}"
        c2 = "<br><b>Name</b>: {{c2::" + self.name + " }}"
        c3 = "<br><b>Combat</b>: {{c3::" + self.combat + " }}"
        c4 = "<br><b>Move</b>: {{c4::" + self.move + " }}"
        c5 = "<br><b>Capacity</b>: {{c5::" + self.capacity + " }}"
        c6 = "<br><b>Ability</b>: {{c6::" + self.ability + " }}"
        c7 = "<br><b>Keywords</b>: {{c7::" + ",".join(self.keywords) + " }}"
        return f"{title}{c1}{c2}{c3}{c4}{c5}{c6}{c7}"


@dataclass
class Agent:
    """
    Data class for agent information
    """
    faction: str
    name: str
    ability: str
    tags: List[str]

    def render_template(self) -> str:
        """
        Render the card template.
        """
        title = f"Complete the Agent Card."
        c1 = "<br><b>Faction</b>: {{c1::" + self.faction + " }}"
        c2 = "<br><b>Name</b>: {{c2::" + self.name + " }}"
        c3 = "<br><b>Ability</b>: {{c3::" + self.ability + " }}"
        return f"{title}{c1}{c2}{c3}"