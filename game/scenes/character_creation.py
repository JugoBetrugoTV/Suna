"""HOLLOWMERE - Character Creation Scene"""
from engine.display import (
    _RED, _GREEN, _YELLOW, _BLUE, _MAGENTA, _CYAN, _WHITE, _GRAY,
    _BOLD, _DIM, _RESET,
)

# Compatibility aliases
class Fore:
    RED = _RED; GREEN = _GREEN; YELLOW = _YELLOW; BLUE = _BLUE
    MAGENTA = _MAGENTA; CYAN = _CYAN; WHITE = _WHITE
    LIGHTBLACK_EX = _GRAY; LIGHTYELLOW_EX = _YELLOW
    LIGHTCYAN_EX = _CYAN; LIGHTBLUE_EX = _BLUE
    LIGHTGREEN_EX = _GREEN; LIGHTMAGENTA_EX = _MAGENTA
    LIGHTWHITE_EX = _WHITE

class Style:
    BRIGHT = _BOLD; DIM = _DIM; RESET_ALL = _RESET


def run(display, state):
    display.clear()
    display.blank()
    display.narration("Bevor wir beginnen...")
    display.pause(1.5)
    display.narration("Wer bist du?")
    display.blank()
    display.pause(1)

    # --- Name ---
    while True:
        print(f"  {Fore.YELLOW}Dein Name:{Style.RESET_ALL} ", end="")
        name = input().strip()
        if name:
            state.player_name = name
            break

    display.blank()
    display.pause(0.5)
    display.narration(f"{name}. Also gut.")
    display.pause(1)

    # --- Origin ---
    display.blank()
    display.narration("Warum bist du hier?")
    display.blank()
    display.pause(0.5)

    origin_choice = display.choice([
        ("Ich bin Journalist/in. Ich suche eine Geschichte.", None),
        ("Ich habe Verwandte hier. Zumindest hatte ich das.", None),
        ("Zufall. Autopanne. Falscher Ort, falsche Zeit.", None),
    ])

    if origin_choice == 0:
        state.origin = "journalist"
        state.attributes["perception"] += 1
        state.attributes["intellect"] += 1
        display.blank()
        display.narration("Ein/e Journalist/in. Immer auf der Suche nach der naechsten Story.")
        display.narration("Die Leute hier werden das nicht moegen.")
        display.system_msg("  [+1 Wahrnehmung, +1 Verstand]")
        state.set_flag("origin_journalist")
    elif origin_choice == 1:
        state.origin = "relative"
        state.attributes["empathy"] += 1
        display.blank()
        display.narration("Familie. Das schwerste Wort, das es gibt.")
        display.narration("Du hast einen Grund hier zu sein. Einen persoenlichen.")
        display.system_msg("  [+1 Empathie]")
        state.set_flag("origin_relative")
    else:
        state.origin = "stranger"
        display.blank()
        display.narration("Zufall. Das sagen sie alle.")
        display.narration("Vielleicht stimmt es sogar.")
        display.system_msg("  [Keine Attribut-Boni. Maximale Freiheit.]")
        state.set_flag("origin_stranger")

    display.pause(1.5)

    # --- Trauma ---
    display.blank()
    display.separator()
    display.blank()
    display.narration("Noch etwas. Bevor du ankommst.")
    display.pause(1)
    display.narration("Jeder traegt etwas mit sich. Etwas, das er lieber vergessen wuerde.")
    display.pause(1)
    display.narration("Was ist es bei dir?")
    display.blank()

    trauma_choice = display.choice([
        ("Ich habe jemanden verloren. Jemanden, der mir nahe stand.", None),
        ("Es gab einen Unfall. Es war meine Schuld.", None),
        ("Da ist eine Erinnerung. Aus der Kindheit. Ich kann sie nicht greifen.", None),
        ("Nichts. Mir geht es gut.", None),
    ])

    if trauma_choice == 0:
        state.trauma = "loss"
        display.blank()
        display.narration("Verlust. Er folgt dir wie ein Schatten.")
        display.narration("Du hoffst, dass die Entfernung hilft. Sie tut es nie.")
        state.set_flag("trauma_loss")
    elif trauma_choice == 1:
        state.trauma = "accident"
        state.modify_guilt(10)
        display.blank()
        display.narration("Schuld. Sie sitzt hinter deinen Augen.")
        display.narration("Egal wie oft du dir sagst, dass es ein Unfall war.")
        state.set_flag("trauma_accident")
    elif trauma_choice == 2:
        state.trauma = "memory"
        display.blank()
        display.narration("Eine Erinnerung, die sich wehrt, ans Licht zu kommen.")
        display.narration("Vielleicht ist es besser so.")
        state.set_flag("trauma_memory")
    else:
        state.trauma = "none"
        display.blank()
        display.narration("Nichts. Alles in Ordnung.")
        display.pause(1)
        display.narration("...")
        display.pause(1)
        display.narration("Wenn du das sagst.", Fore.LIGHTBLACK_EX)
        state.set_flag("trauma_none")

    display.pause(1.5)

    # --- Attributes ---
    display.clear()
    display.blank()
    display.narration("Was fuer ein Mensch bist du?")
    display.pause(1)
    display.blank()
    _attribute_allocation(display, state)

    display.pause(1)
    display.clear()
    display.blank()
    _show_character_summary(display, state)
    display.wait_key()


