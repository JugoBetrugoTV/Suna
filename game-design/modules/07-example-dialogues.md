# Modul 07 -- Beispiel-Dialoge

---

## Hinweise zur Darstellung

- `[OPTION]` = Spieler-Auswahl
- `(BEDINGUNG)` = Voraussetzung fuer die Option
- `{EFFEKT}` = Konsequenz der Wahl
- `>>` = NPC spricht
- `<<` = Spieler spricht / denkt
- `***` = Regieanweisung / Atmosphaere
- Text in `GROSSBUCHSTABEN` bei NPC-Namen

---

## Szene 1: "Die erste Nacht"

**Ort:** Gasthaus "Zum Anker", Gastraum. Abend.
**Kontext:** Erste Interaktion mit Maren Voss nach dem Abendessen. Lilly spielt in der Ecke.
**Mental State:** 80 (Standard-Start)

---

***Der Gastraum ist warm. Holzwaende, gedimmtes Licht. Ein Kamin knistert. Drei Tische, alle leer ausser deinem. Maren wischt die Theke. Lilly malt mit Buntstiften.***

>> MAREN: "Noch ein Bier? Oder lieber Tee? Die Naechte werden kalt hier oben."

```
[1] "Ein Bier, danke."
[2] "Tee waere gut."
[3] "Wie lange ist der Pass schon blockiert?"
[4] (Wahrnehmung 3+) "Sie erwarten nicht viele Gaeste, oder?"
```

---

**Pfad [1] oder [2]:** (Small Talk, beziehungsaufbauend)

>> MAREN: ***stellt das Getraenk ab, setzt sich gegenueber*** "Sind Sie beruflich hier? Oder... auf der Durchreise?"

```
[1a] (Herkunft: Journalist) "Ich schreibe ueber abgelegene Gemeinden."
[1b] (Herkunft: Verwandt) "Ich suche jemanden. Familie."
[1c] (Herkunft: Zufall) "Autopanne. Falscher Ort, falsche Zeit."
[1d] [Luege] "Urlaub. Wandern."
```

**Pfad [1a] -- Journalist:**

>> MAREN: ***Das Laecheln bleibt, aber die Augen veraendern sich. Nur fuer einen Moment.***
>> "Oh. Schreiben. Ja, wir sind... malerisch. Haben Sie schon den See gesehen?"

***Sie wechselt das Thema. Schnell. Professionell. Als haette sie Uebung.***

<< *(Innerer Monolog, automatisch)*: Sie hat nicht gefragt, fuer wen ich schreibe. Jeder fragt das. Sie nicht.

{Maren: Misstrauen-Flag gesetzt. Naechste Gespraeche: vorsichtiger.}

---

**Pfad [4] -- Wahrnehmung-Check:**

>> MAREN: ***Haelt inne. Legt den Lappen hin.***
>> "Wir sind ein kleiner Ort. Nicht viele kommen hierher. Nicht viele... wollen hierher."

***Pause. Lilly schaut auf. Schaut Maren an. Schaut wieder auf ihr Bild.***

>> MAREN: "Es ist schoen hier. Wirklich. Nur eben... ruhig."

```
[4a] "Ruhig ist gut."
[4b] (Empathie 3+) "Sie klingen, als waere das nicht immer so gewesen."
[4c] "Was malt Lilly da?"
```

**Pfad [4b]:**

>> MAREN: ***Lange Pause. Sie schaut zu Lilly. Dann zurueck.***
>> "Mein Mann... reist viel. Beruflich. Seitdem ist es ruhiger."

***Ihre Stimme ist gleichmaessig. Zu gleichmaessig.***

<< *(Innerer Monolog, Wahrnehmung 4+)*: Das war auswendig gelernt. Jedes Wort.

{Hinweis: "Marens Mann" ins Notizbuch eingetragen.}
{Maren: Beziehung +3 (du hast zugehoert)}

---

**Pfad [4c] -- Lilly:**

