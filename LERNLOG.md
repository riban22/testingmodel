# Lernlog – Musterstadt-Prüfstand

## Phase 0 – Setup (25.11.2026)

**Was gebaut wurde**
- Virtuelle Umgebung `.venv` mit Python 3.13 angelegt (bewusst nicht 3.15, weil große Bibliotheken neue Versionen oft erst später unterstützen).
- Playwright 1.65.2 installiert, dazu Chromium als Browser.
- `requirements.txt` von Hand angelegt: nur direkt genutzte Pakete, Version festgelegt (gepinnt).
- Erstes Skript `crawler/first_screenshot.py`: öffnet example.com, gibt den Titel aus, speichert einen Screenshot.
- `screenshots/` in die `.gitignore` aufgenommen (erzeugte Dateien gehören nicht ins Repository).

**Was ich gelernt habe**
- Eine virtuelle Umgebung trennt die Pakete eines Projekts vom restlichen System. `(.venv)` vor der Eingabezeile zeigt, dass sie aktiv ist.
- Pakete werden mit `pip` installiert. Abhängigkeiten (z. B. `greenlet`) holt pip automatisch mit.
- `headless=False` zeigt den Browser bei der Arbeit, was beim Debuggen hilft. Standard ist unsichtbar.
- Insgesamt hat alles gut geklappt.

**Was schwierig war**
- Mit VS Code, Claude Code und Git habe ich noch wenig Erfahrung.
- Ich habe nicht direkt verstanden, wo die neue Datei liegt.
  → Tipp: **Strg + P** und den Dateinamen tippen. Oder den Ordner `testingmodel` direkt in VS Code öffnen, dann ist der Explorer übersichtlicher.

## Phase 1 – Musterstadt (25.11.2026)

**Was gebaut wurde**
- Test-Website „Musterstadt“ mit 5 Seiten: Startseite, Bürgerservice, Ummeldeformular, Abfall und Entsorgung, Kontakt.
- 16 absichtlich eingebaute Fehler: Barrierefreiheit (WCAG), Usability (ISO 9241-110) und Funktion (toter Link, Konsolenfehler).
- `FEHLERLISTE.md` als Ground Truth: Fundort als CSS-Selektor, vorab festgelegte Auswertungsregeln für Grenzfälle, Abschnitte „Bewusst kein Fehler“.
- Jede Seite automatisch mit Playwright geprüft, inklusive Gegenprobe (läuft der Code nach Korrektur des Fehlers sauber?).

**Was ich gelernt habe**
- Die Grundlagen von Git: `status`, `add`, `commit`, `push`, und warum `.gitignore` erzeugte Dateien draußen hält.
- Eine Ground Truth muss **eindeutig und vollständig** sein. Grenzfälle entweder eindeutig machen oder die Auswertungsregel **vor** der Auswertung festlegen. (Das Problem aus meiner Bachelorarbeit: Die KI fand echte, nicht eingebaute Fehler, und die Bewertung wurde schwierig.)
- Nicht jeder Fehler ist für jedes Werkzeug sichtbar: axe-core findet z. B. Pseudo-Überschriften (F12) oder Platzhalter statt Label (F08) nicht. Dafür braucht es eigene Regeln oder KI.
- Minimalpaare (fehlerhaft und korrigiert, sonst identisch) als Grundlage für saubere Test- und Trainingsdaten.
- Seiten mit Entwicklertools (F12), Konsole und der Windows-Sprachausgabe prüfen.

**Was schwierig war**
- Mit Unterstützung nichts Größeres. Git war neu, ist aber jetzt in den Grundzügen klar.

## Phase 2 – Browser steuern (25.11.2026)

**Was gebaut wurde**
- `crawler/page_reader.py`: liest Links, Buttons und Eingabefelder (mit Label, Platzhalter, Pflichtfeld) einer Seite aus.
- `crawler/actions.py`: klicken und tippen, mit Sicherheitsregel. Gefährliche Aktionen („absenden“, „löschen“, „bezahlen“ …) werden erkannt und übersprungen.
- 19 pytest-Tests gegen die Musterstadt-Seiten, gemeinsame Vorbereitung in `tests/conftest.py`.

**Was ich gelernt habe**
- pytest: Tests vergleichen Erwartung und Ergebnis (`assert`), Fixtures bereiten Tests vor, `parametrize` lässt einen Test mit vielen Werten laufen.
- Das Tool sieht eine Seite so, wie ein Screenreader sie sieht. Deshalb wurden F05 (Link ohne Text), F08 (Feld ohne Label) und F14 (Div statt Button) schon beim bloßen Auslesen sichtbar.
- Grenzen von Regeln: Was nicht korrekt ausgezeichnet ist (F14), findet eine Suche nicht. Eine Wortliste für gefährliche Aktionen hat Falsch-Positive und Falsch-Negative. Hier könnte ein Modell später helfen.
- Refactoring: Code umbauen, ohne das Verhalten zu ändern. Die Tests beweisen, dass nichts kaputtgegangen ist.
- Ohne `(.venv)` vor der Eingabezeile findet PowerShell `pytest` nicht.
- Ich lerne besser, wenn Claude baut und erklärt, statt mir Programmieraufgaben zu geben. Die CLAUDE.md ist entsprechend angepasst.

**Was schwierig war**
- Selbst Code zu schreiben. Code lesen und verstehen klappt gut.
