# Modul 06 -- Entscheidungsbaeume

---

## Design-Grundsatz

Jeder Entscheidungsbaum folgt einer Regel: **Keine Option ist eindeutig richtig.** Der Spieler muss zwischen schlecht und schlechter waehlen -- oder zwischen gut fuer sich und gut fuer andere. Konsequenzen sind IMMER verzoegert, unerwartet oder beides.

---

## Entscheidungsbaum 1: "Der Brunnen"

**Zeitpunkt:** Akt 1, Kapitel 1.2
**Kontext:** Der Spieler entdeckt, dass der zugemauerte Brunnen hohl ist. Alte Frau am Brunnen sagt: "Er ist nicht leer."

```
ENTSCHEIDUNG: Was tust du mit dem Brunnen?

+-- [Ignorieren]
|     -> Kein Risiko. Kein Wissen.
|     -> In Akt 2 wird der Brunnen von jemand anderem geoeffnet.
|        Konsequenz: 2 NPCs sterben. Du haettest es verhindern koennen.
|
+-- [Buergermeisterin fragen]
|     -> Sie sagt: "Der Brunnen ist aus Sicherheitsgruenden zugemauert."
|     -> Wenn du insistierst (Willenskraft 3+):
|        Sie wird misstrauisch. Beziehung -10.
|     -> Wenn du akzeptierst:
|        Sie notiert dich als "kooperativ". Beziehung +5.
|
+-- [Nachts aufbrechen] (Wahrnehmung 3+ fuer Zugang)
|     |
|     +-- [Allein]
|     |     -> Du oeffnest den Brunnen. Darin: eine Leiter nach unten.
|     |     -> Du steigst hinab.
|     |     -> Unten: Ein Raum. Getrocknetes Blut. Symbole.
|     |     -> Und: Ein Name an der Wand. DEIN Name. (Falls "Verwandt"-Herkunft)
|     |     -> ODER: Der Name deines letzten Gastzimmer-Vorgaengers.
|     |     -> Mental State -8. Wichtiger Hinweis gewonnen.
|     |     -> ABER: Ernst hat dich gesehen. Er berichtet der Buergermeisterin.
|     |
|     +-- [Mit Nina] (Beziehung 40+)
|     |     -> Nina kennt die Symbole. "Grossvater hat davon gesprochen."
|     |     -> Mehr Kontext. Weniger Mental-State-Verlust (-4 statt -8).
|     |     -> ABER: Nina wird ab jetzt von der Buergermeisterin beobachtet.
|     |
|     +-- [Mit Maren] (Beziehung 50+)
|           -> Maren erkennt etwas am Boden: Dieters Ring.
|           -> Sie bricht zusammen. Beziehung +20 (geteiltes Leid).
|           -> ABER: Maren wird in Akt 2 unberechenbar. Sie will Rache.
|
+-- [Maren fragen, BEVOR du den Brunnen oeffnest]
      -> Maren sagt: "Lass den Brunnen zu. Bitte."
      -> Ihre Stimme zittert. Empathie 3+ erkennt: Sie weiss, was drin ist.
      -> Wenn du trotzdem oeffnest: Maren-Beziehung -15 ("Du haettest mir vertrauen sollen")
      -> Wenn du es laesst: Maren-Beziehung +10, aber Hinweis geht verloren
```

---

## Entscheidungsbaum 2: "Hildes Suche"

**Zeitpunkt:** Akt 1, Kapitel 1.3
**Kontext:** Hilde Rieger bittet um Hilfe bei der Suche nach ihrem Mann Karl.

