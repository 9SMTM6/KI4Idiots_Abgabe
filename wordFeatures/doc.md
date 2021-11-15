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
* Viele Wörter haben keinen inhärenten Informationsgehalt, diese wollen wir entfernen. NLTK bietet da Hilfe auf 2erlei Wegen, einmal gibt es eine Liste häufig vorkommender Wörter die geringen Informationsgehalt haben ("to", "I", "my", "theirs"), nltk.corpus.stopwords.words("english"), zudem hat es einen Part-Of-Speech tagger nltk.pos_tagger. Diese bieter sehr viele Infos, wir wollten es nicht in der allgemeinheit behandeln, es gibt eine Option um weniger Infos zu bekommen, tagset="universal". Dies klassifiziert nur nach: Verb, Nomen, Adjektiv, Pronom, Conjunktiv, Zahl, Partikular, Satzzeichen, Determinativ.
* Die Rangliste sollte grundsätzlich davon abhängen, wie häufig ein Wort vorkommt: nltk.FreqDist, liefert auf eine Liste angewandt die vorkommensanzahl der einzeln vorkommenden Wörter
* Um die verschiedenen Kategorien fair zu behandeln, sie aber unterschiedlich viel Stoff haben könnten, sollte die Häufigkeit unabhängig zwischen den Kategorien bestimmt werden.
* Eine weitergehende möglichkeit ist das Stemming. In dem Fall wollen wir wirklich nur stemmen, denn bei diesen Algorithmen kann findet man das resultat in der Ursprungseingabe wirklich wieder, beim Lemmatizing nicht unbedingt.


# Zusammenfassung / gemeinsame verwendung der erzeugten Wortlisten mit Features

