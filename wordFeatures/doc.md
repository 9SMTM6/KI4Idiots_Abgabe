# Grundidee:

Verschiedene Wörter kommen unterschiedlich häufig vor in verschiedenen Themenbereichen. Wir wollen das als Features abbilden.

Wir könnten manuell Wörter erfinden, aber damit müssen wir die Arbeit leisten, verpassen vermutlich Wörter, können weniger mit den Wörtern rumspielen, da wir nicht wirklich eine größe dafür haben, wie relevant sie sind.

Alternative: Algorithmische erstellung der Wörter, nach denen gesucht wird.

# Grundregeln / zu beachten:

Da der verwendete Algorithmus nur auf Zahlen oder Sets als Features arbeitet, müssen die Features in der Form vorliegen.

Da wir dem Algorithmus essentiell das Essen vorkauen, müssen wir, um streng den Regeln zu folgen, vorsichtig sein, was wir vorkauen: Unsere Algorithmen dürfen als Grunddaten lediglich die Trainingsdaten haben.

Zudem wollen wir, das die Features letztlich lediglich auf den Wörtern und ihrer "Häufigkeit" selbst basieren, dinge wie die Länge des Posts handhaben wir separat, also wollen wir die Daten gegen diese Einflüsse normalisieren.

# Ideen

unimplementiert: Irgendwie umgekehrt proportional zu gesamtanzahl minus anzahl in dem ort

* nltk.word_tokenizer: Auf die einzelnen Blogs angewandt versucht die Wörter darin zu isolieren
* Viele Wörter haben keinen inhärenten Informationsgehalt, diese wollen wir entfernen. NLTK bietet da Hilfe auf 2erlei Wegen, einmal gibt es eine Liste häufig vorkommender Wörter die geringen Informationsgehalt haben ("to", "I", "my", "theirs"), nltk.corpus.stopwords.words("english"), zudem hat es einen Part-Of-Speech tagger nltk.pos_tagger. Diese bietet sehr viele Infos, es gibt eine Option um weniger Infos zu bekommen, tagset="universal", dies war uns für den aufwand dieser aufgabe ausreichend. Dieses klassifiziert nur nach: Verb, Nomen, Adjektiv, Pronom, Conjunktiv, Zahl, Partikular, Satzzeichen, Determinativ, Unbekannt.
* Die Rangliste sollte grundsätzlich davon abhängen, wie häufig ein Wort vorkommt: nltk.FreqDist, liefert auf eine Liste angewandt die vorkommensanzahl der einzeln vorkommenden Wörter
* Um die verschiedenen Kategorien fair zu behandeln, sie aber unterschiedlich viel Stoff haben könnten, sollte die Häufigkeit unabhängig zwischen den Kategorien bestimmt werden.
* Eine weitergehende möglichkeit ist das Stemming. In dem Fall wollen wir wirklich nur stemmen, denn bei diesen Algorithmen kann findet man das resultat in der Ursprungseingabe wirklich wieder, beim Lemmatizing nicht unbedingt.

# Zusammenfassung / gemeinsame verwendung der erzeugten Wortlisten mit Features

Zum erstellen der Wortlisten haben wir zunächst alle Blogs Tokenized, dann die Tokenliste pro Kategorie zusammengefügt. Aus diesen Listen haben wir die Stopwords entfernt, dann den POS-Tagger angewandt und nur Nomen, Verben, Adjektive und unbekannte Wörter beibehalten.

Anschließend haben wir optional die vorhandenen Wörter gestemmt, mit nltk.PorterStemmer, oder die Wörter so belassen. 

Über das Ergebnis des ganzen haben wir die Frequenzverteilung berechnet (d.h. wie oft kommen einzelne Wörter vor). Diesen Schritt haben wir einmal auf den Wortlisten der einzelnen Kategorien gemacht und einmal auf auf der Kombination aller Kategorien, sodas wir für jedes Wort wissen, wie oft es in den einzelnen Kategorien vorkommt, und insgesamt.

Anschließend haben wir verschiedene Rankings versucht, die mit den Frequenzverteilungen erstellt wurden. Auf diese wird später eingegangen. Nach diesen Rankings wurden anschließend Wörter ausgesucht. Dabei haben wir 3 optionale Stellschrauben festgelegt: Den ausschluß von Wörtern, deren Rang unter einem Schwellenwert ist und die Auswahl von N Wörtern nach Rang, einmal je nach Kategorie, einmal insgesamt.

# Rankings

Dann zu den Rankings. Hier wurden ein paar alternativen ausprobiert. Der simpelste Algorithmus verwendet einfach nur die Anzahl wie oft das Wort in seiner Kategorie vorkommt (N_wort).

Eine mögliche Verbesserung davon ist es, das Vorkommen des Wortes in der Kategorie durch das Vorkommen in allen zu Teilen ("Häufigkeit" in der Kategorie). Dies ist allerdings Problematisch, da dadurch auch Wörter gut wegkommen, die insgesamt selten vorkommen, diese sind aber vermutlich kein guter entscheider sondern einfach ungewöhnliche Wörter.

Daher wollen wir desweiteren die insgesamte Häufigkeit des Wortes bestimmen und diese beiden Größen verknüpfen. Wenn wir die 