"""HOLLOWMERE - Act 1, Chapter 3: Der Vermisste"""
from engine.display import (
    _RED, _GREEN, _YELLOW, _BLUE, _MAGENTA, _CYAN, _WHITE, _GRAY,
    _BOLD, _DIM, _RESET,
)

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
    display.separator("═")
    print(f"  {Fore.RED}{Style.BRIGHT}AKT 1{Style.RESET_ALL}")
    print(f"  {Fore.LIGHTBLACK_EX}Kapitel 3: Der Vermisste{Style.RESET_ALL}")
    display.separator("═")
    display.blank()
    display.wait_key()

    _second_night(display, state)
    _hilde_plea(display, state)
    _search_decision(display, state)
    _act1_ending(display, state)


def _second_night(display, state):
    state.current_time = "Nacht"
    display.clear()
    display.blank()
    display.narration("Zweite Nacht in Hollowmere.")
    display.pause(2)

    tier = state.get_mental_tier()

    if tier in ("stable", "tense"):
        display.narration("Du liegst wach. Hoerst. Wartest.")
        display.pause(1.5)
        display.narration("Nichts. Keine Schreie. Nur Stille.")
        display.pause(1)
        display.narration("Das ist fast schlimmer.")
    else:
        display.narration("Du liegst wach. Dein Herz schlaegt zu schnell.")
        display.pause(1)
        display.horror("Im Flur -- Schritte? Nein. Nur das Haus, das arbeitet.")
        display.pause(1)
        display.horror("Oder?")
        state.modify_mental_state(-2)

    display.pause(1)
    display.blank()
    display.narration("Irgendwann schlaefst du ein.")
    display.pause(1)

    # Dream sequence
    display.blank()
    display.separator()
    display.narration("Du traeumst.")
    display.pause(1.5)

    if state.trauma == "loss":
        display.narration("Von einem Gesicht. Vertraut. Geliebt.")
        display.narration("Es loest sich auf wie Nebel.")
        display.horror("Und dahinter ist ein anderes Gesicht. Keines, das du kennst.")
        display.horror("Es laechelt.")
    elif state.trauma == "accident":
        display.narration("Von einer Strasse. Nass. Scheinwerferlicht.")
        display.horror("Das Geraeusch von Metall. Dann Stille.")
        display.horror("Jemand sagt deinen Namen. Aber die Stimme kommt von unter der Erde.")
    elif state.trauma == "memory":
        display.narration("Von einem dunklen Raum. Klein. Eng.")
        display.horror("Du bist ein Kind. Die Waende pulsieren.")
        display.horror("Jemand sagt: 'Nicht umdrehen.'")
    else:
        display.narration("Von nichts. Nur Schwarz.")
        display.pause(1)
        display.horror("Und in dem Schwarz: ein Fluestern.")
        display.horror("'Warum weigerst du dich zu erinnern?'")

    display.pause(2)
    display.separator()
    display.blank()
    display.narration("Du wachst auf. Es ist Morgen.")
    display.pause(1)
    state.modify_mental_state(-3)
    display.blank()
    display.wait_key()


