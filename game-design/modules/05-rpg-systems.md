# Modul 05 -- RPG-Systeme

---

## Design-Grundsatz

Attribute sind KEINE Kampfwerte. Sie sind Persoenlichkeitsmerkmale. Sie definieren, WER der Spieler ist, nicht wie stark er zuschlaegt. Jeder Wert oeffnet oder schliesst Tueren -- im Dialog, in der Story, in der Wahrnehmung der Welt.

---

## Attribute

### Die fuenf Saeulen

| Attribut | Beschreibung | Was es beeinflusst |
|---|---|---|
| **WILLENSKRAFT** | Mentale Stabilitaet. Widerstand gegen Horror, Manipulation und Verzweiflung | Mental-State-Verlust, Widerstand gegen die Praesenz, Faehigkeit zur Konfrontation |
| **EMPATHIE** | Einfuehlungsvermoegen. Faehigkeit, Menschen zu lesen und emotionale Verbindungen aufzubauen | NPC-Beziehungen, Zugang zu emotionalen Dialogen, Erkennen von Luegen und Schmerz |
| **WAHRNEHMUNG** | Aufmerksamkeit. Bemerken von Details, Unstimmigkeiten, versteckten Hinweisen | Entdecken von Clues, Erkennen von Gefahren, Bemerken von Anomalien |
| **GEWALTBEREITSCHAFT** | Bereitschaft zur Eskalation. Nicht nur physisch -- auch verbal, emotional | Einschuechtungsoptionen, Kampf-Effizienz, aber auch: NPC-Reaktionen (Angst, Ablehnung) |
| **VERSTAND** | Analytisches Denken. Logik, Deduktion, Verknuepfung von Informationen | Hinweis-Verbindungen, historische Analyse, Widerstand gegen Manipulation |

### Startwerte

Der Spieler verteilt **15 Punkte** auf die 5 Attribute. Minimum: 1. Maximum: 5.

Beispiel-Builds:

**"Der Ermittler"**: Wahrnehmung 5, Verstand 4, Empathie 3, Willenskraft 2, Gewaltbereitschaft 1
-> Findet alles, versteht alles, aber bricht unter dem Druck zusammen.

**"Der Mitfuehlende"**: Empathie 5, Willenskraft 4, Wahrnehmung 3, Verstand 2, Gewaltbereitschaft 1
-> Tiefe Beziehungen, stabil, aber uebersieht logische Zusammenhaenge.

**"Der Hardliner"**: Gewaltbereitschaft 4, Willenskraft 4, Verstand 3, Wahrnehmung 3, Empathie 1
-> Robust und analytisch, aber niemand vertraut ihm. NPCs haben Angst.

**"Der Verdraenger"**: Willenskraft 5, Verstand 4, Wahrnehmung 3, Empathie 2, Gewaltbereitschaft 1
-> Psychisch stabil, aber emotional taub. Kann die Wahrheit ertragen, aber versteht nicht, warum andere leiden.

### Attribut-Entwicklung

Attribute steigen NICHT durch Erfahrungspunkte. Sie veraendern sich durch HANDLUNGEN:

| Aktion | Effekt |
|---|---|
| Eine Konfrontation durchstehen ohne wegzulaufen | Willenskraft +1 (einmalig pro Situation) |
| Einem NPC in einer Krise beistehen | Empathie +1 |
| Einen versteckten Hinweis finden | Wahrnehmung +1 (einmalig pro Hinweis-Typ) |
| Gewalt anwenden oder androhen | Gewaltbereitschaft +1 |
| Einen komplexen Zusammenhang erkennen | Verstand +1 |

**Maximum: 7** (durch Aktionen ueber den Startwert hinaus)

**ABER:** Jede Erhoehung hat einen Preis:
- Willenskraft +1 = Empathie -0.5 (man wird haerter, aber kaelter)
- Empathie +1 = Willenskraft -0.5 (man fuehlt mehr, aber ertraegt weniger)
- Gewaltbereitschaft +1 = Empathie -1 (Gewalt entfremdet)
- Wahrnehmung +1 = Mental State -3 (man sieht Dinge, die man nicht sehen will)

---

## Mental State System

### Uebersicht

