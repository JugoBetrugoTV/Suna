"""HOLLOWMERE - Act 1, Chapter 2: Risse"""
import time
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
    print(f"  {Fore.LIGHTBLACK_EX}Kapitel 2: Risse{Style.RESET_ALL}")
    display.separator("═")
    display.blank()
    display.wait_key()

    _night_screams(display, state)
    _morning_after(display, state)
    _investigation_choice(display, state)
    _nina_meeting(display, state)


def _night_screams(display, state):
    display.clear()
    display.blank()
    display.narration("Nacht.")
    display.pause(2)
    display.narration("Du liegst im Bett. Die Decke ist warm. Draussen: Stille.")
    display.pause(2)
    display.narration("Absolute Stille.")
    display.pause(2)
    display.narration("Keine Grillenzirpen. Kein Wind. Nichts.")
    display.pause(2)

    display.blank()
    display.narration("Dann --")
    display.pause(1.5)

    display.horror("Ein Schrei.")
    display.pause(1)
    display.horror("Aus dem Wald. Hoch. Lang. Menschlich.")
    display.pause(1.5)
    display.horror("Er bricht ab. Ploetzlich. Als haette jemand den Ton abgedreht.")
    display.pause(2)

    display.blank()
    display.narration("Stille. Wieder.")
    display.pause(2)
    display.narration("Dein Herz haemmert.")
    display.pause(1)

    # Check for water glass
    display.blank()
    display.narration("Du schaust zum Nachttisch. Das Glas Wasser.")
    display.pause(1)
    display.narration("Es ist leer.")
    display.pause(0.5)
    display.narration("Du hast nicht daraus getrunken.")
    display.pause(2)

    state.modify_mental_state(-5)
    state.add_clue("nachtschrei")
    state.add_notebook("Schreie in der Nacht. Aus dem Wald. Menschlich. "
                       "Das Wasserglas war leer -- ich habe nicht getrunken.")

    display.blank()
    ch = display.choice([
        ("Ans Fenster gehen und hinausschauen.", None),
        ("Die Decke ueber den Kopf ziehen. Nicht bewegen.", None),
        ("[Willenskraft 3+] Runtergehen und nachsehen.",
         lambda s: s.check("willpower", 3)),
    ], state)

    if ch == 0:
        display.blank()
        display.narration("Du gehst zum Fenster. Ziehst den Vorhang zurueck.")
        display.pause(1)
        display.narration("Der Marktplatz. Leer. Mondlicht auf Kopfsteinpflaster.")
        display.pause(1)
        display.narration("Am Waldrand -- eine Bewegung? Ein Schatten?")
        display.pause(1)
        display.narration("Nein. Nichts. Nur Baeume.")
        if state.check("perception", 4):
            display.pause(1)
            display.narration("Doch.")
            display.pause(0.5)
            display.narration("Da. Am Brunnen.")
            display.pause(1)
            display.horror("Die alte Frau. Sie steht da. Im Nachthemd. "
                           "Und sie schaut zu deinem Fenster.")
            display.pause(2)
            display.narration("Du blinzelst. Sie ist weg.")
            state.modify_mental_state(-3)
            state.add_clue("frau_am_brunnen_nachts")
        state.add_decision("looked_out_window")

    elif ch == 1:
        display.blank()
        display.narration("Du ziehst die Decke hoch. Atmest flach.")
        display.pause(1)
        display.narration("Minuten vergehen. Oder Stunden. Du weisst es nicht.")
        display.pause(1)
        display.narration("Irgendwann schlaefst du ein.")
        display.pause(1)
        display.narration("Du traeumst. Von einem Brunnen. Von Wasser, das nach oben faellt.")
        state.add_decision("hid_under_covers")

    elif ch == 2:
        display.blank()
        display.narration("Du stehst auf. Ziehst dich an. Gehst die Treppe hinunter.")
        display.pause(1)
        display.narration("Der Gastraum ist dunkel. Leer.")
        display.pause(0.5)
        display.narration("Nein. Nicht leer.")
        display.pause(1)
        display.narration("Maren sitzt an der Theke. Im Dunkeln. "
                          "Sie haelt ein Glas. Ihre Haende zittern.")
        display.pause(1)

        display.dialogue("Maren", "Gehen Sie wieder hoch.", Fore.LIGHTYELLOW_EX)
        display.narration("Keine Freundlichkeit. Keine Waerme. Ein Befehl.")
        display.pause(1)

        ch2 = display.choice([
            ("\"Ich habe Schreie gehoert.\"", None),
            ("[Empathie 4+] Schweigen. Neben sie setzen.",
             lambda s: s.check("empathy", 4)),
            ("Wieder hochgehen.", None),
        ], state)

        if ch2 == 0:
            display.blank()
            display.dialogue("Maren", "Fuechse. Die schreien manchmal so.",
                             Fore.LIGHTYELLOW_EX)
            if state.check("perception", 3):
                display.thought("Ihre Haende zittern. Das war kein Fuchs und sie weiss es.")
                state.add_notebook("Maren sagt: Fuechse. Maren luegt.")
            state.modify_relationship("maren", -3)

        elif ch2 == 1:
            display.blank()
            display.narration("Du setzt dich neben sie. Sagst nichts.")
            display.pause(2)
            display.narration("Minuten vergehen.")
            display.pause(1)
            display.dialogue("Maren", "...danke.", Fore.LIGHTYELLOW_EX)
            display.narration("Leise. Fast unhoerrbar.")
            display.pause(1)
            display.dialogue("Maren", "Gehen Sie jetzt schlafen. Bitte.",
                             Fore.LIGHTYELLOW_EX)
            state.modify_relationship("maren", 10)
            state.add_decision("comforted_maren_night")

        else:
            display.narration("Du gehst zurueck. Marens Blick folgt dir die Treppe hinauf.")

        state.add_decision("went_downstairs_night")

    display.blank()
    display.wait_key()


