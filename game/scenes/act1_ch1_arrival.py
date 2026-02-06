"""HOLLOWMERE - Act 1, Chapter 1: Ankommen"""
from colorama import Fore, Style


def run(display, state):
    display.clear()
    display.blank()
    display.separator("═")
    print(f"  {Fore.RED}{Style.BRIGHT}AKT 1: BODEN UNTER DEN FUESSEN{Style.RESET_ALL}")
    print(f"  {Fore.LIGHTBLACK_EX}Kapitel 1: Ankommen{Style.RESET_ALL}")
    display.separator("═")
    display.blank()
    display.wait_key()

    _arrival_scene(display, state)
    _gasthaus_scene(display, state)
    _explore_town(display, state)
    _evening_scene(display, state)


def _arrival_scene(display, state):
    display.clear()
    display.narration("Der Pickup holpert ueber eine Schotterstrasse.")
    display.pause(1)
    display.narration("Der Fahrer -- ein wortkarger Mann mit wettergegerbtem Gesicht -- hat seit "
                      "zwanzig Minuten kein Wort gesagt.")
    display.pause(1)
    display.narration("Vor dir taucht ein Tal auf. Huegel. Wald. Daecher zwischen den Baeumen.")
    display.pause(1.5)

    display.dialogue("Fahrer", "Hollowmere. Da waeren wir.")
    display.pause(0.5)

    if state.origin == "journalist":
        display.thought("Ein Ort, der auf keiner Karte steht. Perfekt fuer eine Geschichte.")
    elif state.origin == "relative":
        display.thought("Also hier. Hier hat er gelebt. Oder lebt er noch?")
    else:
        display.thought("Hauptsache ein Bett und ein Telefon.")

    display.pause(1)
    display.narration("Der Pickup haelt am Ortseingang. Ein Schild, verblasst: HOLLOWMERE. "
                      "Darunter, in kleinerer Schrift, unleserlich.")
    display.blank()

    if state.check("perception", 3):
        display.thought("Die kleinere Schrift... da stand mal etwas anderes. "
                        "Jemand hat es ueberstrichen.")
        state.add_clue("schild_ueberstrichen")
        state.add_notebook("Das Ortsschild wurde ueberstrichen. Was stand da vorher?")
        display.show_notebook_entry("Das Ortsschild wurde ueberstrichen. Was stand da vorher?")
    display.pause(0.5)

    display.dialogue("Fahrer", "Gasthaus is in der Mitte. Maren kuemmert sich um Sie.")
    display.pause(0.5)
    display.dialogue("Fahrer", "Und... bleiben Sie nicht zu lang.")
    display.pause(0.5)
    display.narration("Bevor du fragen kannst, faehrt er zurueck. Schneller als noetig.")
    display.pause(1.5)

    display.blank()
    display.narration("Du stehst allein am Ortseingang. Es ist spaeter Nachmittag. "
                      "Warmes Licht. Vogelgesang.")
    display.narration("Alles sieht friedlich aus.")
    display.pause(1)
    display.narration("Du gehst los.")
    display.blank()
    display.wait_key()