Der Mental State (MS) ist der zentrale Horror-Mechanismus. Er reicht von 0 bis 100 und beeinflusst ALLES.

**Startwert:** 80 (leichtes Unbehagen, der Spieler ist schliesslich an einem fremden Ort)

### Wie der Mental State sinkt

| Ereignis | MS-Verlust |
|---|---|
| Horror-Event erleben | -3 bis -15 (je nach Schwere) |
| Einen NPC sterben sehen | -10 |
| Allein im Wald nachts | -2 pro Minute (Echtzeit) |
| Im Bergwerk (Ebene 2+) | -1 pro Minute |
| Luegen (bewusst) | -2 pro Luege |
| Jemanden opfern | -20 |
| Einen Verrat erleben | -8 |
| Die Wahrheit erfahren (Akt 3) | -15 |

### Wie der Mental State steigt

| Aktion | MS-Gewinn |
|---|---|
| Mit einem vertrauten NPC sprechen | +3 (max 1x pro Tag) |
| Im Gasthaus schlafen | +5 (nur wenn MS > 30) |
| Ein Raetsel loesen | +2 |
| Einem NPC helfen | +3 |
| Am See sitzen (bei Tag, MS > 50) | +2 |
| Die Wahrheit aussprechen | +5 (einmalig pro Gestaendnis) |

### Mental State Stufen und ihre Effekte

#### STABIL (MS 70-100)
- **Visuell:** Normale Grafik. Warme Farben. Klar.
- **Audio:** Normale Umgebungsgeraeusche. Musik, wenn vorhanden.
- **Dialog:** Alle Optionen verfuegbar. Klare Formulierungen.
- **Gameplay:** Standard. Notizbuch ist zuverlaessig. Karte funktioniert.

#### ANGESPANNT (MS 50-69)
- **Visuell:** Leicht entsaettigte Farben. Schatten sind laenger. Manchmal flackert eine Lichtquelle.
- **Audio:** Leises Hintergrund-Drone. Gelegentliches Knacken. Schritte, wenn niemand da ist.
- **Dialog:** Manche Optionen sind "unscharf" formuliert. Der Spieler ist sich nicht sicher, was er sagt.
  - Normal: "Ich glaube Ihnen nicht."
  - Angespannt: "Ich... bin nicht sicher, ob das stimmt."
- **Gameplay:** Notizbuch hat gelegentliche Tippfehler. Karte zeigt manchmal falsche Position.

#### INSTABIL (MS 30-49)
- **Visuell:** Deutlich dunkler. Farben verlieren Saettigung. Pixel-Glitch-Effekte am Bildrand. NPCs haben fuer einzelne Frames andere Sprites.
- **Audio:** Konstantes Summen. Stimmen im Hintergrundrauschen. Musik verzerrt sich.
- **Dialog:** Neue Optionen erscheinen, die "nicht vom Spieler" kommen:
  - "(Fluestern: Frag sie nach dem Brunnen)"
  - "[Du willst das nicht sagen. Oder?]"
  - Manche Optionen fehlen (Empathie-Optionen verschwinden zuerst)
- **Gameplay:** Notizbuch hat falsche Eintraege. Karte zeigt Orte, die nicht existieren. Raetsel-Loesungen verschieben sich.

#### GEBROCHEN (MS 10-29)
- **Visuell:** Fast monochrom. Starke Verzerrungen. NPCs bewegen sich abgehackt. Gesichter verschwimmen. Der Spieler-Sprite veraendert sich (dunkler, verzerrter).
- **Audio:** Dauerhaftes Rauschen. Weinen. Der Name des Spielers wird gefluestert.
- **Dialog:** Die Haelfte der Optionen fehlt. Neue, verstoerrende Optionen:
  - "(Schrei sie an. SCHREI.)"
  - "[Sag nichts. Sie verdienen dein Schweigen nicht.]"
  - "...ich bin so muede. Kann ich einfach... aufhoeren?"
- **Gameplay:** Notizbuch ist kaum lesbar. Karte dreht sich. Timer laufen schneller. Speichern ist unsicher (Autosave kann fehlerhafte Daten erzeugen -- kosmetischer Effekt, keine echte Datenbeschaedigung).

