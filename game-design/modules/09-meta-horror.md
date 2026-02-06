# Modul 09 -- Meta-Horror & Optionale Elemente

---

## Meta-Horror: Das Spiel weiss, dass du spielst

### Designphilosophie

Meta-Horror ist KEIN Gimmick. Es wird sparsam, gezielt und NUR an Stellen eingesetzt, an denen es die Immersion VERTIEFT statt sie zu brechen. Der Spieler soll sich fragen: "War das Absicht? Oder bilde ich mir das ein?" -- und nie eine klare Antwort bekommen.

---

### Implementierung

#### 1. Speicherdatei-Manipulation

**Was passiert:**
- Beim zweiten Durchlauf erkennt das Spiel, dass der Spieler schon einmal gespielt hat
- NPCs machen Andeutungen: "Kommen Sie mir bekannt vor?" (nur beim zweiten Durchlauf)
- Konrad sagt im zweiten Durchlauf: "Du warst schon hier. Ich erinnere mich. Aber beim letzten Mal... hast du es anders gemacht."

**Technisch:**
- Speicherdatei enthaelt eine unsichtbare Variable: `visits`
- Wird beim Starten eines NEUEN Spiels nicht zurueckgesetzt
- Auch nach Loeschen des Spielstands bleibt eine Datei: `hollowmere.rem` im Spielordner
- Wird DIESE Datei geloescht, erscheint beim naechsten Start: "Etwas fehlt. Aber wir erinnern uns trotzdem."

#### 2. Spielername ausserhalb des Spiels

**Was passiert:**
- In Akt 3, wenn Mental State < 30, fluestert die Praesenz den TATSAECHLICHEN Spielernamen -- nicht den Charakternamen
- Technisch: Das Spiel liest den Benutzernamen des Betriebssystems
- Wenn der Spieler z.B. "Thomas" heisst und sein Charakter "Alex": "...Thomas...warum nennst du dich Alex?..."

**Einschraenkung:**
- NUR bei Mental State < 30
- NUR einmal pro Durchlauf
- Kann in den Optionen DEAKTIVIERT werden (Respekt vor Grenzen)
- Wenn deaktiviert, sagt die Praesenz: "...du hast dich versteckt...das ist in Ordnung...wir finden dich trotzdem..."

#### 3. Uhrzeit-Reaktivitaet

**Was passiert:**
- Das Spiel reagiert auf die echte Uhrzeit des Systems
- Zwischen 2:00 und 4:00 Uhr nachts (Echtzeit):
  - Die Stimmung im Spiel ist ANDERS. Dunkler. Laenger Schatten
  - Ein NPC (zufaellig) sagt: "Solltest du nicht schlafen?"
  - Am See erscheint eine Reflexion, die sonst nicht da ist: ein Schreibtisch. Ein Bildschirm. DEIN Bildschirm
- Am 6. Oktober (Datum des Rituals von 1924):
  - Besonderes Event: Alle NPCs versammeln sich am Brunnen. Schweigend. Ohne Erklaerung
  - Wenn der Spieler an diesem Tag das Bergwerk betritt: Die Tuer in Ebene 3 ist offen. Keine Bedingungen

#### 4. Screenshot-Verweigerung

**Was passiert:**
- Bei bestimmten Szenen (3-4 im ganzen Spiel) zeigt das Spiel fuer einen einzelnen Frame ein anderes Bild
- Wenn der Spieler versucht, einen Screenshot zu machen, ist das Bild NORMAL
- Nur im Augenblick des Erlebens ist es FALSCH
- Szenen:
  - Spiegel im Gasthaus (anderes Gesicht)
  - See bei Nacht (Gestalt unter Wasser)
  - Lillys Zeichnung (die Zeichnung bewegt sich)
  - Der eigene Charakter im Menue (Augen sind geschlossen, obwohl sie offen sein sollten)

---

## Unzuverlaessiger Erzaehler

### Konzept

Das Spiel hat keinen externen Erzaehler. Alles wird durch den SPIELER wahrgenommen -- und der Spieler ist nicht zuverlaessig. Seine Wahrnehmung verzerrt sich mit sinkendem Mental State.

### Implementierung

#### Ebene 1: Textveraenderung

Fruehe Dialoge veraendern sich im Nachhinein. Wenn der Spieler das Notizbuch liest, sind Saetze ANDERS als er sie in Erinnerung hat.

**Beispiel:**