def _gasthaus_scene(display, state):
    display.clear()
    display.narration("Das Gasthaus 'Zum Anker' steht am Marktplatz. Ein altes Fachwerkhaus, "
                      "gut gepflegt. Blumen an den Fenstern.")
    display.pause(1)
    display.narration("In der Mitte des Platzes: ein Brunnen. Zugemauert. Grauer Zement "
                      "ueber altem Stein.")
    display.pause(1)

    if state.check("perception", 2):
        display.thought("Warum mauert man einen Brunnen zu?")
        state.add_clue("brunnen_zugemauert")

    display.blank()
    display.narration("Du betrittst das Gasthaus. Holzwaende, warmes Licht, der Geruch "
                      "von Eintopf. Eine Frau steht hinter der Theke.")
    display.pause(1)

    display.blank()
    display.dialogue("Maren", "Oh! Ein Gast!", Fore.LIGHTYELLOW_EX)
    display.pause(0.3)
    display.narration("Sie laechelt. Breit. Warm. Ihre Augen brauchen eine Sekunde laenger.")
    display.pause(1)

    display.dialogue("Maren", f"Willkommen in Hollowmere. Ich bin Maren. "
                     "Sie muessen hungrig sein nach der Fahrt.", Fore.LIGHTYELLOW_EX)

    display.blank()
    ch = display.choice([
        (f"\"Danke. {state.player_name}. Haetten Sie ein Zimmer frei?\"", None),
        ("\"Wie viele Gaeste haben Sie normalerweise?\"",
         lambda s: s.check("perception", 3)),
        ("\"Der Fahrer sagte, ich soll nicht zu lang bleiben. Warum?\"", None),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Maren", "Natuerlich! Zimmer drei, oben rechts. "
                         "Frisch bezogen.", Fore.LIGHTYELLOW_EX)
        display.narration("Sie greift unter die Theke. Ein Schluessel. Kein Gaestebuch.")
        if state.check("perception", 3):
            display.thought("Kein Gaestebuch. Oder sie hat es weggeraeumt, bevor ich kam.")
        state.modify_relationship("maren", 5)

    elif ch == 1:
        display.blank()
        display.dialogue("Maren", "Wir sind ein kleiner Ort. Nicht viele kommen hierher.",
                         Fore.LIGHTYELLOW_EX)
        display.narration("Ihr Laecheln bleibt. Aber die Haende hinter der Theke sind "
                          "fuer einen Moment still.")
        display.dialogue("Maren", "Umso schoener, dass Sie da sind!", Fore.LIGHTYELLOW_EX)
        state.add_notebook("Maren weicht der Frage nach Gaesten aus.")
        display.show_notebook_entry("Maren weicht der Frage nach Gaesten aus.")

    elif ch == 2:
        display.blank()
        display.narration("Marens Laecheln flackert. Nur fuer einen Moment.")
        display.dialogue("Maren", "Ach, der alte Gerhard. Redet immer so. "
                         "Meint nichts Boeses.", Fore.LIGHTYELLOW_EX)
        display.pause(0.5)
        display.dialogue("Maren", "Bleiben Sie so lang Sie wollen. Wirklich.",
                         Fore.LIGHTYELLOW_EX)
        if state.check("empathy", 3):
            display.thought("Das 'wirklich' war zu betont. Sie uebt das.")
            state.add_notebook("Maren besteht darauf, dass ich bleiben soll. Zu nachdruecklich.")
        state.modify_relationship("maren", -3)

    display.blank()
    display.wait_key()

    # --- Room scene ---
    display.clear()
    display.narration("Dein Zimmer ist klein, aber sauber. Ein Bett, ein Stuhl, ein Nachttisch.")
    display.narration("Am Fenster haengen schwere Vorhaenge. Auf dem Nachttisch steht "
                      "ein Glas Wasser.")
    display.pause(1)
    display.narration("Du stellst deine Tasche ab. Setzt dich aufs Bett.")
    display.pause(1)

    if state.check("perception", 4):
        display.blank()
        display.narration("Etwas stimmt nicht.")
        display.pause(0.5)
        display.narration("Die Schublade des Nachttischs ist nicht ganz geschlossen. "
                          "Du ziehst sie auf.")
        display.pause(1)
        display.narration("Ein Zettel. Zerknittert. In krakeliger Handschrift:")
        display.pause(0.5)
        display.horror("  L A U F")
        display.pause(2)
        display.narration("Du drehst den Zettel um. Nichts.")
        state.add_clue("zettel_lauf")
        state.add_notebook("Ein Zettel in der Schublade: 'LAUF'. Wer hat das geschrieben?")
        state.add_item("Zerknitterter Zettel")
        display.show_notebook_entry("Ein Zettel in der Schublade: 'LAUF'. Wer hat das geschrieben?")
        state.modify_mental_state(-3)
    else:
        display.narration("Alles wirkt normal. Sauber. Gemuetlich.")
        display.narration("Du legst dich hin und ruhst dich aus.")

    display.blank()
    display.wait_key()


def _explore_town(display, state):
    display.clear()
    display.status_bar(state)
    display.blank()
    display.narration("Du gehst durch den Ort. Es ist spaeter Nachmittag. Die Sonne steht tief.")
    display.blank()
    display.narration("Hollowmere ist... huebsch. Wirklich. Alte Haeuser, Blumengaerten, "
                      "Kopfsteinpflaster.")
    display.narration("Wie aus einem Bilderbuch.")
    display.pause(1.5)

    display.blank()
    display.narration("Wohin gehst du zuerst?")
    display.blank()

    ch = display.choice([
        ("Zum Kraemerladen.", None),
        ("Zur Kirche.", None),
        ("Zurueck zum Brunnen.", None),
    ], state)

    if ch == 0:
        _kraemer_scene(display, state)
    elif ch == 1:
        _kirche_scene(display, state)
    else:
        _brunnen_scene(display, state)


def _kraemer_scene(display, state):
    display.clear()
    display.narration("Der Kraemerladen Hofer. Ein altmodisches Geschaeft mit allem, "
                      "was man braucht.")
    display.narration("Hinter der Theke: ein kleiner, duenner Mann mit Brille. "
                      "Nervoes. Haende immer in Bewegung.")
    display.pause(1)

    display.dialogue("Ernst", "Guten Tag, guten Tag! Der neue Gast, nicht wahr? "
                     "Man hoert ja so Dinge.", Fore.LIGHTGREEN_EX)

    display.blank()
    ch = display.choice([
        ("\"Man hoert Dinge? Was fuer Dinge?\"", None),
        ("\"Ja. Ich brauche ein paar Sachen. Batterien? Eine Taschenlampe?\"", None),
        ("\"Wie lange leben Sie schon hier, Herr Hofer?\"",
         lambda s: s.check("intellect", 3)),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Ernst", "Nichts, nichts! Kleiner Ort. "
                         "Man weiss eben, wenn jemand Neues da ist.", Fore.LIGHTGREEN_EX)
        display.narration("Er sortiert Dosen. Stellt sie gerade. Rueckt sie zurecht. "
                          "Dreht das Etikett nach vorn.")
        if state.check("perception", 3):
            display.thought("Er hat mich nicht gefragt, wie lange ich bleibe. "
                            "Wie lange ich bleibe, hat er nicht gefragt.")
            display.thought("Nein. Er hat mich nicht gefragt, weil er es schon weiss.")

    elif ch == 1:
        display.blank()
        display.dialogue("Ernst", "Taschenlampe? Natuerlich. Gute Wahl. Die Naechte sind "
                         "dunkel hier.", Fore.LIGHTGREEN_EX)
        display.narration("Er reicht dir eine Taschenlampe und Batterien. "
                          "Seine Hand zittert leicht.")
        state.add_item("Taschenlampe")
        display.system_msg("  [Taschenlampe erhalten]")

    elif ch == 2:
        display.blank()
        display.dialogue("Ernst", "Oh, schon... schon eine Weile.", Fore.LIGHTGREEN_EX)
        display.narration("Er wendet sich ab. Sortiert Regale.")
        display.dialogue("Ernst", "30 Jahre. Oder mehr. Man verliert "
                         "den Ueberblick.", Fore.LIGHTGREEN_EX)
        display.pause(0.5)
        if state.check("empathy", 3):
            display.thought("30 Jahre. Und doch klingt er wie jemand, der nie angekommen ist.")
            state.add_notebook("Ernst Hofer: Lebt seit ~30 Jahren hier. Wirkt nicht heimisch.")
            display.show_notebook_entry("Ernst Hofer: Lebt seit ~30 Jahren hier. Wirkt nicht heimisch.")

    display.blank()
    display.dialogue("Ernst", "Ach, und... seien Sie vorsichtig da draussen. "
                     "Nachts. Wenn Sie spazieren gehen.", Fore.LIGHTGREEN_EX)
    display.pause(0.5)
    display.dialogue("Ernst", "Die Wege sind uneben. Man stolpert leicht.",
                     Fore.LIGHTGREEN_EX)
    display.narration("Er laechelt. Es erreicht seine Augen nicht.")
    state.modify_relationship("ernst", 5)
    display.blank()
    display.wait_key()


def _kirche_scene(display, state):
    display.clear()
    display.narration("Die Kirche ist ueberraschend gross fuer einen Ort dieser Groesse. "
                      "Dunkles Holz. Hohe Fenster.")
    display.narration("Drinnen: kuehle Luft, der Geruch von Wachs. 300 leere Plaetze.")
    display.pause(1)
    display.narration("Vor dem Altar steht ein Mann in Schwarz. Hager. Muede Augen.")
    display.pause(1)

    display.dialogue("Brandt", "Ah. Ein neues Gesicht.", Fore.LIGHTCYAN_EX)
    display.narration("Er streckt die Hand aus. Sein Griff ist fest, aber die Finger sind kalt.")
    display.dialogue("Brandt", "Thomas Brandt. Pfarrer. Fuer das, was es wert ist.",
                     Fore.LIGHTCYAN_EX)
    display.pause(0.5)

    display.blank()
    ch = display.choice([
        ("\"Grosse Kirche fuer einen kleinen Ort.\"", None),
        ("\"Ist Hollowmere schon immer so... ruhig gewesen?\"",
         lambda s: s.check("empathy", 2)),
        ("\"Ich bin nicht religioes. Aber danke.\"", None),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Brandt", "Ja.", Fore.LIGHTCYAN_EX)
        display.pause(1)
        display.dialogue("Brandt", "Sie wurde gebaut, als der Ort groesser war. "
                         "Oder als der Glaube groesser war. Ich bin mir nicht sicher, "
                         "was zuerst geschrumpft ist.", Fore.LIGHTCYAN_EX)
        display.narration("Ein Anflug von Humor. Trocken. Wie Staub.")
        state.modify_relationship("brandt", 5)

    elif ch == 1:
        display.blank()
        display.dialogue("Brandt", "Ruhig...", Fore.LIGHTCYAN_EX)
        display.narration("Er schaut zum Fenster. Lange.")
        display.dialogue("Brandt", "Manche Naechte sind lauter als andere.",
                         Fore.LIGHTCYAN_EX)
        display.pause(1)
        display.dialogue("Brandt", "Aber das werden Sie selbst merken.",
                         Fore.LIGHTCYAN_EX)
        state.add_notebook("Pfarrer Brandt: 'Manche Naechte sind lauter als andere.'")
        display.show_notebook_entry("Pfarrer Brandt: 'Manche Naechte sind lauter als andere.'")
        state.modify_relationship("brandt", 3)

    elif ch == 2:
        display.blank()
        display.dialogue("Brandt", "Die wenigsten hier sind es.", Fore.LIGHTCYAN_EX)
        display.pause(0.5)
        display.dialogue("Brandt", "Mich eingeschlossen. Manchmal.", Fore.LIGHTCYAN_EX)
        display.narration("Er sagt es leise. Wie ein Gestaendnis, das ihm herausrutscht.")

    display.blank()
    display.wait_key()


def _brunnen_scene(display, state):
    display.clear()
    display.narration("Du stehst vor dem zugemauerten Brunnen. Grauer Zement auf altem Stein.")
    display.narration("Die Oberflaeche ist rau. Jemand hat das in Eile getan.")
    display.pause(1)

    display.narration("Auf einer Bank gegenueber sitzt eine alte Frau. "
                      "Sie starrt den Brunnen an. Reglos.")
    display.pause(1.5)

    display.blank()
    ch = display.choice([
        ("Die Frau ansprechen.", None),
        ("Den Brunnen untersuchen.", lambda s: s.check("perception", 3)),
        ("Weitergehen. Es ist nur ein alter Brunnen.", None),
    ], state)

    if ch == 0:
        display.blank()
        display.narration("Du setzt dich neben sie. Sie reagiert nicht.")
        display.pause(1)
        print(f"  {Fore.YELLOW}{state.player_name}:{Style.RESET_ALL} ", end="")
        display.type_text("\"Guten Tag. Wohnen Sie hier?\"", speed=display.NORMAL)
        display.pause(2)
        display.narration("Stille. Zehn Sekunden. Zwanzig.")
        display.pause(2)
        display.narration("Sie dreht den Kopf. Langsam. Laechelt.")
        display.pause(1)
        display.narration("Dann steht sie auf und geht. Ohne ein Wort.")
        display.pause(1)
        state.add_notebook("Eine alte Frau sitzt am Brunnen und starrt. Spricht nicht.")
        display.show_notebook_entry("Eine alte Frau sitzt am Brunnen und starrt. Spricht nicht.")
        state.set_flag("met_old_woman")

    elif ch == 1:
        display.blank()
        display.narration("Du legst die Hand auf den Zement. Kuehl. Rau.")
        display.pause(1)
        display.narration("Du klopfst. Einmal. Zweimal.")
        display.pause(1)
        display.narration("Hohl. Der Brunnen ist hohl.")
        display.pause(0.5)
        display.narration("Und da ist noch etwas. Ein Geruch. Suesslich. Wie verdorbene Blumen.")
        state.add_clue("brunnen_hohl")
        state.add_notebook("Der Brunnen ist hohl. Es riecht suesslich. Warum ist er zugemauert?")
        display.show_notebook_entry("Der Brunnen ist hohl. Es riecht suesslich. Warum ist er zugemauert?")
        state.modify_mental_state(-2)

    else:
        display.blank()
        display.narration("Du gehst weiter. Es ist nur ein Brunnen.")
        display.pause(1)
        display.narration("Nur ein alter, zugemauierter Brunnen in einem kleinen Ort.")
        display.pause(0.5)
        display.narration("Nichts Besonderes.")
        display.pause(1)
        if state.check("perception", 2):
            display.thought("Warum schaue ich immer noch zurueck?")

    display.blank()
    display.wait_key()


def _evening_scene(display, state):
    """Evening in the Gasthaus - meeting Lilly."""
    state.current_time = "Abend"
    display.clear()
    display.status_bar(state)
    display.blank()
    display.narration("Abend. Du sitzt im Gastraum. Eintopf und Brot. Es schmeckt gut.")
    display.narration("Besser als es sollte.")
    display.pause(1)

    display.blank()
    display.narration("In der Ecke sitzt ein Maedchen. Acht, vielleicht neun Jahre alt. "
                      "Sie malt mit Buntstiften.")
    display.pause(1)
    display.dialogue("Maren", "Das ist Lilly. Meine Tochter. "
                     "Lilly, sag Hallo.", Fore.LIGHTYELLOW_EX)
    display.pause(0.5)

    display.narration("Lilly schaut auf. Grosse Augen. Laechelt.")
    display.dialogue("Lilly", "Hallo.", Fore.LIGHTMAGENTA_EX)
    display.pause(0.5)
    display.narration("Sie schaut wieder auf ihr Bild.")
    display.pause(1)

    display.blank()
    ch = display.choice([
        ("Zu Lilly gehen und ihr Bild anschauen.", None),
        ("Mit Maren reden.", None),
        ("Essen. Schweigen. Ins Bett.", None),
    ], state)

    if ch == 0:
        _lilly_drawing(display, state)
    elif ch == 1:
        _maren_evening_talk(display, state)
    else:
        display.blank()
        display.narration("Du isst. Du schweigst. Du gehst ins Bett.")
        display.pause(1)
        display.narration("Manchmal ist Schweigen die sicherste Antwort.")
        state.add_decision("evening_silent")

    display.blank()
    state.set_flag("act1_ch1_complete")
    state.advance_time()  # -> Nacht
    display.wait_key()


def _lilly_drawing(display, state):
    display.blank()
    display.narration("Du gehst zu Lilly. Setzt dich neben sie.")
    display.narration("Sie malt ein Haus. Schwarz. Alle Fenster schwarz.")
    display.pause(1)
    display.narration("Vor dem Haus steht eine Figur. Zu gross. Zu duenn. "
                      "Keine Gesichtszuege.")
    display.pause(1.5)

    display.blank()
    ch = display.choice([
        ("\"Wer ist das vor dem Haus?\"", None),
        ("\"Schoenes Bild, Lilly.\"", None),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Lilly", "Das ist der Mann, der nachts kommt.",
                         Fore.LIGHTMAGENTA_EX)
        display.pause(2)

        display.dialogue("Maren", "Lilly, Zeit fuers Bett.",
                         Fore.LIGHTYELLOW_EX)
        display.narration("Schnell. Zu schnell.")
        display.pause(0.5)
        display.dialogue("Lilly", "Aber Mama --", Fore.LIGHTMAGENTA_EX)
        display.dialogue("Maren", "Jetzt.", Fore.LIGHTYELLOW_EX)
        display.pause(1)

        display.narration("Lilly nimmt das Bild. Geht nach oben. "
                          "Maren laechelt dich an.")
        display.pause(0.5)
        display.dialogue("Maren", "Kinder und ihre Fantasie.",
                         Fore.LIGHTYELLOW_EX)
        display.narration("Es ist das gleiche Laecheln wie vorher. Genau das gleiche.")

        state.add_clue("lilly_zeichnung")
        state.add_notebook("Lilly malt einen 'Mann, der nachts kommt'. "
                           "Maren hat Angst. Sie versteckt es.")
        display.show_notebook_entry("Lilly malt einen 'Mann, der nachts kommt'. "
                                    "Maren hat Angst. Sie versteckt es.")
        state.modify_mental_state(-2)
        state.modify_relationship("maren", -5)
        state.modify_relationship("lilly", 10)
        state.add_decision("asked_about_drawing")
    else:
        display.blank()
        display.dialogue("Lilly", "Danke! Das ist unser Haus.", Fore.LIGHTMAGENTA_EX)
        display.narration("Sie laechelt und malt weiter.")
        state.modify_relationship("lilly", 5)
        state.add_decision("complimented_drawing")


def _maren_evening_talk(display, state):
    display.blank()
    display.dialogue("Maren", "Noch ein Bier? Oder Tee? "
                     "Die Naechte werden kalt hier oben.", Fore.LIGHTYELLOW_EX)
    display.pause(0.5)

    ch = display.choice([
        ("\"Wie lange ist der Pass schon blockiert?\"", None),
        ("\"Leben Sie allein hier? Mit Lilly?\"",
         lambda s: s.check("empathy", 3)),
        ("\"Danke fuer alles. Gute Nacht.\"", None),
    ], state)

    if ch == 0:
        display.blank()
        display.dialogue("Maren", "Oh, der Erdrutsch? Drei Wochen etwa. Passiert manchmal. "
                         "Die Berge, wissen Sie.", Fore.LIGHTYELLOW_EX)
        display.pause(0.5)
        if state.check("perception", 4):
            display.thought("Drei Wochen. Sie hat nicht gezueckt. "
                            "Als waere eine blockierte Strasse normal.")
            state.add_notebook("Der Pass ist seit 3 Wochen blockiert. "
                               "Maren scheint das nicht zu stoeren.")

    elif ch == 1:
        display.blank()
        display.narration("Marens Haende halten inne. Nur fuer einen Moment.")
        display.dialogue("Maren", "Mein Mann... reist viel. Beruflich. "
                         "Seitdem ist es ruhiger.", Fore.LIGHTYELLOW_EX)
        display.pause(1)
        if state.check("empathy", 4):
            display.thought("Das war auswendig gelernt. Jedes Wort.")
            state.add_clue("maren_mann")
            state.add_notebook("Marens Mann 'reist viel'. Sie klingt, als wuerde sie "
                               "einen Text aufsagen.")
            display.show_notebook_entry("Marens Mann 'reist viel'. Sie klingt, als wuerde sie "
                                        "einen Text aufsagen.")
        state.modify_relationship("maren", 3)

    else:
        display.blank()
        display.dialogue("Maren", "Gute Nacht. Schlafen Sie gut.",
                         Fore.LIGHTYELLOW_EX)
        display.narration("Sie laechelt. Warm. Muetterlich.")
        display.pause(0.5)
        display.narration("Fast echt.")
        state.modify_relationship("maren", 5)