def _hilde_plea(display, state):
    state.current_time = "Morgen"
    state.day += 1
    display.clear()
    display.status_bar(state)
    display.blank()
    display.narration(f"Tag {state.day}. Morgen.")
    display.pause(1)

    display.narration("Laerm im Gastraum. Eine Frau. Ende 50. Aufgeloest.")
    display.narration("Sie redet auf Maren ein. Maren haelt ihre Haende und sagt leise Dinge.")
    display.pause(1.5)

    display.dialogue("Hilde", "Drei Tage! Drei Tage ist er jetzt weg! "
                     "Karl wuerde nie --", Fore.LIGHTYELLOW_EX)
    display.dialogue("Maren", "Hilde. Setz dich. Atme.", Fore.LIGHTYELLOW_EX)
    display.pause(1)

    display.blank()
    display.narration("Maren sieht dich. Ihr Blick sagt: Bitte nicht einmischen.")
    display.pause(1)

    display.narration("Hilde dreht sich um. Sieht dich. Neue Hoffnung in ihren Augen.")
    display.pause(0.5)

    display.dialogue("Hilde", f"Sie! Sie sind fremd hier. Sie sind nicht... "
                     "Sie gehoeren nicht dazu.", Fore.LIGHTYELLOW_EX)
    display.narration("Das klingt nicht wie eine Beleidigung. Es klingt wie ein Kompliment.")
    display.pause(0.5)
    display.dialogue("Hilde", "Mein Mann. Karl Rieger. Er ist seit drei Tagen verschwunden. "
                     "Niemand sucht nach ihm. NIEMAND.",
                     Fore.LIGHTYELLOW_EX)
    display.pause(0.5)
    display.dialogue("Hilde", "Die Buergermeisterin sagt, er sei 'Bergwandern'. "
                     "Karl HASST die Berge.", Fore.LIGHTYELLOW_EX)
    display.pause(1)

    display.blank()
    display.narration("Maren schuettelt leise den Kopf. Fast unsichtbar.")
    display.pause(0.5)

    state.add_notebook("Karl Rieger: Seit 3 Tagen vermisst. Frau Hilde ist verzweifelt. "
                       "Buergermeisterin sagt 'Bergwandern'. Niemand sucht.")
    display.show_notebook_entry("Karl Rieger: Seit 3 Tagen vermisst. Frau Hilde ist verzweifelt. "
                                "Niemand sucht.")


def _search_decision(display, state):
    """The central decision of Act 1."""
    display.blank()
    display.separator("═")
    display.type_text("  ENTSCHEIDUNG", Fore.RED, display.SLOW)
    display.separator("═")
    display.blank()

    ch = display.choice([
        ("\"Ich helfe Ihnen suchen, Frau Rieger.\"", None),
        ("\"Ich werde mich umhoeren. Aber leise. Ohne Aufsehen.\"", None),
        ("\"Das ist eine Sache fuer die Gemeinde. Nicht fuer mich.\"", None),
        ("[Empathie 4+] \"Hilde. Hoer auf zu suchen. Bitte.\"",
         lambda s: s.check("empathy", 4)),
    ], state)

    if ch == 0:
        state.set_flag("search_active")
        state.add_decision("search_active")
        _active_search(display, state)
    elif ch == 1:
        state.set_flag("search_secret")
        state.add_decision("search_secret")
        _secret_search(display, state)
    elif ch == 2:
        state.set_flag("search_refused")
        state.add_decision("search_refused")
        _refuse_search(display, state)
    elif ch == 3:
        state.set_flag("search_warned")
        state.add_decision("search_warned")
        _warn_hilde(display, state)


def _active_search(display, state):
    display.blank()
    display.dialogue("Hilde", "Danke. Oh Gott, danke.", Fore.LIGHTYELLOW_EX)
    display.narration("Sie greift deine Haende. Fest. Ihre Finger sind eiskalt.")
    display.pause(1)
    display.narration("Maren schaut weg.")
    state.modify_relationship("hilde", 20)
    state.modify_relationship("maren", -5)
    display.pause(1)

    display.blank()
    display.narration("Ihr sucht zusammen. Den ganzen Tag.")
    display.pause(1)

    display.blank()
    display.narration("Wohin zuerst?")
    display.blank()

    ch = display.choice([
        ("Zum Bergwerk.", None),
        ("Zum See.", None),
        ("Zu Karl und Hildes Haus.", None),
    ], state)

    if ch == 0:
        _search_mine(display, state)
    elif ch == 1:
        _search_lake(display, state)
    else:
        _search_house(display, state)

    display.blank()
    display.wait_key()