***Du gehst zu Lilly. Sie malt ein Haus. Schwarz. Alle Fenster schwarz. Vor dem Haus steht eine Figur. Zu gross. Zu duenn.***

>> LILLY: ***schaut auf, laechelt*** "Das ist unser Haus."

```
[4c-1] "Und wer ist das vor dem Haus?"
[4c-2] "Schoenes Bild, Lilly."
[4c-3] (Wahrnehmung 4+) ***Du schaust genauer hin. Die Figur hat keinen Schatten.***
```

**Pfad [4c-1]:**

>> LILLY: "Das ist der Mann, der nachts kommt."

>> MAREN: ***schnell, von der Theke*** "Lilly, Zeit fuers Bett."

>> LILLY: "Aber Mama --"

>> MAREN: "Jetzt."

***Lilly nimmt das Bild. Geht nach oben. Maren laechelt dich an. Es ist das gleiche Laecheln wie vorher. Genau das gleiche.***

>> MAREN: "Kinder und ihre Fantasie."

{Mental State -2}
{Hinweis: "Lillys Zeichnung" ins Notizbuch}
{Maren: Beziehung -5 (du hast eine Grenze beruehrt)}

---

## Szene 2: "Das Verhoer"

**Ort:** Kraemerladen Hofer. Nachmittag, Akt 2.
**Kontext:** Der Spieler hat Ernsts Briefe entdeckt und konfrontiert ihn.
**Mental State:** 55 (angespannt)

---

***Der Laden ist leer. Ernst sortiert Konserven. Seine Haende zittern leicht. Er hat dich kommen sehen. Er weiss, warum du hier bist.***

>> ERNST: ***ohne aufzuschauen*** "Brauchen Sie etwas? Die Bohnen sind frisch."

```
[1] "Ich weiss von den Briefen, Ernst."
[2] (Manipulativ, Verstand 4+) "Die Buergermeisterin hat mir von Ihrem... Hobby erzaehlt."
[3] (Empathie 3+) "Wie lange tragen Sie das schon allein?"
[4] (Gewaltbereitschaft 3+) "Wir muessen reden. Und zwar ehrlich."
```

---

**Pfad [1] -- Direkt:**

***Ernst stellt die Dose ab. Langsam. Dreht sich um.***

>> ERNST: "Welche Briefe?"

<< "An wen schreiben Sie? Und wer schreibt zurueck?"

>> ERNST: ***nimmt die Brille ab. Putzt sie. Setzt sie wieder auf. Eine Geste, die er immer macht, wenn er Zeit braucht.***
>> "Sie haben mein Lager durchsucht."

```
[1a] "Ja."
[1b] "Nein, jemand hat es mir gesagt."
[1c] [Schweigen]
```

**Pfad [1a]:**

>> ERNST: "Dann wissen Sie mehr als die meisten." ***Pause.*** "Und weniger als Sie glauben."

>> ERNST: ***schliesst den Laden ab. Dreht das Schild auf 'GESCHLOSSEN'.***
>> "Ich bin seit 30 Jahren hier. Ich kam, weil mein Bruder hier verschwunden ist. STEFAN HOFER. 1991."

***Er setzt sich. Zum ersten Mal siehst du ihn stillsitzen.***

>> ERNST: "Ich habe ihn nie gefunden. Aber ich habe gefunden, WARUM er verschwunden ist."

```
[1a-1] "Erzaehlen Sie."
[1a-2] "Warum haben Sie nie etwas getan?"
[1a-3] (MS <50) "Ich habe Angst, Ernst. Vor dem, was Sie mir sagen werden."
```

**Pfad [1a-2]:**

>> ERNST: ***Stille. Lang. Seine Haende umklammern die Theke.***
>> "Was haette ich tun sollen? Die Polizei rufen? Die kommen nicht her. Einen Artikel schreiben? Wer wuerde das drucken? Hier verschwinden alle paar Jahre Menschen in einem Ort, der auf keiner Karte steht."

