# Modul 02 -- Hauptstory (3 Akte)

---

## Prolog: Ankunft

Der Spieler definiert seinen Charakter:

**Name:** Frei waehlbar
**Herkunft:** Drei Optionen, die spaetere Dialogoptionen und NPC-Reaktionen beeinflussen:

| Herkunft | Effekt |
|---|---|
| **Journalist/in** | +Wahrnehmung, +Verstand. Zugang zu Recherche-Dialogen. NPCs misstrauen dir ("Wieder so einer, der Geschichten sucht") |
| **Verwandt mit jemandem aus Hollowmere** | +Empathie. NPCs oeffnen sich leichter, aber erwarten Loyalitaet. Du hast persoenliche Stakes |
| **Zufall / Autopanne** | Keine Boni, aber maximale Freiheit. NPCs sind neugierig, nicht feindlich. Du bist ein unbeschriebenes Blatt |

**Vergangenheit (optionales Detail):**
Der Spieler kann ein Trauma waehlen, das spaeter relevant wird:
- Verlust einer nahestehenden Person
- Schuld an einem Unfall
- Verdraengte Erinnerung an die Kindheit
- Keines (Spieler verweigert die Angabe -- dies wird AUCH zur Mechanik: "Warum willst du nicht darueber reden?")

---

## AKT 1: "BODEN UNTER DEN FUESSEN"

### Kapitel 1.1 -- Ankommen

Der Spieler erreicht Hollowmere. Der Pass ist blockiert, aber ein Einheimischer hat ihn/sie mit einem Pickup mitgenommen. Das Gasthaus "Zum Anker" ist der erste sichere Ort.

**Stimmung:** Trügerische Normalitaet. Der Ort ist huebsch. Die Leute sind freundlich -- auf die Art, wie Kleinstadtmenschen freundlich sind. Neugierig, aber nicht aufdringlich. Es gibt warmes Essen und ein sauberes Bett.

**Gameplay:**
- Erkundung des Ortskerns
- Erste Gespraeche mit Schluessel-NPCs (Maren, Ernst, Pfarrer Brandt)
- Kleine Gefaelligkeiten erledigen (Side-Quest-Einfuehrung)
- Atmosphaere aufbauen: Alles wirkt normal

**Erste Unstimmigkeiten (subtil):**
- Ernst Hofer fragt, wie lange man bleibt -- und wirkt erleichtert, wenn man "nur ein paar Tage" sagt
- Im Gasthaus-Zimmer steht ein Glas Wasser auf dem Nachttisch. Morgens ist es leer. Der Spieler hat nicht daraus getrunken
- Am Marktplatz steht eine Frau und starrt den zugemauerten Brunnen an. Spricht man sie an, laechelt sie und geht weg. Spricht man sie nicht an, steht sie am naechsten Tag wieder da

### Kapitel 1.2 -- Risse

**Trigger-Event:** In der zweiten Nacht hoert der Spieler Schreie. Aus dem Wald. Laengere Schreie, dann Stille.

Am naechsten Morgen tut jeder so, als waere nichts passiert. Fragt man danach, reagieren NPCs unterschiedlich:

| NPC | Reaktion |
|---|---|
| Maren Voss | "Fuechse. Die schreien manchmal so." (Luege -- Wahrnehmung 3+ erkennt ihr Zittern) |
| Ernst Hofer | "Ich schlafe tief. Hab nichts gehoert." (Luege -- er hat Augenringe) |
| Pfarrer Brandt | Lange Pause. "Manche Naechte sind lauter als andere." (Ausweichend, aber ehrlich) |
| Nina Althammer | "Nicht nachts in den Wald gehen. Bitte." (Aufrichtig. Angst in den Augen) |

**Gameplay:**
- Erste echte Entscheidung: Sucht der Spieler nach der Quelle der Schreie?
  - JA -> Wald erkunden, erster Kontakt mit dem Grauen Saum, Mental State -5
  - NEIN -> Bleibt im Ort, gewinnt Vertrauen der NPCs, verpasst fruehen Hinweis
- Einfuehrung des Mental-State-Systems (subtil, ohne UI-Element am Anfang)
- Beziehungsaufbau mit NPCs

### Kapitel 1.3 -- Der Vermisste

**Trigger-Event:** Der Bauer KARL RIEGER wird vermisst. Seine Frau HILDE kommt ins Gasthaus und bittet um Hilfe. Die Buergermeisterin sagt, er sei "wahrscheinlich zum Bergwandern" gegangen. Hilde sagt, Karl hasst die Berge.

**Zentrale Entscheidung Akt 1:**

```
Hilfst du bei der Suche?
  |
  +-- [JA, aktiv suchen]
  |     Verbuendete: Hilde, Nina
  |     Feinde: Buergermeisterin wird misstrauisch
  |     -> Findet Karls Jacke am Bergwerkseingang, Blutspuren
  |
  +-- [JA, aber heimlich]
  |     Keine Verbuendeten, keine Feinde
  |     -> Findet weniger, aber niemand beobachtet dich
  |
  +-- [NEIN, nicht mein Problem]
  |     Verbuendete: Buergermeisterin (du bist "vernuenftig")
  |     Feinde: Hilde verachtet dich
  |     -> Karl wird "gefunden" -- angeblich Herzinfarkt im Wald
  |     -> Der Spieler verpasst den Bergwerks-Hinweis
  |
  +-- [NEIN, aber sage Hilde, sie soll aufhoeren zu suchen]
        (Empathie 4+ oder Gewaltbereitschaft 3+)
        -> Hilde bricht zusammen ODER Hilde wird wuetend
        -> In beiden Faellen: Sie verschwindet in der naechsten Nacht
```