def _search_mine(display, state):
    display.clear()
    display.narration("Das Bergwerk. Noerdlich. Am Berghang.")
    display.narration("Die Eingaenge sind mit Brettern vernagelt. Ketten. Schloeser.")
    display.pause(1)

    display.narration("Aber an einem Eingang --")
    display.pause(0.5)
    display.narration("Das Schloss fehlt.")
    display.pause(1)
    display.narration("Und auf dem Boden, vor dem Eingang:")
    display.pause(0.5)

    display.horror("Eine Jacke. Braun. Abgetragen. Blutflecken am Aermel.")
    display.pause(1.5)

    display.dialogue("Hilde", "Das... das ist Karls Jacke.", Fore.LIGHTYELLOW_EX)
    display.narration("Ihre Stimme bricht.")
    display.pause(1)

    state.add_clue("karls_jacke")
    state.add_item("Karls Jacke")
    display.system_msg("  [Karls Jacke gefunden]")

    if state.check("perception", 4):
        display.blank()
        display.narration("Du siehst mehr. Frische Werkzeugspuren am Tueerrahmen. "
                          "Ein Stueck Seil.")
        display.narration("Jemand hat das Schloss nicht gebrochen. "
                          "Jemand hat es ENTFERNT. Mit dem richtigen Werkzeug.")
        state.add_clue("schloss_entfernt")
        state.add_notebook("Das Bergwerks-Schloss wurde professionell entfernt. "
                           "Das war kein Einbruch. Das war geplant.")
        display.show_notebook_entry("Das Bergwerks-Schloss wurde professionell entfernt. Geplant.")

    display.blank()
    ch = display.choice([
        ("Hineingehen.", None),
        ("Nicht heute. Wir brauchen Ausruestung.", None),
    ], state)

    if ch == 0:
        display.blank()
        display.narration("Der Eingang gaehnt. Dunkelheit.")
        display.pause(1)
        display.narration("Du machst einen Schritt hinein.")
        display.pause(1)
        display.narration("Kalte Luft. Nein -- warme Luft. Von innen. "
                          "Als wuerde das Bergwerk atmen.")
        display.pause(1.5)
        display.horror("Tief unten, im Dunkel, ein Gerausch. "
                       "Wie ein Herzschlag. Langsam. Gleichmaessig.")
        display.pause(1)
        display.dialogue("Hilde", "Karl? KARL?!", Fore.LIGHTYELLOW_EX)
        display.narration("Ihre Stimme hallt. Und hallt. Und hallt.")
        display.narration("Keine Antwort. Nur das Pochen.")
        state.modify_mental_state(-5)
        state.add_clue("bergwerk_herzschlag")
        state.add_notebook("Im Bergwerk: warme Luft und ein Gerausch wie ein Herzschlag. "
                           "Tief unten.")
        display.show_notebook_entry("Im Bergwerk: warme Luft und ein Gerausch wie ein Herzschlag.")
        display.blank()
        display.narration("Ihr geht zurueck. Hilde weint leise. "
                          "Du sagst nichts, weil es nichts zu sagen gibt.")
    else:
        display.blank()
        display.narration("Hilde will hineingehen. Du haeltst sie zurueck.")
        display.narration("Sie sieht dich an. Versteht. Nickt.")
        display.dialogue("Hilde", "Morgen. Mit Licht. Mit allem.", Fore.LIGHTYELLOW_EX)
        state.set_flag("bergwerk_zugang_geplant")

    state.add_notebook("Karls Jacke am Bergwerkseingang. Blutspuren. "
                       "Er ist dort hineingegangen. Oder gebracht worden.")
    state.modify_relationship("lena", -15)


