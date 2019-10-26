Nils Lorentzen, Paul Golz

25.10.2019

Hangman - Spiel

Vorzufinden ist das Spiel Hangman in einer kleinen und unkomplizierten Ausführung.
Es stehen bereits 658 Wörter zur Verfügung, die in der Datei dat/deutsch.txt gespeichert sind.
Um die Liste zu erweitern einfach diese Text Datei öffnen und ein beliebiges Wort hinzufügen.
Dabei ist zu beachten dem Muster zu folgen und für jedes Wort eine neue Zeile zu beginnen.

Um Hangman zu spielen die Datei Hangman.py öffnen und ausführen.
Es wird jetzt per Zufall ein Wort ausgesucht, welches dann durch den Spieler zu lösen ist und es öffnet sich ein Spiel-Fenster.
Zu beachten ist, dass Umlaute der deutschen Sprache automatisch umgewandelt werden (z.B.: Ä zu Ae, ö zu oe, ß zu ss).
Für die Eingabe mit der Maus über den gewünschten Buchstaben im Spiel-Fenster fahren und ihn per Linksklick auswählen.

Erscheint der Buchstabe ROT war dieser Falsch, erscheint er GRÜN war dieser Richtig.
Unter den Buchstaben Feldern ist das gesuchte Wort zu sehen. Jedoch muss dieses erst Buchstabe für Buchstabe aufgedeckt werden.
Anfangs sind in diesem Feld nur Unterstriche, also _, zu sehen. (z.b.: Wenn das gesuchte Wort "Hallo" ist wird es so "_ _ _ _ _" dargestellt)
Mit dem Spielverlauf werden die Unterstriche durch die jeweiligen Buchstaben ersetzt. (z.b.: " H _ l l _ " ---> "Hallo")

Sollte ein Falscher Buchstabe getippt werden reduzieren sich die Versuche.
Sollten die Versuche auf 0 fallen ist das Spiel beendet.
Sollten sie das gesamte Wort erraten bevor die Versuche auslaufen gewinnen sie.

Um das Programm zu beenden das Fenster schließen oder auf das Feld mit EXIT klicken.

###############################################################################

Geplant ist:

Ein eigenes Programm zum hinzufügen von Wörtern in der Wörter-Datei.

Eine Zeichnung im oberen Spielfeld, die anzeigt wieviele Fehlversuche bereits getätigt wurden. (Der "Hangman")