#### VERLOREN (MS 0-9)
- **Visuell:** Schwarz-weiss mit rotem Akzent. Welt ist ANDERS. Gebaeude haben andere Formen. NPCs sind Silhouetten.
- **Audio:** Stille. Absolute Stille. Dann: Ein einzelner Ton. Lang. Tief.
- **Dialog:** Eine einzige Option pro Gespraech. Der Spieler hat keine Wahl mehr.
- **Gameplay:** Linearer Pfad zu einem der "Gebrochenen Enden" (siehe Modul 08).

---

## Dialog-System

### Grundstruktur

Jeder Dialog bietet 2-5 Antwortmoeglichkeiten. Die Optionen sind nicht immer gleich -- sie haengen ab von:

1. **Attributen** (bestimmte Optionen erfordern Mindestwerte)
2. **Beziehungswert** (manche Optionen nur bei hohem/niedrigem Vertrauen)
3. **Wissen** (was der Spieler bereits weiss, oeffnet neue Optionen)
4. **Mental State** (veraendert Formulierungen und verfuegbare Optionen)
5. **Vorherigen Entscheidungen** (der Dialog merkt sich, was du gesagt hast)

### Dialog-Typen

#### Typ 1: STANDARD
Normales Gespraech. Informationsaustausch. 3-4 Optionen.

#### Typ 2: KONFLIKT
Eskalierte Situation. 4-5 Optionen, einige mit Attribut-Checks.
```
[Ehrlich] "Ich weiss, dass du luegst."
[Empathie 3+] "Du hast Angst. Ich verstehe das."
[Gewalt 3+] "Sag es mir. Jetzt."
[Verschwiegen] "..." (Schweigen als Druckmittel)
[Manipulativ, Verstand 4+] "Ernst hat mir schon alles erzaehlt." (Luege)
```

#### Typ 3: VERTRAUENSENTSCHEIDUNG
Intime Momente. 2-3 Optionen. Jede hat schwere Konsequenzen.
```
Nina: "Ich war dabei. Beim Rat. Ich habe nichts gesagt. Bin ich... schuldig?"

[Empathie 4+] "Du warst ein Kind, Nina. Du konntest nichts tun."
   -> Nina: Erleichterung. Vertrauen +15. ABER: Sie glaubt die Luege. Es aendert nichts.
[Ehrlich] "Schweigen war eine Entscheidung. Wie jede andere."
   -> Nina: Zusammenbruch. Vertrauen -10. ABER: Ehrlichkeit. Langfristig staerker.
[Ausweichend] "Das ist jetzt nicht wichtig."
   -> Nina: Enttaeuschung. Vertrauen -5. Das Gespraech ist vorbei.
```

#### Typ 4: UNTER DRUCK
Zeitlimit. 3-5 Sekunden fuer eine Antwort. Wenn keine Antwort: automatische Aktion (meist Schweigen oder Flucht).

#### Typ 5: INNERER MONOLOG
Kein Gespraech mit NPCs. Der Spieler redet mit sich selbst. Optionen sind Gedanken, die die innere Entwicklung beeinflussen.
```
[Du stehst vor dem Bergwerkseingang. Es ist dunkel.]

(Mut) "Ich muss da rein. Was immer da ist, ich muss es sehen."
(Vorsicht) "Nicht allein. Nicht heute."
(Verdraengung) "Es gibt nichts da drin. Das ist nur eine alte Mine."
(Akzeptanz, MS <50) "Es ruft mich. Ich weiss es. Und ich will antworten."
```

### Dialog-Konsequenzen

Jede Antwort hat mindestens EINE der folgenden Konsequenzen:

| Typ | Beschreibung |
|---|---|
| **Sofort** | NPC reagiert direkt. Beziehungswert veraendert sich |
| **Verzoegert** | Wirkung zeigt sich 1-3 Ingame-Tage spaeter |
| **Langzeit** | Beeinflusst Akt-Ende oder Spielende |
| **Intern** | Veraendert Mental State, Schuld-Zaehler oder innere Monologe |
| **Weltveraendernd** | Veraendert physisch etwas in der Welt (Tuer oeffnet sich, NPC verschwindet) |

---

## Schuld-System

### Konzept