def _search_lake(display, state):
    display.clear()
    display.narration("Der Stille See. 800 Meter Durchmesser. Das Wasser ist klar.")
    display.pause(1)
    display.narration("Zu klar. Man sieht den Grund -- Steine, Sand, Algen.")
    display.narration("Ausser in der Mitte. Dort ist das Wasser schwarz.")
    display.pause(1.5)

    display.narration("Am Ufer: eine Bank mit eingeritzten Initialen.")
    display.pause(0.5)

    if state.check("perception", 3):
        display.narration("Manche Initialen sind durchgestrichen. "
                          "Manche so tief ausgekratzt, dass das Holz gesplittert ist.")
        state.add_clue("bank_initialen")

    display.blank()
    display.narration("Nichts von Karl hier. Keine Spuren. Keine Jacke. Nichts.")
    display.pause(1)
    display.narration("Nur der See. Und die Stille.")
    display.pause(2)

    display.blank()
    display.narration("Beim Zurueckgehen --")
    display.pause(1)
    display.narration("Du drehst dich um. Zum See.")
    display.pause(1)

    display.horror("Fuer einen Moment -- einen einzigen Moment -- "
                   "siehst du ein Gesicht unter der Wasseroberflaeche.")
    display.pause(1)
    display.horror("Es schaut hoch. Mund offen. Augen weit.")
    display.pause(1)
    display.narration("Du blinzelst.")
    display.narration("Nur Wasser. Klar. Still.")
    display.pause(1)

    state.modify_mental_state(-5)
    state.add_clue("gesicht_im_see")
    state.add_notebook("Am See: Fuer einen Moment ein Gesicht unter Wasser. "
                       "Einbildung? Oder nicht?")
    display.show_notebook_entry("Am See: Ein Gesicht unter Wasser. Nur fuer einen Moment.")


def _search_house(display, state):
    display.clear()
    display.narration("Karl und Hildes Haus. Ein kleines Bauernhaus am Ortsrand.")
    display.pause(1)
    display.narration("Hilde zeigt dir Karls Sachen. Alles da. "
                      "Schuhe, Jacke (eine zweite), Werkzeug.")
    display.narration("Alles, was ein Mann mitnehmen wuerde, wenn er wandern geht.")
    display.pause(1)
    display.dialogue("Hilde", "Sehen Sie? Er hat nichts mitgenommen. "
                     "Wer geht wandern ohne Schuhe?", Fore.LIGHTYELLOW_EX)
    display.pause(1)

    display.blank()
    if state.check("perception", 3):
        display.narration("Am Kuechentisch: zwei Tassen. Kaffee, kalt. "
                          "Eine halb getrunken, eine unberuehrt.")
        display.narration("Zwei Stuehle. Einer zurueckgeschoben. "
                          "Der andere umgefallen.")
        display.pause(1)
        display.thought("Jemand war hier. Jemand, den Karl nicht erwartet hat. "
                        "Oder jemand, vor dem er aufgesprungen ist.")
        state.add_clue("zwei_tassen")
        state.add_notebook("Bei Riegers: Zwei Kaffeetassen, ein umgefallener Stuhl. "
                           "Karl hatte Besuch. Es ging schnell.")
        display.show_notebook_entry("Zwei Kaffeetassen, ein umgefallener Stuhl. "
                                    "Karl hatte Besuch.")

    if state.check("intellect", 4):
        display.blank()
        display.narration("Im Flur: ein Kalender. Der letzte Eintrag, drei Tage alt:")
        display.narration("'Rathaus. 20 Uhr.'")
        display.pause(1)
        display.thought("Karl war am Abend seines Verschwindens im Rathaus.")
        state.add_clue("karl_rathaus")
        state.add_notebook("Karl hatte am Abend seines Verschwindens einen Termin im Rathaus.")