```
HILDE: "Bitte. Er wuerde nie einfach weggehen. Ich kenne ihn seit 30 Jahren."

+-- [Aktiv suchen]
|     +-- Suche im Wald
|     |     -> Findet Fussspuren, die zum Bergwerk fuehren
|     |     -> Wird von Buergermeisterin konfrontiert: "Sie machen den Leuten Angst."
|     |     -> Buergermeisterin-Beziehung -15
|     |
|     +-- Suche am Bergwerk
|     |     -> Findet Karls Jacke. Blutspuren.
|     |     -> Wenn Wahrnehmung 4+: Auch ein Stueck Seil und frische Werkzeugspuren
|     |     -> Bergwerk-Zugang in Akt 2 erleichtert
|     |
|     +-- Suche am See
|           -> Nichts. Nur Stille.
|           -> ABER: Beim Zurueckgehen sieht der Spieler Karls Spiegelbild im Wasser.
|           -> Nur fuer eine Sekunde. Mental State -5.
|
+-- [Heimlich suchen]
|     -> Weniger Feinde, weniger Verbuendete
|     -> Findet weniger, aber bleibt unter dem Radar
|     -> Buergermeisterin bemerkt es trotzdem in Akt 2 (Ernst berichtet)
|
+-- [Ablehnen]
|     +-- [Ehrlich] "Es geht mich nichts an."
|     |     -> Hilde: Verachtung. Permanent feindlich.
|     |     -> ABER: Buergermeisterin sieht dich als Verbuendeten (+10)
|     |     -> Karl wird "gefunden" (Herzinfarkt-Story). Fall geschlossen.
|     |     -> Hilde verschwindet 3 Tage spaeter. Niemand sucht nach IHR.
|     |
|     +-- [Luege] "Ich bin sicher, er taucht auf."
|     |     -> Hilde: Hoffnung, dann Enttaeuschung. Beziehung: Neutral, dann negativ.
|     |     -> Schuld +5 (du hast ihr falsche Hoffnung gemacht)
|     |
|     +-- [Warnung, Empathie 4+] "Hilde. Hoer auf zu suchen. Bitte."
|           -> Hilde erstarrt. "Was weisst du?"
|           +-- [Wahrheit] "Ich weiss nichts. Aber ich fuehle, dass es gefaehrlich ist."
|           |     -> Hilde hoert auf. Ueberlebt. Wird spaeter zur Verbuendeten.
|           +-- [Schweigen]
|                 -> Hilde sucht allein. Verschwindet in der naechsten Nacht.
```

---

## Entscheidungsbaum 3: "Brandts Gestaendnis"

**Zeitpunkt:** Akt 2, Kapitel 2.1
**Kontext:** Pfarrer Brandt zeigt dem Spieler die fehlenden Kirchenbuchseiten (nur bei Vertrauen 70+).

```
BRANDT: "17 Namen. Alle am selben Tag. 6. Oktober 1924.
         Todesursache in jeder Zeile: 'Gotteswille.'
         Ich bete seit 30 Jahren fuer sie. Ich weiss nicht, ob jemand zuhoert."

ENTSCHEIDUNG: Wie reagierst du?

+-- [Empathie] "Das muss eine schwere Last sein."
|     -> Brandt weint. Beziehung +15.
|     -> Er gibt dir die Seiten (Kopie). Hinweis erhalten.
|     -> Aber: Er trinkt am Abend. Naechsten Tag ist er nicht ansprechbar.
|
+-- [Verstand 4+] "17 auf einmal. Das war kein Unfall. Was war das Ritual?"
|     -> Brandt: "Woher wissen Sie von einem Ritual?"
|     +-- [Ehrlich] "Ich habe Dinge gefunden. Im Bergwerk."
|     |     -> Brandt wird blass. Gibt dir MEHR als die Seiten: Ein separates Dokument.
|     |     -> Das Dokument beschreibt das Ritual. Nicht vollstaendig. Genug.
|     |     -> Hinweis: "Die Symbole sind eine Einladung. Der Kreis ist die Tuer."
|     |
|     +-- [Luege] "Konrad hat es erwaehnt." (Wenn Konrad-Kontakt)
|     |     -> Brandt glaubt dir. Gibt die Seiten.
|     |     -> Aber: Er konfrontiert Konrad. Nina wird wuetend auf dich.
|     |     -> Nina-Beziehung -15.
|     |
|     +-- [Verschwiegen] "Quellen schuetzen."
|           -> Brandt: Respekt. Aber kein Vertrauen. Gibt nur die Seiten, nicht das Dokument.
|
+-- [Aggressiv] "Sie wussten es die ganze Zeit. 30 Jahre!"
|     -> Brandt: Zusammenbruch. "Ja. JA. Ich wusste es. Was haette ich tun sollen?"
|     -> Beziehung -10. ABER: Ehrlichkeit. Er erzaehlt ALLES, was er weiss.
|     -> Der Preis: Sein Glaube bricht. Ab jetzt ist er ein gebrochener Mann.
|     -> Seine Companion-Faehigkeit (Gebete) funktioniert nicht mehr.
|
+-- [Gewaltbereitschaft 4+] "Geben Sie mir die Seiten. Alle."
|     -> Brandt gibt nach. Sofort.
|     -> Alle Hinweise erhalten. Kein weiteres Gespraech moeglich.
|     -> Brandt verschliesst die Kirche. Er redet mit niemandem mehr.
|     -> Andere NPCs erfahren davon: "Man hoert, Sie haben den Pfarrer bedroht."
|
+-- [MS <50, Spezial] "...ich habe sie auch gehoert. Die Stimmen. Sie sagen meinen Namen."
      -> Brandt: Schock. Dann: Mitgefuehl.
      -> Er haelt deine Hand. "Dann ist es fuer Sie schon zu spaet."
      -> Einzigartiger Hinweis: "Wenn die Praesenz deinen Namen kennt, bist du schon Teil von ihr."
      -> Mental State +5 (jemand versteht). Schuld -5 (Beichte).
```