Neben dem Mental State fuehrt das Spiel einen unsichtbaren SCHULD-Zaehler. Der Spieler sieht ihn NIE direkt. Aber er beeinflusst:

- Wie die Praesenz auf den Spieler reagiert
- Welche Visionen der Spieler hat
- Welches Ende erreichbar ist
- Wie NPCs den Spieler in Akt 3 behandeln

### Schuld steigt durch:
- Jemanden opfern oder opfern lassen (durch Untaetigkeit)
- Luegen mit schweren Konsequenzen
- NPCs manipulieren fuer eigenen Vorteil
- Die Wahrheit verdraengen
- Gewalt als erste Option waehlen

### Schuld sinkt durch:
- Gestaendnisse (gegenueber NPCs oder sich selbst)
- Opfer bringen (eigene Sicherheit fuer andere riskieren)
- Die Wahrheit aussprechen, auch wenn es wehtut
- Verantwortung uebernehmen

### Schuld-Schwellen

| Stufe | Schwelle | Effekt |
|---|---|---|
| Unschuldig | 0-10 | Praesenz ignoriert den Spieler weitgehend |
| Belastet | 11-30 | Praesenz beginnt, den Spieler wahrzunehmen. Subtile Effekte |
| Schuldig | 31-60 | Visionen. Stimmen. Die Praesenz "kennt" den Spieler |
| Verloren | 61-80 | Die Praesenz bietet dem Spieler einen Deal an |
| Verdammt | 81-100 | Die Praesenz WILL den Spieler. Bestimmte Enden werden zwingend |

---

## Kampf-System (minimal)

### Philosophie

Kampf ist SELTEN, HAESSLICH und hat KONSEQUENZEN. Es gibt kein XP fuer Kills. Es gibt Trauma.

### Wann kommt es zum Kampf?

- Wenn der Spieler in eine Falle geraet (Wald, Bergwerk)
- Wenn NPCs gewalttaetig werden (Eskalation)
- In der finalen Konfrontation (Akt 3, optional)

### Kampf-Mechanik

Echtzeit-Entscheidungen, KEIN rundenbasiertes System:

```
[SITUATION: Ein NPC blockiert den Weg. Er hat ein Messer.]

OPTIONEN (3 Sekunden):
-> [FLUCHT] Zurueck. Weg verloren. Aber sicher.
-> [REDEN] "Leg das Messer weg." (Empathie 4+ ODER Willenskraft 5+)
-> [ENTWAFFNEN] Riskant. Gewaltbereitschaft 3+. Erfolg: NPC am Boden. Misserfolg: Verletzung.
-> [GEWALT] Zuschlagen. Immer moeglich. Immer erfolgreich. Mental State -10. Schuld +15.
```

### Konsequenzen von Gewalt

- Jede Gewaltanwendung wird vom Spiel vermerkt
- NPCs, die von Gewalt erfahren, aendern ihr Verhalten
- Der Spieler-Sprite veraendert sich subtil (dunkler, eckiger)
- Manche Dialog-Optionen verschwinden permanent
- Die Praesenz wird staerker angezogen

---

## Zeitsystem

### Tagesablauf

Ein Ingame-Tag dauert ~30 Minuten Echtzeit:
- **Morgen** (6:00-12:00): NPCs sind aktiv, Laeden offen, sicher
- **Nachmittag** (12:00-18:00): Wie Morgen, aber manche NPCs ziehen sich zurueck
- **Abend** (18:00-22:00): Weniger NPCs draussen. Gasthaus voll. Geruechte werden getauscht
- **Nacht** (22:00-6:00): Gefaehrlich. Wald ist anders. Bergwerk zugaenglich. Horror-Events

### Zeit als Ressource

Der Spieler hat NICHT unendlich Zeit:
- Die Story schreitet voran, auch wenn der Spieler nichts tut
- NPCs treffen eigene Entscheidungen, wenn der Spieler zu lange wartet
- Hilde verschwindet nach 3 Tagen ohne Hilfe
- Konrad stirbt nach einer bestimmten Anzahl von Tagen
- Die Praesenz wird staerker, je mehr Tage vergehen

Es gibt keine Zeitanzeige im UI. Der Spieler muss nach dem Sonnenstand und NPC-Verhalten schaetzen.
