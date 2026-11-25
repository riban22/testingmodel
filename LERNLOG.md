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