---

## Entscheidungsbaum 4: "Der Rat"

**Zeitpunkt:** Akt 2, Kapitel 2.3
**Kontext:** Der Spieler erfaehrt vom "Rat" -- dem informellen Gremium, das entscheidet, wer als naechstes verschwindet.

```
ENTSCHEIDUNG: Was machst du mit dem Wissen ueber den Rat?

+-- [Den Rat konfrontieren]
|     -> Du platzt in eine Versammlung. Buergermeisterin, Dr. Seidl, drei Aelteste.
|     -> Buergermeisterin: "Sie verstehen nicht, was auf dem Spiel steht."
|     +-- [Moralpredigt] "Ihr mordet Menschen!"
|     |     -> Buergermeisterin: "Wir RETTEN 200 Menschen. Jedes Mal."
|     |     -> Kein Ergebnis. Du wirst ausgesperrt. Alle Beziehungen -20.
|     |
|     +-- [Verhandlung, Verstand 5+] "Ich verstehe die Logik. Aber es gibt einen anderen Weg."
|     |     -> Buergermeisterin: Interessiert. "Welchen?"
|     |     -> Du MUSST einen Vorschlag machen (oeffnet Akt-3-Pfade)
|     |     -> Wenn kein Vorschlag: Glaubwuerdigkeit verloren. Beziehung -30.
|     |
|     +-- [Drohung] "Ich werde die Aussenwelt informieren."
|           -> Stille. Blicke werden getauscht.
|           -> Buergermeisterin: "Die Aussenwelt weiss, wo Sie sind?"
|           +-- [Ja (Luege)] -> Sie werden vorsichtiger, aber nicht aufhoeren.
|           |     Schuld +5. Du gewinnst Zeit.
|           +-- [Nein (Ehrlich)] -> Du bist jetzt der naechste Kandidat.
|                 Gefahr-Level maximiert. Flucht-Optionen benoetigt.
|
+-- [Heimlich beobachten]
|     -> Du belauschst den Rat. Wahrnehmung 4+ noetig.
|     -> Du hoerst: Der naechste Name. Es ist JONA WEBER (der Teenager).
|     +-- [Jona warnen]
|     |     -> Jona panikt. Versucht zu fliehen. Schafft es oder nicht (abhaengig von Spieler-Hilfe).
|     |     -> Wenn Jona flieht: Rat braucht einen Ersatz. DU bist der Kandidat.
|     |     -> Wenn Jona bleibt: Er vertraut dir. Wird zum Verbuendeten. Lebt auf Zeit.
|     |
|     +-- [Nichts tun]
|     |     -> Jona verschwindet. Schuld +20. Mental State -15.
|     |     -> "Du wusstest es. Du hast nichts getan. Du bist jetzt wie sie."
|     |
|     +-- [Jemand anderen vorschlagen] (Nur bei Gewaltbereitschaft 4+ UND Schuld >40)
|           -> Du WIRST Teil des Systems. Du waehlst, wer geht.
|           -> Schuld +30. Mental State -20. Beziehung mit gewaehlter Person: zerstoert.
|           -> ABER: Du bist sicher. Der Rat akzeptiert dich. Neue Enden freigeschaltet.
|
+-- [Ernst informieren]
|     -> Ernst dokumentiert. Schickt Briefe nach aussen.
|     -> Langfristiger Effekt: In Akt 3 kommt Hilfe von aussen (einer von wenigen Lichtblicken).
|     -> ABER: Dauert zu lang fuer Jona. Er verschwindet trotzdem.
|
+-- [Nina einweihen]
      -> Nina wusste es bereits. Sie bricht zusammen.
      -> "Ich war DABEI. Ich habe seinen Namen gehoert und NICHTS GESAGT."
      -> -> Siehe Entscheidungsbaum: "Ninas Schuld" (unten)
```

---

## Entscheidungsbaum 5: "Ninas Schuld"

**Zeitpunkt:** Akt 2-3 Uebergang
**Kontext:** Nina gesteht dem Spieler, dass sie beim Rat war und Karls Namen gehoert hat.