def _morning_after(display, state):
    state.current_time = "Morgen"
    state.day += 1
    display.clear()
    display.status_bar(state)
    display.blank()
    display.narration("Morgen. Tag 2.")
    display.pause(1)
    display.narration("Sonnenlicht. Vogelgesang. Der Geruch von Kaffee.")
    display.narration("Als waere letzte Nacht nie passiert.")
    display.pause(1.5)

    display.blank()
    display.narration("Im Gastraum fruehstuecken zwei Einheimische. "
                      "Maren wischt die Theke. Sie laechelt.")
    display.narration("Das gleiche Laecheln wie gestern. Millimetergenau.")
    display.pause(1)

    display.blank()
    display.narration("Du fragst nach den Schreien.")
    display.pause(1)

    display.separator()
    display.blank()

    display.dialogue("Maren", "Fuechse. Die schreien manchmal so.", Fore.LIGHTYELLOW_EX)
    if state.check("perception", 3):
        display.narration("Ihre Hand zittert. Kaum sichtbar.")
    display.blank()

    display.dialogue("Ernst", "Ich schlafe tief. Hab nichts gehoert.",
                     Fore.LIGHTGREEN_EX)
    display.narration("Er hat Augenringe. Tiefe.")
    display.blank()

    # Only Brandt gives a semi-honest answer
    display.dialogue("Brandt", "Manche Naechte sind lauter als andere.",
                     Fore.LIGHTCYAN_EX)
    display.narration("Er schaut dich an. Lange. Sagt nichts weiter.")
    display.blank()
    display.pause(1)

    state.add_notebook("Alle weichen den Fragen nach den Schreien aus. "
                       "Nur Brandt ist annaehernd ehrlich.")
    display.show_notebook_entry("Alle weichen den Fragen nach den Schreien aus. "
                                "Nur Brandt ist annaehernd ehrlich.")
    display.wait_key()


