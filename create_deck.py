import os
from anki.storage import Collection
from models import Mech
from data_loader import load_mechs, load_flagships, load_agents

# Setup the Anki Directory
anki_home = "/home/map/AnkiTest/User 1"
anki_collection_path = os.path.join(anki_home, "collection.anki2")

# Load the Anki Collection
col = Collection(anki_collection_path)

# Find the model to use, and set the deck
modelCloze = col.models.by_name("Cloze")
deck = col.decks.by_name("Twilight Imperium")
col.decks.select(deck["id"])
col.decks.current()["mid"] = modelCloze["id"]

# Create a new set of cards
mech_data = load_mechs()
flagship_data = load_flagships()
agent_data = load_agents()

all_model_data = mech_data + flagship_data + agent_data

for model in all_model_data:
    note = col.newNote()
    note.fields[0] = model.render_template()
    for tag in model.tags:
        note.add_tag(tag)
    col.add_note(note, deck["id"])