>> ERNST: "Also habe ich dokumentiert. Jedes Verschwinden. Jeden Namen. Jedes Datum. 30 Jahre. 11 Namen."

>> ERNST: ***leise*** "Und jetzt sind Sie hier. Und ich frage mich, ob Sie Nummer 12 werden. Oder ob Sie der sind, auf den ich gewartet habe."

{Ernst: Vertrauen -> Offen}
{Hinweis: "Ernsts Archiv" -- Liste aller Verschwundenen}
{Hinweis: "Stefan Hofer, 1991"}
{Schuld-Check: Ernst traegt Schuld. Erkennt der Spieler sich darin wieder?}

---

## Szene 3: "Unter der Erde"

**Ort:** Bergwerk, Ebene 2. Nacht.
**Kontext:** Der Spieler ist allein im Bergwerk. Akt 2.
**Mental State:** 42 (instabil)

---

***Die Luft ist feucht und warm. Zu warm fuer diese Tiefe. Deine Lampe flackert. Die Symbole an den Waenden werfen Schatten, die sich nicht richtig bewegen.***

***Dann hoerst du es. Nicht mit den Ohren. In deinem Kopf.***

>> STIMME: ***kein Klang, nur Worte, die da sind*** "...du bist gekommen..."

```
[1] (Willenskraft 4+) "Wer bist du?"
[2] (MS <50) "...ja."
[3] [Umdrehen und gehen]
[4] [Schweigen. Zuhoeren.]
```

---

**Pfad [4] -- Schweigen:**

***Du stehst still. Die Lampe flackert schneller. Die Waende pulsieren. Oder bilden du dir das ein?***

>> STIMME: "...du suchst...wir suchen auch...immer suchen...nie finden..."

***Bilder. Nicht vor deinen Augen -- dahinter. Blitze von Erinnerungen, die nicht deine sind:***
- ***Ein Mann kniet im Dunkeln. Weint. Traegt Bergmannskleidung. 1924.***
- ***Eine Frau steht am See. Geht ins Wasser. Schaut nicht zurueck.***
- ***Ein Kind laeuft durch den Wald. Lacht. Das Lachen verzerrt sich.***
- ***Dein eigenes Gesicht. Aber die Augen sind falsch. Zu dunkel. Zu tief.***

```
[4a] (Willenskraft 5+) "Das sind nicht meine Erinnerungen. Lass mich gehen."
[4b] (Empathie 4+) "Ihr leidet."
[4c] (MS <40) "Zeig mir mehr."
[4d] ***Du merkst, dass du weinst. Du weisst nicht warum.***
```

**Pfad [4b]:**

>> STIMME: ***laenger. Klarer.*** "...leiden...ja...immer...seit sie uns gerufen haben...wir wollten nicht kommen...wir konnten nicht NICHT kommen..."

***Die Temperatur steigt. Schweiss auf deiner Stirn. Oder sind es Traenen?***

>> STIMME: "...du bist warm...du bist voller...Dinge...Schuld...Angst...Erinnerungen...so voll..."

```
[4b-1] "Was willst du von mir?"
[4b-2] "Ich kann euch helfen."
[4b-3] (Verstand 4+) "Ihr seid keine Person. Ihr seid ein Echo."
```

**Pfad [4b-1]:**

>> STIMME: "...bleib...nur...bleib..."

***Die Lampe geht aus. Absolute Dunkelheit. Fuer 5 Sekunden. Echtzeit. Kein Input moeglich.***

***Dann kommt das Licht zurueck. Du stehst am Eingang des Bergwerks. Draussen. Es ist Morgen.***

***Du hast keine Erinnerung an den Rueckweg.***