**AKT 1 ENDE:**
Der Spieler hat den Ort kennengelernt, erste Beziehungen aufgebaut und merkt: Hier stimmt etwas nicht. Aber er kann noch nicht benennen, WAS. Das Unbehagen ist diffus, wie ein Geruch, den man nicht zuordnen kann.

---

## AKT 2: "DER BODEN WIRD DUENNER"

### Kapitel 2.1 -- Geheimnisse an der Oberflaeche

Der Pass ist immer noch blockiert. Oder wurde er blockiert? Ein Spieler mit Wahrnehmung 4+ bemerkt, dass die Felsen zu gleichmaessig liegen fuer einen natuerlichen Erdrutsch.

**Neue Orte oeffnen sich:**
- Das Bergwerk (Ebene 1 und 2)
- Tieferer Wald
- Das alte Rathaus (mit dem richtigen Ansatz)

**Sidequest-Netz:**
Jeder NPC hat ein Geheimnis, und die Sidequests drehen sich darum, diese zu enthuellen:

| NPC | Geheimnis | Sidequest |
|---|---|---|
| Maren Voss | Ihr Mann ist nicht "auf Reisen" -- er ist im Bergwerk verschwunden | "Marens Schweigen" -- finde Hinweise auf ihren Mann |
| Ernst Hofer | Er erhaelt Briefe von aussen. Er ist ein Informant | "Der Haendler und die Post" -- fange einen Brief ab oder gewinne sein Vertrauen |
| Pfarrer Brandt | Er hat die fehlenden Kirchenbuchseiten | "Die leeren Seiten" -- ueberzeuge ihn oder stiehl sie |
| Nina Althammer | Ihr Grossvater weiss die Wahrheit, aber sein Verstand ist unklar | "Fieberwort" -- pflege Konrad, gewinne Ninas Vertrauen, hoere zu |
| Buergermeisterin Karl | Sie organisiert das Schweigen. Sie glaubt, es sei zum Schutz | "Die Last der Verantwortung" -- konfrontiere oder verbuende dich |

**Spieler-Agency:**
Der Spieler entscheidet, WEM er nachgeht. Man kann nicht alle Sidequests in einem Durchlauf abschliessen. Manche schliessen sich gegenseitig aus. Wer Maren hilft, veraergert die Buergermeisterin. Wer Ernst verraet, verliert den Zugang zu Informationen von aussen.

### Kapitel 2.2 -- Das Ritual

**Trigger-Event:** Der Spieler findet (je nach Pfad) einen Hinweis auf ein Ritual, das 1924 im Bergwerk stattfand. Die Details variieren:

- **Kirchenbuch-Pfad:** 17 Namen. Alle am selben Tag gestorben. Todesursache: "Gotteswille"
- **Bergwerk-Pfad:** Symbole an den Waenden. Ein Kreis aus Steinen. Knochen
- **Konrad-Pfad:** Er fluestert: "Wir haben sie eingeladen. Und sie sind geblieben"
- **Brief-Pfad (Ernst):** Jemand von aussen recherchiert. Hollowmere ist nicht der einzige Ort

Egal welcher Pfad: Der Spieler erfaehrt, dass 1924 etwas gerufen wurde. Etwas, das nie gegangen ist.

### Kapitel 2.3 -- Vertrauensbruch

**Zentrales Event Akt 2:** Einer der NPCs, dem der Spieler vertraut, luegt ihn an. Welcher NPC es ist, haengt davon ab, wem der Spieler am naechsten steht (hoechster Beziehungswert).

Das System waehlt automatisch den engsten Verbuendeten als Verraeter. Der Schmerz soll maximal sein.

**Moegliche Szenarien:**
- Maren hat dem Spieler Schlafmittel ins Essen gemischt (im Auftrag der Buergermeisterin)
- Nina hat Informationen zurueckgehalten, die den Spieler in Gefahr bringen
- Pfarrer Brandt hat eine Warnung nicht weitergegeben
- Ernst hat den Spieler an die Buergermeisterin verraten

**Reaktion des Spielers (Entscheidungsbaum):**