```
NINA (weinend): "Ich habe dort gesessen. Ich habe seinen Namen gehoert.
                 Und ich habe... nichts gesagt. Nichts."

+-- [Troesten] "Du konntest nichts tun."
|     -> Nina: Dankbar. Vertrauen +15.
|     -> ABER: Du hast gelogen. Sie HAETTE etwas tun koennen.
|     -> Schuld +5 (fuer die Luege). Nina's Schuld bleibt. Sie wird es nie verarbeiten.
|     -> In Akt 3: Nina opfert sich, wenn die Gelegenheit kommt. Sie sucht Erloesung.
|
+-- [Ehrlich] "Du haettest etwas sagen koennen. Das weisst du."
|     -> Nina: Zusammenbruch. Vertrauen -10. Mental State -5.
|     -> ABER: Langfristig staerker. Sie akzeptiert ihre Schuld.
|     -> In Akt 3: Nina kaempft. Sie will wiedergutmachen, nicht sterben.
|
+-- [Hart, Gewaltbereitschaft 3+] "Du bist mitschuldig. Genauso wie die anderen."
|     -> Nina erstarrt. Dann: Wut.
|     -> "Und du? Du bist hergekommen und hast ALLES schlimmer gemacht!"
|     -> Beziehung: Gebrochen. Nina wird zum Antagonisten in Akt 3.
|     -> Sie verraet den Spieler an die Buergermeisterin.
|
+-- [Schweigen]
|     -> Nina wartet. 10 Sekunden. Dann steht sie auf und geht.
|     -> "Dein Schweigen sagt genug."
|     -> Beziehung: Gebrochen. Aber anders als bei Haerte: Nina zieht sich zurueck.
|     -> Sie trifft ihre eigenen Entscheidungen in Akt 3 -- ohne den Spieler.
|
+-- [Eigenes Gestaendnis, Schuld >30] "Ich habe auch... Dinge getan. Oder nicht getan."
      -> Nina schaut auf. "Was meinst du?"
      -> Der Spieler kann seine bisherigen Entscheidungen gestehen.
      -> Fuer JEDES Gestaendnis: Schuld -5. Mental State +3. Beziehung +5.
      -> Nina und der Spieler tragen die Last gemeinsam.
      -> Einzigartiger Pfad: "Gemeinsame Erloesung" (siehe Enden).
```

---

## Entscheidungsbaum 6: "Die Stahltuer"

**Zeitpunkt:** Akt 3, Kapitel 3.1
**Kontext:** Der Spieler steht vor der Tuer in Ebene 3 des Bergwerks.

```
[Die Tuer steht vor dir. Massiv. Kalt. Sie summt.]

BEDINGUNGEN PRUEFEN:
- Symbole aus Kirchenbuch? [Ja/Nein]
- Schluessel aus Rathaus? [Ja/Nein]
- Konrads letzte Worte? [Ja/Nein]
- Ernsts Anleitung? [Ja/Nein]

IF weniger als 2: Die Tuer oeffnet sich nicht.
  -> Der Spieler muss zurueck und fehlende Hinweise finden.
  -> Zeit laeuft weiter. NPCs treffen Entscheidungen ohne ihn.

IF 2: Die Tuer oeffnet sich. Langsam. Widerstand.
  -> Unvollstaendiges Wissen. Manche Wahrheiten bleiben verborgen.

IF 3: Die Tuer oeffnet sich. Leichter.
  -> Fast vollstaendiges Bild. Ein Fragment fehlt.

IF 4: Die Tuer oeffnet sich sofort. Sie hat auf dich gewartet.
  -> Vollstaendiges Wissen. Alle Enden zugaenglich.
  -> ABER: Mental State -10 ("Du bist zu tief drin.")

WER IST DABEI?
+-- [Allein]
|     -> Maximum Horror. Minimum Hilfe. Mental State sinkt schnell.
|     -> ABER: Manche Wahrheiten zeigt die Praesenz nur, wenn du allein bist.
|
+-- [Mit Maren]
|     -> Sie sucht Dieter. Sie wird ihn finden. Was uebrig ist.
|     -> Emotionaler Zusammenbruch. Spieler muss sie stabilisieren ODER zuruecklassen.
|     -> Wenn zurueckgelassen: Maren wird Teil der Praesenz. Neues Ende moeglich.
|
+-- [Mit Nina]
|     -> Nina spuert die Praesenz. Sie hat weniger Angst als erwartet.
|     -> "Ich glaube... ich war schon immer mit ihr verbunden."
|     -> Nina kann als Vermittlerin dienen (einzigartiger Akt-3-Pfad).
|
+-- [Mit Brandt]
|     -> Seine Gebete halten die Praesenz auf Abstand. Wenn sein Glaube intakt ist.
|     -> Wenn sein Glaube gebrochen: Die Praesenz antwortet auf seine Gebete.
|     -> Das ist schlimmer.
|
+-- [Mit Buergermeisterin]
      -> Sie kennt den Weg. Sie war schon hier.
      -> "Ich komme jedes Jahr. Am 6. Oktober. Um mich zu entschuldigen."
      -> Neue Perspektive: Die Buergermeisterin ist kein Monster. Sie ist ein Mensch,
         der eine unmoegliche Entscheidung getroffen hat. Immer wieder.
```