Original-Dialog (Akt 1):
> MAREN: "Willkommen in Hollowmere. Ich hoffe, Sie fuehlen sich wohl."

Notizbuch-Eintrag (Akt 2, MS 50):
> MAREN: "Willkommen in Hollowmere. Ich hoffe, Sie bleiben nicht lange."

Notizbuch-Eintrag (Akt 3, MS 30):
> MAREN: "Willkommen in Hollowmere. Wir haben auf Sie gewartet."

**Der Spieler kann NICHT pruefen, was wirklich gesagt wurde.** Es gibt keine Moeglichkeit, den Original-Dialog erneut zu lesen. Das Notizbuch IST die einzige Quelle -- und es luegt.

#### Ebene 2: Raeumliche Verzerrung

Raeume veraendern sich bei wiederholtem Betreten:
- Das Gastzimmer hat beim ersten Besuch 1 Fenster. Beim dritten: 2. Niemand kommentiert es
- Der Kraemerladen hat ein Regal, das bei jedem Besuch an einer anderen Wand steht
- Der Weg zum Bergwerk wird laenger. Objektiv messbar (Schrittzaehler im Spiel)

#### Ebene 3: NPC-Inkonsistenz

NPCs widersprechen sich -- und der Spieler kann nicht feststellen, wer luegt:

> MAREN (Akt 1): "Mein Mann ist auf Geschaeftsreise."
> MAREN (Akt 2): "Mein Mann ist seit 3 Jahren weg."
> Wenn konfrontiert: "Das habe ich nie gesagt. Sie verwechseln mich mit jemand anderem."

War es Maren, die luegt? Oder der Spieler, der sich falsch erinnert? Das Spiel gibt keine Antwort.

#### Ebene 4: Falsche Erinnerungen

Das Spiel fuegt dem Notizbuch Eintraege hinzu, die auf Events basieren, die NIE stattgefunden haben:

> "Gespraech mit dem alten Mann am Brunnen. Er hat mir von den Lichtern im See erzaehlt."

Es gibt keinen alten Mann am Brunnen. Nur die alte Frau. Oder... gab es einen Mann? Und hat er es wirklich gesagt?

**Regel:** Falsche Erinnerungen treten nur auf bei MS < 50. Sie sind immer PLAUSIBEL -- nie offensichtlich falsch. Der Spieler soll zweifeln, nicht sicher sein.

---

## Erinnerungen, die sich aendern

### Konzept

Die Vergangenheit des Spielers -- das Trauma, das er zu Beginn gewaehlt hat -- ist nicht festgeschrieben. Sie veraendert sich im Laufe des Spiels.

### Implementierung

#### Das gewaehlte Trauma evoliert

**Verlust einer nahestehenden Person:**
- Akt 1: "Ich habe jemanden verloren."
- Akt 2: "Ich habe jemanden verloren. Es war meine Schuld."
- Akt 3: "Ich habe jemanden verloren. Ich habe sie verloren, weil ich HIER sein wollte."
- Akt 3 (MS < 30): "Habe ich wirklich jemanden verloren? Oder habe ich mir das gewuenscht?"

**Schuld an einem Unfall:**
- Akt 1: "Es war ein Unfall."
- Akt 2: "Es war ein Unfall. Aber ich haette es verhindern koennen."
- Akt 3: "Es war kein Unfall."
- Akt 3 (MS < 30): "Der Unfall hat nie stattgefunden. Hollowmere hat ihn erfunden. Fuer mich."

**Verdraengte Kindheitserinnerung:**
- Akt 1: "Da ist etwas, an das ich mich nicht erinnern will."
- Akt 2: "Ich erinnere mich an einen Ort. Dunkel. Warm. Unter der Erde."
- Akt 3: "Ich war schon einmal hier. Als Kind. Ich habe es verdraengt."
- Akt 3 (MS < 30): "Ich wurde hier GEBOREN. Nicht im menschlichen Sinn."

**Kein Trauma (Verweigerung):**
- Akt 1: "Ich bin in Ordnung."
- Akt 2: NPCs fragen: "Warum reden Sie nie ueber sich?"
- Akt 3: Die Praesenz: "...du hast dich so gut versteckt...sogar vor dir selbst..."
- Akt 3 (MS < 30): "Das Trauma bist DU. Du bist das Verdraengte von jemand anderem."

### Mechanik

