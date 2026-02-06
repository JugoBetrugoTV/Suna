"""HOLLOWMERE - Game Engine: Game State"""


class GameState:
    """Central game state tracking all player data, relationships, and flags."""

    def __init__(self):
        # Player identity
        self.player_name = ""
        self.origin = ""  # "journalist", "relative", "stranger"
        self.trauma = ""  # "loss", "accident", "memory", "none"

        # Attributes (1-7, start with 15 points across 5)
        self.attributes = {
            "willpower": 1,    # Willenskraft
            "empathy": 1,      # Empathie
            "perception": 1,   # Wahrnehmung
            "aggression": 1,   # Gewaltbereitschaft
            "intellect": 1,    # Verstand
        }

        # Core systems
        self.mental_state = 80
        self.guilt = 0
        self.day = 1
        self.current_time = "Abend"

        # NPC relationships (0-100)
        self.relationships = {
            "maren": 50,
            "brandt": 40,
            "ernst": 30,
            "nina": 35,
            "lena": 40,
            "hilde": 45,
            "lilly": 50,
            "konrad": 20,
            "jona": 30,
        }

        # NPC trust levels
        self.trust = {
            "maren": "neutral",
            "brandt": "neutral",
            "ernst": "suspicious",
            "nina": "neutral",
            "lena": "neutral",
        }

        # Story flags
        self.flags = set()

        # Notebook entries
        self.notebook = []

        # Known clues
        self.clues = set()

        # Inventory
        self.inventory = []

        # Decisions log
        self.decisions = []

    def attr(self, name):
        return self.attributes.get(name, 0)

    def check(self, attr_name, threshold):
        return self.attr(attr_name) >= threshold

    def modify_mental_state(self, amount):
        self.mental_state = max(0, min(100, self.mental_state + amount))

    def modify_guilt(self, amount):
        self.guilt = max(0, min(100, self.guilt + amount))

    def modify_relationship(self, npc, amount):
        if npc in self.relationships:
            self.relationships[npc] = max(0, min(100, self.relationships[npc] + amount))
            self._update_trust(npc)

    def _update_trust(self, npc):
        if npc not in self.trust:
            return
        val = self.relationships[npc]
        if val <= 20:
            self.trust[npc] = "suspicious"
        elif val <= 50:
            self.trust[npc] = "neutral"
        elif val <= 70:
            self.trust[npc] = "open"
        elif val <= 90:
            self.trust[npc] = "trusted"
        else:
            self.trust[npc] = "trusted"

    def set_flag(self, flag):
        self.flags.add(flag)

    def has_flag(self, flag):
        return flag in self.flags

    def add_clue(self, clue):
        self.clues.add(clue)

    def has_clue(self, clue):
        return clue in self.clues

    def add_notebook(self, entry):
        self.notebook.append(entry)

    def add_decision(self, decision):
        self.decisions.append(decision)

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    def has_item(self, item):
        return item in self.inventory

    def advance_time(self):
        times = ["Morgen", "Nachmittag", "Abend", "Nacht"]
        idx = times.index(self.current_time) if self.current_time in times else 0
        if idx == 3:
            self.day += 1
            self.current_time = "Morgen"
        else:
            self.current_time = times[idx + 1]

    def rel(self, npc):
        return self.relationships.get(npc, 0)

    def get_mental_tier(self):
        ms = self.mental_state
        if ms > 70:
            return "stable"
        elif ms > 50:
            return "tense"
        elif ms > 30:
            return "unstable"
        elif ms > 10:
            return "broken"
        return "lost"