{Mental State -12}
{Schuld: unbestimmt -- +5 ODER -5, abhaengig von Interpretation}
{Hinweis: "Die Praesenz spricht" -- "Sie sagen, sie wollten nicht kommen."}
{Hinweis: "Verlorene Zeit" -- "Ich war Stunden da drin. Es fuehlt sich an wie Minuten."}
{Notizbuch-Eintrag (automatisch, MS-abhaengig):}
  MS 50+: "Die Stimme im Bergwerk. Sie klang... traurig."
  MS 30-49: "SIE HAT MIT MIR GEREDET. Sie will mich. Ich glaube, ich will auch."
  MS <30: [Der Eintrag ist leer. Nur ein nasser Fleck auf der Seite.]

---

## Szene 4: "Marens Wahrheit"

**Ort:** Gastzimmer. Nacht. Akt 2.
**Kontext:** Maren kommt zum Spieler, nachdem er Dieters Ring im Brunnen gefunden hat. Vertrauen 60+.

---

***Klopfen an der Tuer. Leise. Dreimal.***

***Maren steht im Flur. Ohne Schuerze. Ohne Laecheln. Sie sieht 10 Jahre aelter aus.***

>> MAREN: "Darf ich reinkommen?"

***Sie setzt sich auf den Stuhl am Fenster. Schaut hinaus. Lange.***

>> MAREN: "Sie haben seinen Ring gefunden."

***Keine Frage. Eine Feststellung.***

>> MAREN: "Dieter ist nicht auf Reisen. Das wussten Sie schon."

```
[1] "Ja."
[2] "Seit wann weisst du es?"
[3] [Schweigen. Sie reden lassen.]
[4] (Empathie 4+) ***Du setzt dich neben sie. Sagst nichts.***
```

**Pfad [3] -- Schweigen:**

***Stille. Eine Minute. Zwei. Maren atmet. Gleichmaessig. Dann nicht mehr.***

>> MAREN: "Drei Jahre. Drei Jahre habe ich mir selbst gesagt, dass er wiederkommen wird."
>> "Am Anfang habe ich gesucht. Ueberall. Den Wald. Die Berge. Das Bergwerk."
>> "Dann hat Lena -- die Buergermeisterin -- mich besucht."

***Maren dreht sich um. Ihre Augen sind trocken. Schlimmer als Traenen.***

>> MAREN: "Sie hat gesagt: 'Maren. Dieter hat seine Pflicht getan. Fuer Hollowmere. Fuer Lilly. Hoer auf zu suchen. Oder die naechste Pflicht faellt auf jemand anderen.'"

```
[3a] "Lilly."
[3b] "Das ist eine Drohung."
[3c] "Und du hast aufgehoert."
[3d] (Gewaltbereitschaft 3+) "Und du hast das AKZEPTIERT?"
```

**Pfad [3c]:**

>> MAREN: ***Nickt. Langsam.***
>> "Ich habe aufgehoert. Fuer Lilly. Was haette ich tun sollen? Weglaufen? Wohin? Der Pass war -- IST -- blockiert."

>> MAREN: "Also laechle ich. Koche Essen. Mache Betten. Und jeden Abend, wenn Lilly schlaeft, stehe ich am Fenster und frage mich, ob es heute Nacht klopft."

>> MAREN: ***schaut dich an. Direkt.***
>> "Sie sind der erste Mensch seit drei Jahren, dem ich das sage. Und ich sage es Ihnen, weil..."

***Pause. Lang.***

>> MAREN: "...weil ich glaube, dass Sie entweder der Mensch sind, der das hier beendet. Oder der naechste, der verschwindet."

```
[3c-1] "Ich werde es beenden."
[3c-2] "Ich weiss nicht, was ich bin."
[3c-3] "Komm mit mir. In das Bergwerk. Wir finden raus, was mit Dieter passiert ist."
[3c-4] (MS <40) "Vielleicht... verschwinden ist nicht das Schlimmste."
```

**Pfad [3c-4] -- Gebrochener Spieler:**

>> MAREN: ***Greift nach deiner Hand. Fest.***
>> "Nein. NEIN. Sie reden wie Dieter kurz bevor... Nein."

