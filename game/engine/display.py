"""HOLLOWMERE - Game Engine: Display System
Uses ANSI escape codes directly -- no external dependencies needed.
"""
import sys
import time
import random
import os
import shutil

# ANSI escape codes -- work on Windows 10+ and all Unix terminals
_ESC = "\033["
_RESET = f"{_ESC}0m"
_BOLD = f"{_ESC}1m"
_DIM = f"{_ESC}2m"

# Foreground colors
_RED = f"{_ESC}91m"
_GREEN = f"{_ESC}92m"
_YELLOW = f"{_ESC}93m"
_BLUE = f"{_ESC}94m"
_MAGENTA = f"{_ESC}95m"
_CYAN = f"{_ESC}96m"
_WHITE = f"{_ESC}97m"
_GRAY = f"{_ESC}90m"
_LIGHT_YELLOW = f"{_ESC}93m"
_LIGHT_CYAN = f"{_ESC}96m"
_LIGHT_BLUE = f"{_ESC}94m"
_LIGHT_GREEN = f"{_ESC}92m"
_LIGHT_MAGENTA = f"{_ESC}95m"
_LIGHT_WHITE = f"{_ESC}97m"


def _enable_windows_ansi():
    """Enable ANSI/VT100 escape codes on Windows 10+."""
    if os.name == "nt":
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            # STD_OUTPUT_HANDLE = -11
            handle = kernel32.GetStdHandle(-11)
            # ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
            mode = ctypes.c_ulong()
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)
        except Exception:
            pass


_enable_windows_ansi()


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
        os.system("cls" if os.name == "nt" else "clear")

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

    def type_text(self, text, color=_WHITE, speed=None, glitch=True):
        spd = speed or self.text_speed
        for ch in text:
            out = self._glitch_char(ch) if glitch else ch
            sys.stdout.write(color + out)
            sys.stdout.flush()
            time.sleep(spd)
        sys.stdout.write(_RESET)
        print()

    def narration(self, text, speed=None):
        self.type_text(text, _GRAY, speed or self.SLOW)

    def dialogue(self, speaker, text, color=_WHITE):
        sys.stdout.write(_BOLD + color + speaker + ": " + _RESET)
        sys.stdout.flush()
        self.type_text(text, _WHITE, self.NORMAL)

    def thought(self, text):
        self.type_text(f"  ({text})", _MAGENTA, self.SLOW)

    def horror(self, text):
        self.type_text(text, _RED, self.SLOW)

    def system_msg(self, text):
        print(_DIM + _CYAN + text + _RESET)

    def warning(self, text):
        print(_YELLOW + _BOLD + text + _RESET)

    def separator(self, char="─"):
        print(_GRAY + char * self.width + _RESET)

    def blank(self, lines=1):
        print("\n" * (lines - 1))

    def pause(self, seconds=1.0):
        time.sleep(seconds)

    def wait_key(self, prompt="  [Weiter...]"):
        print(_DIM + _GRAY + prompt + _RESET, end="")
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
            if text.startswith("["):
                bracket_end = text.find("]")
                if bracket_end > 0:
                    tag = text[: bracket_end + 1]
                    rest = text[bracket_end + 1 :]
                    print(f"  {_YELLOW}{display_idx}. {_CYAN}{tag}{_WHITE}{rest}{_RESET}")
                    continue
            print(f"  {_YELLOW}{display_idx}. {_WHITE}{text}{_RESET}")

        while True:
            try:
                sys.stdout.write(_YELLOW + "\n  > " + _RESET)
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
        print(_RED + _BOLD + title + _RESET)
        print(_GRAY + "    Ein Ort, der auf keiner Karte verzeichnet ist.".center(self.width) + _RESET)
        self.blank(2)

    def status_bar(self, state):
        ms = state.mental_state
        if ms > 70:
            ms_color = _GREEN
            ms_label = "Stabil"
        elif ms > 50:
            ms_color = _YELLOW
            ms_label = "Angespannt"
        elif ms > 30:
            ms_color = _RED
            ms_label = "Instabil"
        elif ms > 10:
            ms_color = _RED + _BOLD
            ms_label = "Gebrochen"
        else:
            ms_color = _MAGENTA + _BOLD
            ms_label = "Verloren"

        bar_len = 20
        filled = int((ms / 100) * bar_len)
        bar = "█" * filled + "░" * (bar_len - filled)

        self.separator()
        line = f"  Mental State: {ms_color}{bar} {ms}% ({ms_label}){_RESET}"
        line += f"  │  Tag {state.day}"
        if state.current_time:
            line += f"  │  {state.current_time}"
        print(line)
        self.separator()

    def show_notebook_entry(self, entry):
        print(f"\n  {_YELLOW}Notizbuch:{_RESET}")
        print(f"  {_WHITE}{_DIM}{entry}{_RESET}\n")

    def darkness(self, seconds=3):
        """Screen goes dark for a moment."""
        self.clear()
        self.pause(seconds)

    def flicker_text(self, text, times=3):
        for _ in range(times):
            sys.stdout.write(_RED + text + "\r")
            sys.stdout.flush()
            time.sleep(0.15)
            sys.stdout.write(" " * len(text) + "\r")
            sys.stdout.flush()
            time.sleep(0.1)
        print(_RED + text + _RESET)
