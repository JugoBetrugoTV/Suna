#!/usr/bin/env python3
"""
HOLLOWMERE - A Story-Driven Horror RPG
=======================================
Run with: python3 main.py
"""
import sys
import os
import time
from colorama import Fore, Style, init

# Ensure the game package is importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from engine.display import Display
from engine.game_state import GameState
from scenes import character_creation
from scenes import act1_ch1_arrival
from scenes import act1_ch2_cracks
from scenes import act1_ch3_missing

init(autoreset=True)


def intro(display):
    display.clear()
    time.sleep(1)
    display.type_text("  ...", Fore.LIGHTBLACK_EX, 0.3)
    time.sleep(2)
    display.clear()
    time.sleep(1)

    lines = [
        "Es gibt Orte, die auf keiner Karte verzeichnet sind.",
        "Nicht weil sie vergessen wurden.",
        "Sondern weil jemand dafuer gesorgt hat.",
        "",
        "Du wirst gleich an einem solchen Ort ankommen.",
        "Die Leute dort werden freundlich sein.",
        "Sie werden laecheln.",
        "",
        "Glaub ihnen nicht.",
    ]

    for line in lines:
        if line == "":
            display.blank()
            time.sleep(0.5)
        else:
            display.type_text(f"  {line}", Fore.LIGHTBLACK_EX, 0.04)
            time.sleep(0.8)

    display.blank()
    time.sleep(2)
    display.type_text("  Glaub dir selbst auch nicht.", Fore.RED, 0.05)
    time.sleep(3)
    display.clear()


def main():
    display = Display()
    state = GameState()

    try:
        # Title screen
        display.title_screen()
        display.wait_key("  [Druecke ENTER um zu beginnen...]")

        # Intro
        intro(display)

        # Character creation
        character_creation.run(display, state)

        # Update glitch based on mental state
        display.set_glitch(state.mental_state)

        # Act 1
        act1_ch1_arrival.run(display, state)
        display.set_glitch(state.mental_state)

        act1_ch2_cracks.run(display, state)
        display.set_glitch(state.mental_state)

        act1_ch3_missing.run(display, state)
        display.set_glitch(state.mental_state)

        # End screen
        display.blank()
        display.wait_key("  [ENTER zum Beenden]")
        display.clear()

    except KeyboardInterrupt:
        display.clear()
        print(f"\n  {Fore.RED}Du versuchst zu fliehen.{Style.RESET_ALL}")
        time.sleep(1)
        print(f"  {Fore.LIGHTBLACK_EX}Hollowmere laesst dich gehen.{Style.RESET_ALL}")
        time.sleep(1)
        print(f"  {Fore.LIGHTBLACK_EX}Diesmal.{Style.RESET_ALL}")
        time.sleep(1)
        print()


if __name__ == "__main__":
    main()