```
Dein engster Verbuendeter hat dich verraten.
  |
  +-- [Konfrontation, wuetend]
  |     Beziehung bricht. NPC wird feindlich oder verzweifelt
  |     -> Zugang zu ihren Informationen verloren
  |     -> Aber: Ehrlichkeit kann spaeter belohnt werden
  |
  +-- [Konfrontation, ruhig]
  |     (Empathie 4+ ODER Willenskraft 5+)
  |     NPC erklaert sich. Beziehung beschaedigt, nicht zerstoert
  |     -> Reduzierter Zugang, aber NPC bleibt Verbuendeter
  |
  +-- [Schweigen. Nichts sagen.]
  |     NPC bemerkt, dass du es weisst. Paranoia steigt
  |     -> NPC wird unberechenbar in Akt 3
  |
  +-- [Luege: "Ich weiss von nichts"]
        (Manipulation-Check)
        NPC glaubt dir -- oder auch nicht
        -> Wenn erfolgreich: Du behaeltst Zugang, aber DEIN Charakter verliert Integritaet
        -> Mental State -10 ("Du wirst wie sie")
```

**AKT 2 ENDE:**
Der Spieler weiss jetzt: Es gibt etwas unter Hollowmere. Etwas, das die Bewohner schuetzen -- oder anbeten -- oder fuerchten. Die Fassade ist gebrochen. Aber die Wahrheit ist noch nicht klar. Und der Spieler muss sich fragen: Bin ich hier, um die Wahrheit zu finden? Oder bin ich hier, weil ICH gerufen wurde?

---

## AKT 3: "KEIN BODEN MEHR"

### Kapitel 3.1 -- Die Wahrheit in Fragmenten

Alle Faeden laufen zusammen. Der Spieler muss in Ebene 3 des Bergwerks vordringen. Die Stahltuer oeffnet sich nur unter bestimmten Bedingungen (abhaengig von gesammeltem Wissen und Beziehungen).

**Bedingungen fuer die Tuer (mindestens 2 von 4 erforderlich):**
1. Die Symbole aus dem Kirchenbuch (Pfad: Brandt)
2. Den Schluessel aus dem Rathaus-Archiv (Pfad: Buergermeisterin)
3. Konrads letzte Worte (Pfad: Nina -- Konrad stirbt in Akt 3)
4. Die Anleitung aus Ernsts Briefen (Pfad: Ernst)

### Kapitel 3.2 -- Unter der Erde

Hinter der Tuer liegt eine Hoehle, die nicht natuerlich ist. Die Waende pulsieren. Die Luft ist warm. Es riecht nach Erde und nach etwas Suesserem.

In der Mitte der Hoehle: ein Riss. Nicht im Boden. In der Realitaet.

Hier erfaehrt der Spieler die Wahrheit (in Fragmenten, je nach gesammeltem Wissen):

**Die vollstaendige Wahrheit:**
1924 fuehrten Bergleute ein Ritual durch -- nicht aus Boesartigkeit, sondern aus Verzweiflung. Die Mine war leer, der Ort am Verhungern. Sie folgten Anweisungen aus einem Buch, das in den tieferen Stollen gefunden wurde. Das Ritual oeffnete den Riss. Etwas kam hindurch. Nicht ein Monster. Etwas Abstraktes. Eine Praesenz, die sich von Schuldgefuehlen, Angst und Geheimnissen ernaehrt.

Die Praesenz haelt Hollowmere am Leben -- buchstaeblich. Der Ort ist unnaturlich fruchtbar. Niemand wird krank. Kinder werden alt. Aber der Preis: Alle paar Jahre verschwindet jemand. Die Praesenz "braucht" jemanden. Die Gemeinschaft waehlt -- inoffiziell, unausgesprochen, durch kollektives Wegschauen.

Karl Rieger war der letzte.

### Kapitel 3.3 -- Die letzte Entscheidung

Der Riss kann geschlossen werden. Aber:
- Das wuerde Hollowmere seiner Lebensgrundlage berauben. Der Ort wuerde sterben
- Die Menschen, die verschwunden sind, wuerden nicht zurueckkommen
- Die Praesenz wehrt sich nicht. Sie bittet. Sie zeigt dem Spieler, was Hollowmere ohne sie waere: Hunger, Krankheit, Tod

ODER:

Der Riss kann offen bleiben. Aber:
- Jemand muss als naechstes gehen
- Die Praesenz will DICH. Du bist voller Schuld, Angst, Geheimnisse
- Du koenntest jemand anderen waehlen
- Du koenntest dich selbst opfern

ODER:

Es gibt einen dritten Weg -- aber nur, wenn der Spieler genug Wissen gesammelt, genug Beziehungen aufgebaut und einen bestimmten Mental State hat (siehe Modul 08: Enden).

---

## Story-Themes

### Das Opfer der Gemeinschaft
Wie weit geht eine Gemeinschaft, um zu ueberleben? Ist kollektives Wegschauen dasselbe wie Mord?

### Schuld als Waehrung
Jeder in Hollowmere traegt Schuld. Die Praesenz ernaehrt sich davon. Je mehr Schuld der Spieler ansammelt, desto staerker wird sie -- und desto mehr Macht hat der Spieler ueber sie.

### Die Frage nach dem Recht
Hat der Spieler das RECHT, ueber das Schicksal eines Ortes zu entscheiden? Er ist ein Fremder. Diese Menschen leben hier seit Generationen. Wer gibt ihm die Autoritaet?

### Wahrheit vs. Frieden
Manche Wahrheiten zerstoeren mehr, als sie heilen. Waere Hollowmere besser dran, wenn niemand fragen wuerde?