- Innere Monologe am See oder in ruhigen Momenten reflektieren die aktuelle Version des Traumas
- Der Spieler kann NICHT die urspruengliche Version zurueckholen
- Das Notizbuch ueberschreibt alte Eintraege zur Vergangenheit
- Bei Gespraechen mit NPCs ueber die Vergangenheit: Der Charakter erzaehlt automatisch die AKTUELLE Version -- auch wenn der Spieler sich an die alte erinnert

---

## Vibe-Boost: Spezial-Events

### "Der leere Raum"

**Trigger:** Spieler steht 60 Sekunden still (keine Eingabe).
**Was passiert:** Der Charakter dreht den Kopf. Langsam. Schaut direkt in die Kamera. 3 Sekunden. Dann weiter wie normal.
**Wenn der Spieler es erneut versucht:** Nichts. Es passiert nie zweimal.

### "Die andere Melodie"

**Trigger:** Spieler hoert die Hintergrundmusik im Gasthaus 5 Mal.
**Was passiert:** Beim 6. Mal ist eine Note anders. Beim 7. Mal eine weitere. Beim 10. Mal ist es ein voellig anderes Lied. Maren summt mit. "Das Lied hat sich schon immer so angehoert."

### "Der Besucher"

**Trigger:** Spieler oeffnet das Spielmenue.
**Was passiert (einmalig, MS < 40):** Im Hintergrund des Menues -- hinter dem Optionen-Bildschirm -- steht eine Figur. Sie war vorher nicht da. Wenn der Spieler das Menue schliesst und wieder oeffnet: weg.

### "Das Inventar luegt"

**Trigger:** Spieler hat mehr als 10 Gegenstaende.
**Was passiert (MS < 50):** Ein Gegenstand im Inventar, den der Spieler NICHT aufgehoben hat. Beschreibung: "Du hast das mitgebracht. Erinnerst du dich nicht?" Wenn untersucht: "Es fuehlt sich vertraut an. Wie etwas, das du immer hattest." Es hat keine Funktion. Es verschwindet nach 2 Ingame-Tagen. Ohne Kommentar.

### "Die Benachrichtigung"

**Trigger:** Spieler pausiert das Spiel fuer mehr als 10 Minuten.
**Was passiert:** Beim Fortsetzen: Ein neuer Notizbuch-Eintrag. "Du warst weg. Wir haben auf dich gewartet." Kein NPC hat es geschrieben. Das Spiel hat es nicht angekuendigt. Es ist einfach DA.

---

## Grenzen des Meta-Horrors

### Was wir NICHT tun:

1. **Keine echten Dateien manipulieren** -- Keine Desktop-Aenderungen, keine Ordner erstellen, keine echten Systemdateien beruehren. Alles bleibt im Spielordner.
2. **Keine echten persoenlichen Daten lesen** -- Nur den Benutzernamen. Keine Fotos, Emails, Dokumente, Browserverlauf. Nie.
3. **Keine Deinstallations-Tricks** -- Das Spiel laesst sich normal deinstallieren. Immer.
4. **Keine Angst vor dem Ausschalten** -- Der Spieler muss jederzeit das Gefuehl haben, das Spiel STOPPEN zu koennen. Die Kontrolle gehoert dem Spieler. Immer.
5. **Kein Jump-Scare-Audio** -- Niemals laute ploetzliche Geraeusche. Auch nicht meta.
6. **Optionen respektieren** -- Jedes Meta-Element kann in den Optionen EINZELN deaktiviert werden:
   - [x] Systemname verwenden
   - [x] Uhrzeitbasierte Events
   - [x] Speicherdatei-Persistenz
   - [x] Meta-Notizbuch-Eintraege

### Warum diese Grenzen?

Weil Meta-Horror nur funktioniert, wenn der Spieler VERTRAUT, dass das Spiel ihn respektiert. Der Moment, in dem der Spieler das Gefuehl hat, das Spiel sei uebergriffig, ist der Moment, in dem die Immersion stirbt. Horror braucht einen sicheren Rahmen, um wirken zu koennen.

---

## Zusammenfassung: Die Erfahrung

HOLLOWMERE soll nicht "ein gutes Spiel" sein. Es soll eine Erfahrung sein, die bleibt. Die nachwirkt. Die den Spieler dazu bringt, um 3 Uhr nachts auf dem Sofa zu sitzen und sich zu fragen:

- "Habe ich das Richtige getan?"
- "War das wirklich, was da stand?"
- "Warum habe ich mich so entschieden?"
- "Was waere passiert, wenn..."

Und dann, ganz leise, im Hinterkopf:
- "Woher wusste es meinen Namen?"