>> MAREN: "Hoeren Sie mir zu. Was immer da unten ist, was immer es Ihnen zeigt -- es LUEGT. Es zeigt Ihnen, was Sie sehen wollen. Nicht was wahr ist."

{Mental State +8 (jemand kaempft fuer dich)}
{Maren: Vertrauen +20}
{Maren: Companion freigeschaltet}
{Hinweis: "Die Praesenz luegt. Oder: Sie zeigt eine Wahrheit, die sich anfuehlt wie Trost."}

---

## Szene 5: "Konrads letzte Stunde"

**Ort:** Hof Althammer. Konrads Schlafzimmer. Akt 3.
**Kontext:** Konrad stirbt. Nina ist anwesend. Konrads letzte Worte haengen vom Spielverlauf ab.

---

***Das Zimmer riecht nach Kamille und nach etwas Suesslicherem. Konrad liegt im Bett. Sein Atem rasselt. Nina haelt seine Hand.***

>> NINA: ***fluestert*** "Er will mit Ihnen sprechen. Allein."

***Nina schaut dich an. Ihre Augen sagen: Bitte. Sei sanft.***

***Sie geht. Die Tuer schliesst sich.***

***Konrads Augen sind offen. Klar. Zum ersten Mal seit du ihn kennst, ist sein Blick fokussiert.***

>> KONRAD: ***jedes Wort kostet Kraft*** "Setz dich."

***Du setzt dich. Der Stuhl knarrt.***

>> KONRAD: "Ich habe nicht mehr lang. Das ist in Ordnung. Ich bin muede."

>> KONRAD: "Aber du musst etwas wissen. Bevor ich gehe."

**[Variante A: Der Spieler war ehrlich zu Konrad]**

>> KONRAD: "Du hast mir die Wahrheit gesagt. Das hat hier lang niemand mehr getan."
>> "Also gebe ich dir die Wahrheit zurueck."
>> "Der Riss kann geschlossen werden. Mein Vater hat es mir gezeigt. Die Symbole, umgekehrt. Der Kreis, gebrochen. Die Worte, rueckwaerts."
>> ***Pause. Atem.***
>> "Aber wer schliesst, bleibt. Nicht tot. Nicht lebendig. Dazwischen. Fuer immer."
>> "Mein Vater wusste es und hat es nicht getan. Und ich habe 87 Jahre mit dieser Schuld gelebt."

>> KONRAD: ***greift deine Hand. Fest. Unerwartet stark.***
>> "Du musst nicht bleiben. Aber jemand muss schliessen."

{Hinweis: "Konrads Anleitung" -- vollstaendig}
{Hinweis: "Der Preis des Schliessens"}
{Mental State: +5 ODER -10, abhaengig von Willenskraft}

**[Variante B: Der Spieler hat Konrad angelogen]**

>> KONRAD: ***Blick wird scharf*** "Du hast mich angelogen."
>> "Glaubst du, ich merke das nicht? Ich bin alt, nicht dumm."
>> "Du bist wie die anderen. Nimmst, was du brauchst, und gibst nichts zurueck."
>> ***Husten. Blut.***
>> "Der Riss kann geschlossen werden. Aber ich sage dir nicht wie."
>> "Frag die, denen du vertraust. Falls es die noch gibt."

{Konrads Anleitung: NICHT erhalten}
{Mental State -5}
{Schuld +10}

**[Variante C: Der Spieler hat Konrad ignoriert]**

***Du betrittst das Zimmer. Konrad liegt still. Augen geschlossen.***

***Nina sitzt neben ihm. Sie weint lautlos.***

>> NINA: "Er ist vor einer Stunde eingeschlafen. Er wird nicht mehr aufwachen."

***Keine letzten Worte. Keine Anleitung. Die Information ist verloren.***

{Konrads Anleitung: permanent verloren}
{Mental State -3}
{Schuld +5 -- du hast ihn nicht besucht, als er dich brauchte}
