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