def _secret_search(display, state):
    display.blank()
    display.dialogue("Hilde", "Umhoeren? Was soll das heissen?", Fore.LIGHTYELLOW_EX)
    display.narration("Enttaeuschung, aber nicht Verachtung.")
    display.pause(0.5)

    display.narration("Du verbringst den Tag unauffaellig. Hoerst zu. Beobachtest.")
    display.pause(1)

    display.blank()
    display.narration("Am Kraemerladen hoerst du Ernst mit jemandem fluestern.")
    display.narration("Er sagt: 'Der neue Gast stellt Fragen. Sei vorsichtig.'")
    display.pause(1)
    display.narration("An wen er das sagt, siehst du nicht.")

    state.add_clue("ernst_warnung")
    state.add_notebook("Ernst warnt jemanden vor mir. Wer? Und warum?")
    display.show_notebook_entry("Ernst warnt jemanden vor mir. Wer? Und warum?")
    state.modify_relationship("hilde", 5)
    display.blank()
    display.wait_key()


def _refuse_search(display, state):
    display.blank()
    display.narration("Hilde starrt dich an. Dann: Verachtung.")
    display.dialogue("Hilde", "Natuerlich. Wie alle anderen.", Fore.LIGHTYELLOW_EX)
    display.narration("Sie geht. Tuer knallt.")
    display.pause(1)

    display.blank()
    display.dialogue("Maren", "Das war... das Richtige.",
                     Fore.LIGHTYELLOW_EX)
    display.narration("Maren sagt es, als muesste sie sich selbst ueberzeugen.")
    display.pause(1)

    state.modify_relationship("hilde", -30)
    state.modify_relationship("maren", 5)
    state.modify_relationship("lena", 10)
    state.modify_guilt(5)

    display.blank()
    display.narration("Zwei Tage spaeter wird Karl 'gefunden'. "
                      "Herzinfarkt im Wald. Fall geschlossen.")
    display.narration("Hilde sagt kein Wort bei der Beerdigung.")
    display.pause(1)

    display.horror("Drei Tage danach verschwindet Hilde.")
    display.narration("Niemand sucht nach ihr.")
    display.pause(2)

    state.set_flag("hilde_verschwunden")
    state.modify_mental_state(-8)
    state.modify_guilt(10)
    state.add_notebook("Karl: offiziell Herzinfarkt. Hilde: verschwunden. "
                       "Niemand sucht. Niemand fragt.")
    display.show_notebook_entry("Karl: offiziell Herzinfarkt. Hilde: verschwunden. Niemand fragt.")
    display.blank()
    display.wait_key()


def _warn_hilde(display, state):
    display.blank()
    display.narration("Du siehst Hilde an. Direkt.")
    print(f"  {Fore.YELLOW}{state.player_name}:{Style.RESET_ALL} ", end="")
    display.type_text("\"Hilde. Hoer auf zu suchen. Bitte.\"", speed=display.NORMAL)
    display.pause(1)

    display.narration("Hilde erstarrt.")
    display.dialogue("Hilde", "Was... was wissen Sie?", Fore.LIGHTYELLOW_EX)
    display.pause(1)

    ch = display.choice([
        ("\"Ich weiss nichts. Aber ich fuehle, dass es gefaehrlich ist.\"", None),
        ("Schweigen.", None),
    ], state)

    if ch == 0:
        display.blank()
        display.narration("Hilde schaut dich an. Lange. Ihre Augen fuellen sich mit Traenen.")
        display.dialogue("Hilde", "Sie haben Recht. Ich weiss es. "
                         "Ich... ich wollte es nur nicht glauben.", Fore.LIGHTYELLOW_EX)
        display.pause(1)
        display.narration("Sie geht. Langsam. Gebrochen.")
        display.narration("Aber sie lebt. Sie hoert auf zu suchen.")
        state.modify_relationship("hilde", 15)
        state.set_flag("hilde_gewarnt")
        state.add_notebook("Hilde hat aufgehoert zu suchen. Sie lebt. "
                           "Aber der Preis war ihre Hoffnung.")
    else:
        display.blank()
        display.narration("Stille. Hilde wartet. Du sagst nichts.")
        display.pause(2)
        display.dialogue("Hilde", "Dann sind Sie wie alle anderen.",
                         Fore.LIGHTYELLOW_EX)
        display.narration("Sie geht. Sucht weiter.")
        display.pause(1)
        display.horror("In der naechsten Nacht verschwindet Hilde Rieger.")
        state.set_flag("hilde_verschwunden")
        state.modify_mental_state(-10)
        state.modify_guilt(15)
        state.add_notebook("Hilde ist verschwunden. Ich haette etwas sagen koennen. "
                           "Ich habe geschwiegen.")

    display.blank()
    display.wait_key()