def _investigation_choice(display, state):
    """The player's first major decision: investigate or not."""
    display.clear()
    display.status_bar(state)
    display.blank()
    display.narration("Vor dem Gasthaus bleibst du stehen. Die Sonne scheint.")
    display.narration("Der Ort sieht aus wie eine Postkarte.")
    display.pause(1)

    display.blank()
    display.narration("Aber du hast die Schreie gehoert. Du weisst, "
                      "dass sie nicht von Fuechsen kamen.")
    display.pause(1)

    display.blank()
    display.separator()
    display.type_text("  Was tust du?", Fore.YELLOW, display.SLOW)
    display.separator()
    display.blank()

    ch = display.choice([
        ("Den Wald untersuchen. Herausfinden, woher die Schreie kamen.", None),
        ("Im Ort bleiben. Fragen stellen. Leute beobachten.", None),
        ("Nichts. Es geht mich nichts an. Ich warte auf den Pass.", None),
    ], state)

    if ch == 0:
        state.set_flag("investigated_forest")
        state.add_decision("investigated_forest")
        _forest_investigation(display, state)
    elif ch == 1:
        state.set_flag("investigated_town")
        state.add_decision("investigated_town")
        _town_investigation(display, state)
    else:
        state.set_flag("ignored_screams")
        state.add_decision("ignored_screams")
        _ignore_investigation(display, state)


def _forest_investigation(display, state):
    display.clear()
    display.narration("Du gehst zum Waldrand. Der 'Graue Saum', wie die Einheimischen ihn nennen.")
    display.pause(1)
    display.narration("Die Baeume stehen unnatuerlich gleichmaessig. Kein Unterholz. "
                      "Kein Vogelgesang.")
    display.narration("Der Boden ist weich. Federt unter deinen Schritten.")
    display.pause(1.5)

    display.blank()
    display.narration("Stille. Tiefe, drueckende Stille.")
    display.pause(1)

    display.narration("Du gehst tiefer. Zehn Minuten. Zwanzig.")
    display.pause(1)
    display.narration("Dann stoppst du.")
    display.pause(1)

    display.blank()
    display.horror("Du stehst am Waldrand. Dort, wo du losgelaufen bist.")
    display.pause(2)
    display.narration("Das ist nicht moeglich. Du bist geradeaus gegangen.")
    display.pause(1)

    state.modify_mental_state(-5)
    state.add_clue("wald_loop")

    display.blank()
    ch = display.choice([
        ("Noch einmal versuchen.", None),
        ("[Wahrnehmung 4+] Den Boden untersuchen.",
         lambda s: s.check("perception", 4)),
        ("Zurueckgehen. Das reicht.", None),
    ], state)

    if ch == 0:
        display.blank()
        display.narration("Du gehst wieder hinein. Laenger diesmal.")
        display.pause(1)
        display.narration("Und stehst wieder am Anfang.")
        display.pause(1)
        display.horror("Aber diesmal siehst du es: Fussspuren im weichen Boden.")
        display.horror("DEINE Fussspuren. Sie fuehren im Kreis.")
        display.pause(1)
        display.horror("Und daneben -- andere Spuren. Groesser. Tiefer. "
                       "Sie fuehren in den Wald hinein.")
        display.horror("Und sie kommen nicht zurueck.")
        state.modify_mental_state(-3)
        state.add_clue("fussspuren_wald")
        state.add_notebook("Der Wald fuehrt im Kreis. Meine Spuren drehen sich. "
                           "Aber andere Spuren fuehren nur REIN.")
        display.show_notebook_entry("Der Wald fuehrt im Kreis. Meine Spuren drehen sich. "
                                    "Aber andere Spuren fuehren nur REIN.")

    elif ch == 1:
        display.blank()
        display.narration("Du kniest dich hin. Der Boden...")
        display.pause(1)
        display.narration("Der Boden ist warm. Wie die Haut eines Tieres.")
        display.pause(1)
        display.narration("Und zwischen den Bleattern: etwas Rotes. Ein Stoffetzen.")
        display.pause(0.5)
        display.narration("Frisch. Noch feucht.")
        state.add_clue("stoff_wald")
        state.add_item("Roter Stofffetzen")
        display.system_msg("  [Roter Stofffetzen erhalten]")
        state.add_notebook("Ein frischer, roter Stofffetzen am Waldrand. Blut?")
        state.modify_mental_state(-2)

    else:
        display.blank()
        display.narration("Du gehst zurueck. Schnell. Ohne dich umzudrehen.")
        display.pause(1)
        display.narration("Erst am Ortsrand merkst du, dass du gerannt bist.")

    display.blank()
    display.wait_key()


