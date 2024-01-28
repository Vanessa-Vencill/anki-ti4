"""
Code to generate Anki cards from a database
"""
import csv
from typing import List
from models import Mech, Flagship, Agent

def load_mechs() -> List[Mech]:
    """
    Load all mech data from csv.
    """
    mechs = []
    with open("data/mechs.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        header = next(reader)
        for row in reader:
            mech_data = Mech(
                row[0],
                row[1],
                row[2],
                row[3].split(","),
                row[4].split(",") + [row[0].lower()]
            )
            mechs.append(mech_data)

    return mechs

def load_flagships() -> List[Flagship]:
    """
    Load all flagship data from csv.
    """
    flagships = []
    with open("data/flagships.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        header = next(reader)
        for row in reader:
            flagship_data = Flagship(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6].split(","),
                row[7].split(",") + [row[0].lower()]
            )
            flagships.append(flagship_data)

    return flagships

def load_agents() -> List[Mech]:
    """
    Load all mech data from csv.
    """
    agents = []
    with open("data/agents.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter="|")
        header = next(reader)
        for row in reader:
            agent_data = Agent(
                row[0],
                row[1],
                row[2],
                row[3].split(",") + [row[0].lower()]
            )
            agents.append(agent_data)

    return agents

if __name__ == "__main__":
    data = load_mechs()
    for d in data:
        print(d)