def _act1_ending(display, state):
    state.advance_time()
    display.clear()
    display.blank()

    display.separator("═")
    display.blank()
    display.narration("Du sitzt am Fenster deines Zimmers. Es ist Nacht.")
    display.pause(1.5)
    display.narration("Draussen: Stille. Die Sorte Stille, die drueckt.")
    display.pause(1)

    display.blank()
    if state.has_flag("search_active"):
        display.narration("Du hast Dinge gesehen, die du nicht erklaeren kannst.")
        display.narration("Blut an einer Jacke. Einen Herzschlag im Dunkel.")
    elif state.has_flag("search_refused") or state.has_flag("ignored_screams"):
        display.narration("Du hast weggeschaut. Und der Ort hat es bemerkt.")
        display.narration("Die Leute laecheln dich an. Mehr als vorher. Als Belohnung.")
    else:
        display.narration("Irgendetwas stimmt hier nicht. Du weisst es. "
                          "Du kannst es nicht benennen.")

    display.pause(2)
    display.blank()
    display.narration("Der Ort ist wie ein Laecheln, das zu lang anhaelt.")
    display.narration("Wie ein Bild, das zu perfekt ist.")
    display.narration("Wie eine Antwort, die schon bereitlag, bevor du gefragt hast.")
    display.pause(2)

    display.blank()
    display.thought("Was verbergen sie?")
    display.pause(1)
    display.thought("Und warum fuehlt es sich an, als wuesste der Ort, "
                    "dass ich es wissen will?")
    display.pause(2)

    # Status display
    display.blank()
    display.status_bar(state)
    display.blank()

    display.separator("═")
    print(f"  {Fore.RED}{Style.BRIGHT}ENDE VON AKT 1, KAPITEL 3{Style.RESET_ALL}")
    display.separator("═")
    display.blank()

    # Summary
    display.system_msg("  Zusammenfassung deiner Entscheidungen:")
    display.blank()
    if state.has_flag("search_active"):
        display.system_msg("  - Du hast aktiv nach Karl gesucht")
    elif state.has_flag("search_secret"):
        display.system_msg("  - Du hast heimlich ermittelt")
    elif state.has_flag("search_refused"):
        display.system_msg("  - Du hast dich geweigert zu helfen")
    elif state.has_flag("search_warned"):
        display.system_msg("  - Du hast Hilde gewarnt")

    if state.has_flag("investigated_forest"):
        display.system_msg("  - Du hast den Wald untersucht")
    elif state.has_flag("investigated_town"):
        display.system_msg("  - Du hast den Ort beobachtet")
    elif state.has_flag("ignored_screams"):
        display.system_msg("  - Du hast die Schreie ignoriert")

    clue_count = len(state.clues)
    display.system_msg(f"  - Hinweise gesammelt: {clue_count}")
    display.system_msg(f"  - Mental State: {state.mental_state}%")
    display.system_msg(f"  - Schuld: {state.guilt}")

    if state.has_flag("hilde_verschwunden"):
        display.blank()
        display.warning("  Hilde Rieger ist verschwunden.")

    display.blank()
    display.separator("═")
    display.blank()
    display.narration("Die Geschichte geht weiter...")
    display.narration("Akt 2 ist in Entwicklung.")
    display.blank()
    display.type_text("  Danke fuers Spielen.", Fore.RED, display.SLOW)
    display.blank()

    state.set_flag("act1_complete")