def _town_investigation(display, state):
    display.clear()
    display.narration("Du bleibst im Ort. Beobachtest. Hoerst zu.")
    display.pause(1)

    display.narration("Am Marktplatz: Zwei Frauen reden. Sie verstummen, als du naeher kommst.")
    display.pause(1)
    display.narration("Am Kraemerladen: Ernst sortiert die gleichen Dosen wie gestern. "
                      "In der gleichen Reihenfolge.")
    display.pause(1)
    display.narration("An der Kirche: Brandt steht vor der Tuer. Schaut zum Wald. "
                      "Bewegt die Lippen. Betet.")
    display.pause(1.5)

    display.blank()
    if state.check("perception", 3):
        display.narration("Dann faellt dir etwas auf.")
        display.pause(1)
        display.narration("Kinder. Es gibt kaum Kinder im Ort. "
                          "Lilly -- und vielleicht ein oder zwei andere.")
        display.narration("Fuer einen Ort mit 200 Einwohnern ist das zu wenig.")
        state.add_clue("wenig_kinder")
        state.add_notebook("Kaum Kinder in Hollowmere. Seltsam fuer einen Ort dieser Groesse.")
        display.show_notebook_entry("Kaum Kinder in Hollowmere. Seltsam fuer einen Ort dieser Groesse.")

    if state.check("intellect", 3):
        display.blank()
        display.narration("Am Ortseingang: Das Schild. Du schaust es dir genauer an.")
        display.pause(1)
        display.narration("'Hollowmere' -- und darunter, ueberstrichen: "
                          "'Gruendung: 1689'.")
        display.narration("Seltsam. Warum ueberstreicht man das Gruendungsjahr?")
        state.add_clue("gruendungsjahr")
        state.add_notebook("Hollowmere: Gegründet 1689. Jemand hat das Datum ueberstrichen.")

    display.blank()
    display.narration("Du merkst: Dieser Ort ist wie eine Buehne. "
                      "Jeder spielt seine Rolle. Perfekt einstudiert.")
    display.narration("Aber heute -- nach den Schreien -- sind die Gesten einen Tick zu schnell. "
                      "Die Laecheln einen Ton zu hoch.")

    state.modify_relationship("maren", 3)
    state.modify_relationship("ernst", 3)
    display.blank()
    display.wait_key()


