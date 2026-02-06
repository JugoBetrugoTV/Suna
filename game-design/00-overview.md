# HOLLOWMERE -- Game Design Document

## Horror Story-RPG | 2D Pixel Art | Top-Down

---

## Konzept

**HOLLOWMERE** ist ein storygetriebenes Horror-RPG in 2D-Pixel-Art. Der Spieler erwacht in der abgelegenen Gemeinde Hollowmere -- einem Ort, der auf keiner Karte verzeichnet ist und den niemand freiwillig verlassen hat. Die Optik erinnert an Stardew Valley: warme, detaillierte Pixel-Art. Aber unter der Oberflaeche fault alles.

Es gibt keine Helden. Keine Monster, die man erschlaegt. Keine einfachen Antworten. Nur Menschen, die etwas verbergen -- und ein Spieler, der entscheiden muss, wie weit er geht, um die Wahrheit zu finden.

---

## Genre-DNA

| Einfluss | Was wir uebernehmen |
|---|---|
| The Witcher 3 | Moralische Grauzonen, verzoegerte Konsequenzen, Begleiter mit eigenen Agenden |
| KOTOR / Starfield | Dialogbaeume mit Skillchecks, Fraktionsloyalitaet, Rufsystem |
| Silent Hill 2 | Psychologischer Horror, Schuld als Mechanik, verzerrte Realitaet |
| Until Dawn | Schmetterlingseffekt, Beziehungen bestimmen Ueberleben |
| Disco Elysium | Attribute als Persoenlichkeit, innerer Monolog, Gedanken-System |

---

## Saeulen des Designs

### 1. Story ueber alles
Kampf existiert, aber er ist selten, haesslich und hat Konsequenzen. Die meisten Konflikte werden durch Worte, Schweigen oder Flucht geloest.

### 2. Entscheidungen mit Gewicht
Keine Entscheidung ist kosmetisch. Jede Wahl veraendert mindestens einen Pfad. Manche Konsequenzen zeigen sich erst Stunden spaeter.

### 3. Kein klares Gut oder Boese
Jeder NPC hat Gruende fuer sein Handeln. Der Spieler wird gezwungen, zwischen schlechten Optionen zu waehlen.

### 4. Horror durch Subtraktion
Weniger ist mehr. Horror entsteht durch das, was man NICHT sieht, NICHT weiss, NICHT kontrollieren kann.

### 5. Der Spieler als Unreliable Narrator
Die Wahrnehmung des Spielers ist nicht objektiv. Mentale Stabilitaet veraendert, was man sieht, hoert und glaubt.

---

## Technische Eckdaten

- **Engine:** Godot 4 (empfohlen) oder RPG Maker mit Custom Scripts
- **Perspektive:** Top-Down, 16x16 oder 32x32 Tiles
- **Aufloesung:** 320x180 nativ, hochskaliert
- **Audio:** Ambient-Design mit dynamischem Layering basierend auf Mental State
- **Spielzeit:** 12-18 Stunden (erster Durchlauf), 8+ Enden
- **Speichersystem:** Manuell + Autosave an Wendepunkten (kein Save-Scumming-Design)

---

## Modul-Uebersicht

| Modul | Datei | Inhalt |
|---|---|---|
| Welt & Setting | `modules/01-world-and-setting.md` | Hollowmere, Geschichte, Orte, Atmosphaere |
| Hauptstory | `modules/02-main-story.md` | 3 Akte, Wendepunkte, Storylines |
| Horror-Mystery | `modules/03-horror-mystery.md` | Zentrale Mystery, Hinweise, Wahrheit |
| NPCs & Begleiter | `modules/04-npcs-and-companions.md` | Alle wichtigen Charaktere |
| RPG-Systeme | `modules/05-rpg-systems.md` | Attribute, Dialog, Mentale Stabilitaet |
| Entscheidungsbaeume | `modules/06-decision-trees.md` | Verzweigungen mit Konsequenzen |
| Beispiel-Dialoge | `modules/07-example-dialogues.md` | Ausgearbeitete Szenen |
| Enden | `modules/08-endings.md` | Alle Enden mit Bedingungen |
| Meta-Horror | `modules/09-meta-horror.md` | Optionale vierte Wand, unzuverlaessiger Erzaehler |
