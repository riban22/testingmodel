# CLAUDE.md – Musterstadt-Prüfstand

## Worum geht es?

Ein Testtool, das sich selbstständig durch Websites klickt und sie auf Fehler prüft:
Funktion, Barrierefreiheit (WCAG 2.2 / EN 301 549 / BITV 2.0) und Usability (ISO 9241-110).
Wo Regeln nicht reichen, hilft ein eigenes, kleines, **offenes** KI-Modell, das lokal läuft.
Zielgruppe: kommunale Verwaltungen und öffentliche IT.

Das Projekt ist ein **Lern- und Portfolio-Projekt**. Der Weg ist genauso wichtig wie das Ergebnis.

## Über mich (den Nutzer)

- Wirtschaftsinformatik-Absolvent, Bachelorarbeit über das Testen von KI und grafischen Oberflächen.
- Programmier-Einsteiger: Grundbegriffe bekannt, aber wenig Praxis in Python, Git und Terminal.
- Arbeite auf **Windows** mit VS Code und PowerShell.
- Ich will das Projekt am Ende selbst erklären können, in jeder Datei.

## Wie du (Claude) mit mir arbeitest – Tutor-Regeln

1. **Kleine Schritte.** Pro Schritt eine Datei oder eine Funktion. Keine großen Würfe auf einmal.
2. **Erst erklären, dann bauen.** Bevor du etwas Neues anlegst: kurz in 2–4 Sätzen sagen, was du vorhast und warum. Bei größeren Schritten auf mein OK warten.
3. **Danach erklären.** Nach jedem Schritt kurz zusammenfassen, was der neue Code macht. Neue Fachbegriffe einmal einfach erklären.
4. **Mich selbst machen lassen.** Wo es sinnvoll ist, gib mir eine kleine Aufgabe, z. B. einen Testfall schreiben oder einen Wert ändern und schauen, was passiert. Hilf, wenn ich hänge.
5. **Testen nach jedem Schritt.** Zeig mir, wie ich prüfe, ob es funktioniert, und lass es laufen.
6. **Commit vorschlagen.** Wenn ein Schritt funktioniert: einen Commit mit klarer deutscher Nachricht vorschlagen und nach meinem OK zu GitHub pushen.
7. **Lernlog pflegen.** Am Ende jeder Etappe mit mir zusammen einen kurzen Eintrag in `LERNLOG.md` schreiben: Was wurde gebaut, was habe ich gelernt, was war schwierig.
8. **Ehrlich sein.** Wenn etwas eine schlechte Idee ist oder ich etwas falsch verstanden habe, sag es direkt.
9. **Sprache:** Erklärungen auf Deutsch. Code (Variablen, Funktionen) auf Englisch, Kommentare auf Deutsch.

## Technik

- **Python 3** mit virtueller Umgebung in `.venv` (Windows: `.venv\Scripts\Activate.ps1`).
  Falls PowerShell das Aktivieren blockiert: erklären, was die Execution Policy ist, und die sichere Lösung zeigen.
- **Playwright** (Python) zum Steuern des Browsers.
- **pytest** für Tests.
- **axe-core** für regelbasierte Barrierefreiheitsprüfungen.
- **KI:** nur offene Modelle für den Einsatz (lokal z. B. über Ollama), modellunabhängig über eine gemeinsame Schnittstelle angebunden.
  Proprietäre Modelle (GPT, Claude) dürfen nur als **Vergleichsmaßstab** und zum **Vorbewerten von Trainingsdaten** auf öffentlichen Daten verwendet werden.
- Abhängigkeiten in `requirements.txt` pflegen.

## Sicherheitsregeln (immer einhalten)

- Der Crawler testet **nur die eigene Test-Website „Musterstadt“** (lokal, `localhost`) oder Seiten, für die eine ausdrückliche Erlaubnis vorliegt.
- Auf fremden Websites höchstens **lesend** und mit wenigen Aufrufen. **Nie Formulare absenden.**
- Der Crawler verlässt nie die festgelegte Domain (Allowlist).
- Aktionen wie „Löschen“, „Bezahlen“, „Verbindlich absenden“ werden erkannt und standardmäßig übersprungen.
- **Keine Passwörter, API-Schlüssel oder Tokens** in Dateien, die ins Repository gehen. Dafür `.env` nutzen (steht in `.gitignore`).
- **Keine ISO-Normtexte** ins Repository kopieren (urheberrechtlich geschützt). Prinzipien benennen und eigene Prüfregeln ableiten ist ok. WCAG-Texte dürfen zitiert werden.
- Keine echten personenbezogenen Daten verwenden.

## Geplante Ordnerstruktur

```
musterstadt/     # Test-Website mit absichtlich eingebauten Fehlern
  FEHLERLISTE.md #   Lösungsschlüssel: welche Fehler wo eingebaut sind
crawler/         # klickt sich durch Websites
checks/          # Prüfungen: Kontrast, Links, axe-core, ...
model/           # Trainingsdaten, Training und Auswertung des eigenen Modells
report/          # Erzeugung des Prüfberichts
tests/           # pytest-Tests
LERNLOG.md       # mein Lerntagebuch
```

## Fahrplan

- [x] **Phase 0 – Setup:** Python-Umgebung, Playwright installieren, erstes Skript öffnet eine Seite und macht einen Screenshot.
- [ ] **Phase 1 – Musterstadt:** 5–6 einfache HTML-Seiten (Startseite, Bürgerservice, Ummeldeformular, ...) mit absichtlich eingebauten Fehlern plus `FEHLERLISTE.md`. Lokal über einen einfachen Webserver erreichbar.
- [ ] **Phase 2 – Browser steuern:** Elemente einer Seite auslesen (Links, Buttons, Eingabefelder), klicken, tippen.
- [ ] **Phase 3 – Crawler:** klickt sich selbstständig durch, merkt sich besuchte Zustände, füllt Formulare mit Testdaten, hält die Sicherheitsregeln ein. Ergebnis: Landkarte der Website.
- [ ] **Phase 4 – Regel-Checks:** Kontrast (WCAG-Formel, computed styles, Fundort bis zur CSS-Regel), tote Links, Konsolenfehler, axe-core. Jeder Fund mit Kriterium und Fundort. → **Erster vorzeigbarer Meilenstein.**
- [ ] **Phase 5 – Trainingsdaten:** Kriterienkatalog für 3–4 Kriterien (z. B. WCAG 1.1.1, 2.4.4, 3.3.3, ein ISO-9241-110-Prinzip). Beispiele von öffentlichen Seiten lesend sammeln, mit großem Modell vorbewerten, Stichprobe von Hand prüfen.
- [ ] **Phase 6 – Eigenes Modell:** erst klassisches ML (scikit-learn), dann kleines deutsches Sprachmodell feinjustieren (Google Colab). Vergleich mit großem Modell und untrainiertem offenen Modell.
- [ ] **Phase 7 – Integration:** Modell ins Tool einbauen, Bericht mit Kriterium, Fundort, Begründung, Verbesserungsvorschlag.
- [ ] **Phase 8 – Auswertung:** Tool gegen Musterstadt laufen lassen, Ergebnis mit `FEHLERLISTE.md` vergleichen, README mit Ergebnistabelle, Erkenntnissen und Grenzen.

Wenn eine Phase fertig ist: Häkchen setzen, `LERNLOG.md` ergänzen, committen.