def _ignore_investigation(display, state):
    display.clear()
    display.narration("Du tust nichts. Es geht dich nichts an.")
    display.pause(1)
    display.narration("Du sitzt im Gasthaus. Trinkst Kaffee. Liest ein altes Buch aus dem Regal.")
    display.pause(1)
    display.narration("Der Tag vergeht. Ruhig. Normal.")
    display.pause(1.5)

    display.blank()
    display.narration("Gegen Abend klopft es an dein Zimmer.")
    display.pause(1)
    display.narration("Die Buergermeisterin. Korrekt gekleidet. Aufrechte Haltung.")
    display.pause(0.5)

    display.dialogue("Lena", f"Guten Abend. Lena Karl, Buergermeisterin. "
                     "Ich wollte mich persoenlich vorstellen.", Fore.LIGHTWHITE_EX)
    display.pause(0.5)
    display.dialogue("Lena", "Und mich erkundigen, ob es Ihnen an etwas fehlt.",
                     Fore.LIGHTWHITE_EX)
    display.pause(0.5)

    display.blank()
    ch = display.choice([
        ("\"Nein, danke. Alles bestens. Ich warte nur auf den Pass.\"", None),
        ("\"Letzte Nacht gab es Schreie im Wald.\"", None),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Lena", "Vernuenftig. Der Pass sollte bald frei sein.",
                         Fore.LIGHTWHITE_EX)
        display.narration("Sie laechelt. Nicht warm. Zufrieden.")
        state.modify_relationship("lena", 10)
        state.add_notebook("Buergermeisterin Lena Karl. Kontrolliert. "
                           "Zufrieden, dass ich nicht frage.")
    else:
        display.blank()
        display.dialogue("Lena", "Fuechse. Kommen im Herbst naeher an den Ort.",
                         Fore.LIGHTWHITE_EX)
        display.pause(0.5)
        display.narration("Die gleiche Antwort. Wort fuer Wort. "
                          "Als haetten alle den gleichen Text gelernt.")
        state.add_notebook("Die Buergermeisterin sagt dasselbe wie Maren. "
                           "Wort fuer Wort: 'Fuechse.'")
        state.modify_relationship("lena", -5)

    display.blank()
    display.wait_key()


def _nina_meeting(display, state):
    """Meeting Nina at the edge of town."""
    state.advance_time()  # -> Nachmittag or Abend
    display.clear()
    display.status_bar(state)
    display.blank()

    display.narration("Spaeter, auf dem Weg zurueck zum Gasthaus, triffst du sie.")
    display.pause(1)
    display.narration("Eine junge Frau. Mitte zwanzig. Sommersprossig. Muede. "
                      "Sie traegt einen Korb mit Lebensmitteln.")
    display.pause(1)
    display.narration("Sie bleibt stehen, als sie dich sieht. "
                      "Mustert dich. Nicht feindlich. Vorsichtig.")
    display.pause(1)

    display.dialogue("Nina", "Sie sind der Gast.", Fore.LIGHTBLUE_EX)
    display.narration("Keine Frage. Eine Feststellung.")
    display.pause(0.5)

    display.blank()
    ch = display.choice([
        (f"\"{state.player_name}. Und du?\"", None),
        ("\"Kennt hier jeder jeden?\"", None),
        ("[Empathie 3+] \"Du siehst muede aus.\"",
         lambda s: s.check("empathy", 3)),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Nina", "Nina. Althammer.", Fore.LIGHTBLUE_EX)
        display.narration("Kurz. Kein Laecheln. Aber auch keine Feindseligkeit.")
        display.dialogue("Nina", "Mein Grossvater lebt am Rand des Ortes. "
                         "Ich kuemmere mich um ihn.", Fore.LIGHTBLUE_EX)
        state.modify_relationship("nina", 5)

    elif ch == 1:
        display.blank()
        display.dialogue("Nina", "200 Menschen. Da kennt man Gesichter.",
                         Fore.LIGHTBLUE_EX)
        display.pause(0.5)
        display.dialogue("Nina", "Besonders neue.", Fore.LIGHTBLUE_EX)
        display.narration("Ein Anflug von Humor. Trocken. Vorsichtig.")
        state.modify_relationship("nina", 3)

    elif ch == 2:
        display.blank()
        display.narration("Sie blinzelt. Ueberrascht.")
        display.dialogue("Nina", "Mein Grossvater... er schlaeft schlecht. "
                         "Und wenn er nicht schlaeft, schlafe ich nicht.", Fore.LIGHTBLUE_EX)
        display.pause(0.5)
        display.dialogue("Nina", "Aber danke. Fuer die Ehrlichkeit.",
                         Fore.LIGHTBLUE_EX)
        display.narration("Ein halbes Laecheln. Das erste, das echt wirkt in diesem Ort.")
        state.modify_relationship("nina", 10)

    display.blank()
    display.narration("Sie will gehen. Dreht sich noch einmal um.")
    display.pause(1)
    display.dialogue("Nina", "Nicht nachts in den Wald gehen. Bitte.", Fore.LIGHTBLUE_EX)
    display.pause(0.5)
    display.narration("Ihre Augen. Da ist Angst. Echte Angst.")
    display.pause(1)
    display.narration("Dann geht sie.")

    state.add_notebook("Nina Althammer. Kuemmert sich um ihren Grossvater. "
                       "Hat Angst vor dem Wald. Aufrichtig.")
    display.show_notebook_entry("Nina Althammer. Kuemmert sich um ihren Grossvater. "
                                "Hat Angst vor dem Wald. Aufrichtig.")

    state.set_flag("met_nina")
    state.set_flag("act1_ch2_complete")
    display.blank()
    display.wait_key()
