"""HOLLOWMERE - Game Engine: Display System"""
import sys
import time
import random
import os
import shutil
from colorama import Fore, Back, Style, init

init(autoreset=True)


class Display:
    """Handles all terminal output with atmospheric effects."""

    SLOW = 0.03
    NORMAL = 0.02
    FAST = 0.01

    def __init__(self):
        self.width = min(shutil.get_terminal_size().columns, 80)
        self.text_speed = self.NORMAL
        self.glitch_chance = 0.0

    def clear(self):
        os.system("clear" if os.name != "nt" else "cls")

    def set_glitch(self, mental_state):
        if mental_state > 70:
            self.glitch_chance = 0.0
        elif mental_state > 50:
            self.glitch_chance = 0.02
        elif mental_state > 30:
            self.glitch_chance = 0.06
        elif mental_state > 10:
            self.glitch_chance = 0.12
        else:
            self.glitch_chance = 0.25

    def _glitch_char(self, c):
        if random.random() < self.glitch_chance and c not in ("\n", " "):
            glitches = "░▒▓█▄▀■□▪▫"
            return random.choice(glitches)
        return c

    def type_text(self, text, color=Fore.WHITE, speed=None, glitch=True):
        spd = speed or self.text_speed
        for ch in text:
            out = self._glitch_char(ch) if glitch else ch
            sys.stdout.write(color + out)
            sys.stdout.flush()
            time.sleep(spd)
        sys.stdout.write(Style.RESET_ALL)
        print()

    def narration(self, text, speed=None):
        self.type_text(text, Fore.LIGHTBLACK_EX, speed or self.SLOW)

    def dialogue(self, speaker, text, color=Fore.WHITE):
        sys.stdout.write(Style.BRIGHT + color + speaker + ": " + Style.RESET_ALL)
        sys.stdout.flush()
        self.type_text(text, Fore.WHITE, self.NORMAL)

    def thought(self, text):
        self.type_text(f"  ({text})", Fore.MAGENTA, self.SLOW)

    def horror(self, text):
        self.type_text(text, Fore.RED, self.SLOW)

    def system_msg(self, text):
        print(Style.DIM + Fore.CYAN + text + Style.RESET_ALL)

    def warning(self, text):
        print(Fore.YELLOW + Style.BRIGHT + text + Style.RESET_ALL)

    def separator(self, char="─"):
        print(Fore.LIGHTBLACK_EX + char * self.width + Style.RESET_ALL)

    def blank(self, lines=1):
        print("\n" * (lines - 1))

    def pause(self, seconds=1.0):
        time.sleep(seconds)

    def wait_key(self, prompt="  [Weiter...]"):
        print(Style.DIM + Fore.LIGHTBLACK_EX + prompt + Style.RESET_ALL, end="")
        input()

    def choice(self, options, state=None):
        """Display choices and return selected index (0-based).

        options: list of tuples (text, requirement_fn_or_None)
        state: GameState for requirement checks
        """
        print()
        available = []
        for i, (text, req) in enumerate(options):
            if req is None or (state and req(state)):
                available.append((i, text))

        if not available:
            available = [(0, options[0][0])]

        for display_idx, (_, text) in enumerate(available, 1):
            color = Fore.WHITE
            if text.startswith("["):
                bracket_end = text.find("]")
                if bracket_end > 0:
                    tag = text[: bracket_end + 1]
                    rest = text[bracket_end + 1 :]
                    print(f"  {Fore.YELLOW}{display_idx}. {Fore.CYAN}{tag}{Fore.WHITE}{rest}{Style.RESET_ALL}")
                    continue
            print(f"  {Fore.YELLOW}{display_idx}. {color}{text}{Style.RESET_ALL}")

        while True:
            try:
                sys.stdout.write(Fore.YELLOW + "\n  > " + Style.RESET_ALL)
                raw = input().strip()
                if not raw:
                    continue
                idx = int(raw)
                if 1 <= idx <= len(available):
                    return available[idx - 1][0]
            except (ValueError, EOFError):
                pass

    def title_screen(self):
        self.clear()
        title = r"""
    ██╗  ██╗ ██████╗ ██╗     ██╗      ██████╗ ██╗    ██╗
    ██║  ██║██╔═══██╗██║     ██║     ██╔═══██╗██║    ██║
    ███████║██║   ██║██║     ██║     ██║   ██║██║ █╗ ██║
    ██╔══██║██║   ██║██║     ██║     ██║   ██║██║███╗██║
    ██║  ██║╚██████╔╝███████╗███████╗╚██████╔╝╚███╔███╔╝
    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝

    ███╗   ███╗███████╗██████╗ ███████╗
    ████╗ ████║██╔════╝██╔══██╗██╔════╝
    ██╔████╔██║█████╗  ██████╔╝█████╗
    ██║╚██╔╝██║██╔══╝  ██╔══██╗██╔══╝
    ██║ ╚═╝ ██║███████╗██║  ██║███████╗
    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
"""
        print(Fore.RED + Style.BRIGHT + title + Style.RESET_ALL)
        print(Fore.LIGHTBLACK_EX + "    Ein Ort, der auf keiner Karte verzeichnet ist.".center(self.width) + Style.RESET_ALL)
        self.blank(2)

    def status_bar(self, state):
        ms = state.mental_state
        if ms > 70:
            ms_color = Fore.GREEN
            ms_label = "Stabil"
        elif ms > 50:
            ms_color = Fore.YELLOW
            ms_label = "Angespannt"
        elif ms > 30:
            ms_color = Fore.RED
            ms_label = "Instabil"
        elif ms > 10:
            ms_color = Fore.RED + Style.BRIGHT
            ms_label = "Gebrochen"
        else:
            ms_color = Fore.MAGENTA + Style.BRIGHT
            ms_label = "Verloren"

        bar_len = 20
        filled = int((ms / 100) * bar_len)
        bar = "█" * filled + "░" * (bar_len - filled)

        self.separator()
        line = f"  Mental State: {ms_color}{bar} {ms}% ({ms_label}){Style.RESET_ALL}"
        line += f"  │  Tag {state.day}"
        if state.current_time:
            line += f"  │  {state.current_time}"
        print(line)
        self.separator()

    def show_notebook_entry(self, entry):
        print(f"\n  {Fore.YELLOW}📓 Notizbuch:{Style.RESET_ALL}")
        print(f"  {Fore.WHITE}{Style.DIM}{entry}{Style.RESET_ALL}\n")

    def darkness(self, seconds=3):
        """Screen goes dark for a moment."""
        self.clear()
        self.pause(seconds)

    def flicker_text(self, text, times=3):
        for _ in range(times):
            sys.stdout.write(Fore.RED + text + "\r")
            sys.stdout.flush()
            time.sleep(0.15)
            sys.stdout.write(" " * len(text) + "\r")
            sys.stdout.flush()
            time.sleep(0.1)
        print(Fore.RED + text + Style.RESET_ALL)