def _attribute_allocation(display, state):
    """Let the player distribute 10 remaining points across 5 attributes."""
    # Calculate already spent points from origin bonuses
    spent = sum(state.attributes.values()) - 5  # 5 base points (1 each)
    remaining = 10 - spent

    attr_names = {
        "willpower": ("Willenskraft", "Mentale Staerke. Widerstand gegen Horror und Manipulation."),
        "empathy": ("Empathie", "Einfuehlungsvermoegen. Menschen lesen, Vertrauen aufbauen."),
        "perception": ("Wahrnehmung", "Aufmerksamkeit. Details und Unstimmigkeiten bemerken."),
        "aggression": ("Gewaltbereitschaft", "Bereitschaft zur Eskalation. Verbal und physisch."),
        "intellect": ("Verstand", "Analytisches Denken. Logik und Deduktion."),
    }

    print(f"  {Fore.YELLOW}Verteile {remaining} Punkte auf deine Attribute.{Style.RESET_ALL}")
    print(f"  {Style.DIM}Jedes Attribut hat bereits 1 Punkt (+ eventuelle Boni).{Style.RESET_ALL}")
    print(f"  {Style.DIM}Maximum pro Attribut: 5{Style.RESET_ALL}")
    display.blank()

    for key, (name, desc) in attr_names.items():
        current = state.attributes[key]
        print(f"  {Fore.CYAN}{name}{Style.RESET_ALL} (aktuell: {current})")
        print(f"  {Style.DIM}{desc}{Style.RESET_ALL}")
        max_add = min(remaining, 5 - current)

        if remaining == 0:
            print(f"  {Style.DIM}Keine Punkte uebrig.{Style.RESET_ALL}")
            display.blank()
            continue

        while True:
            print(f"  {Fore.YELLOW}Punkte hinzufuegen (0-{max_add}, uebrig: {remaining}):{Style.RESET_ALL} ", end="")
            try:
                raw = input().strip()
                if not raw:
                    val = 0
                else:
                    val = int(raw)
                if 0 <= val <= max_add:
                    state.attributes[key] += val
                    remaining -= val
                    break
            except (ValueError, EOFError):
                pass
        display.blank()

    # If points remain, distribute automatically
    if remaining > 0:
        for key in state.attributes:
            while remaining > 0 and state.attributes[key] < 5:
                state.attributes[key] += 1
                remaining -= 1
        display.system_msg(f"  [Verbleibende Punkte automatisch verteilt.]")


def _show_character_summary(display, state):
    attr_de = {
        "willpower": "Willenskraft",
        "empathy": "Empathie",
        "perception": "Wahrnehmung",
        "aggression": "Gewaltbereitschaft",
        "intellect": "Verstand",
    }

    origin_de = {
        "journalist": "Journalist/in",
        "relative": "Verwandtschaft in Hollowmere",
        "stranger": "Zufaellig hier",
    }

    trauma_de = {
        "loss": "Verlust einer nahestehenden Person",
        "accident": "Schuld an einem Unfall",
        "memory": "Verdraengte Kindheitserinnerung",
        "none": "-- Verweigert --",
    }

    display.separator("═")
    print(f"  {Fore.YELLOW}{Style.BRIGHT}{state.player_name}{Style.RESET_ALL}")
    display.separator()
    print(f"  Herkunft: {Fore.CYAN}{origin_de.get(state.origin, '?')}{Style.RESET_ALL}")
    print(f"  Trauma:   {Fore.MAGENTA}{trauma_de.get(state.trauma, '?')}{Style.RESET_ALL}")
    display.blank()

    for key, name in attr_de.items():
        val = state.attributes[key]
        bar = "█" * val + "░" * (5 - val)
        print(f"  {name:20s} {Fore.CYAN}{bar} {val}{Style.RESET_ALL}")

    display.blank()
    print(f"  Mental State: {Fore.GREEN}{'█' * 16}{'░' * 4} {state.mental_state}%{Style.RESET_ALL}")
    display.separator("═")
    display.blank()
    display.narration("Das bist du. Oder zumindest das, was du glaubst zu sein.")
