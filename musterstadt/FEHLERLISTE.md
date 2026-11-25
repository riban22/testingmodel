# Fehlerliste – Musterstadt (Ground Truth)

Lösungsschlüssel: Diese Fehler sind **absichtlich** eingebaut.
In Phase 8 vergleichen wir die Funde des Tools mit dieser Liste (Precision, Recall, F-Score).

Der **Fundort** wird als CSS-Selektor angegeben, nicht als Zeilennummer.
So bleibt er gültig, auch wenn sich die HTML-Datei ändert.

## index.html – Startseite

| ID | Fundort | Kategorie | Kriterium | Beschreibung |
|----|---------|-----------|-----------|--------------|
| F01 | `header img` | Barrierefreiheit | WCAG 1.1.1 Nicht-Text-Inhalt (A) | Das Wappen-Bild hat kein `alt`-Attribut. |
| F02 | `p.hinweis` | Barrierefreiheit | WCAG 1.4.3 Kontrast (Minimum) (AA) | Text `#999999` auf `#ffffff` hat einen Kontrast von 2,85 : 1, nötig sind 4,5 : 1. |
| F03 | `a[href="parkausweis.html"]` | Barrierefreiheit | WCAG 2.4.4 Linkzweck (im Kontext) (A) | Der Linktext „Mehr erfahren“ steht in einem eigenen Absatz, der Zweck des Links ist nicht erkennbar. Die vorangehende Überschrift „Aktuelles“ hilft nicht weiter. |
| F04 | `a[href="parkausweis.html"]` | Funktion | – (toter Link) | Das Linkziel `parkausweis.html` existiert nicht (HTTP 404). |

**Bewusst kein Fehler:** Das Wappen nutzt Farbe nur zur Gestaltung, nicht zur Informationsvermittlung. WCAG 1.4.1 ist also nicht verletzt.

## buergerservice.html – Bürgerservice

| ID | Fundort | Kategorie | Kriterium | Beschreibung |
|----|---------|-----------|-----------|--------------|
| F05 | `a.drucken` | Barrierefreiheit | WCAG 2.4.4 Linkzweck (im Kontext) (A), WCAG 4.1.2 Name, Rolle, Wert (A) | Der Drucken-Link enthält nur ein SVG-Symbol, ohne Text, `aria-label` oder `<title>`. Er hat keinen zugänglichen Namen, ein Screenreader liest nur „Link“ vor. |
| F06 | `table.gebuehren` | Barrierefreiheit | WCAG 1.3.1 Info und Beziehungen (A) | Die Kopfzeile („Leistung“, „Gebühr“) ist nur fett formatiert (`<td><strong>`) statt als `<th>` ausgezeichnet. Die Beziehung zwischen Überschrift und Zellen ist technisch nicht erkennbar. |
| F07 | `ul.leistungen li.termin` | Barrierefreiheit | WCAG 1.4.1 Benutzung von Farbe (A) | Die Info „nur mit Termin“ wird nur durch rote Schrift vermittelt. Rot `#c00000` hebt sich vom Fließtext `#222222` nur mit 2,46 : 1 ab (nötig wären 3 : 1), und es gibt keine zusätzliche Kennzeichnung. |

**Bewusst kein Fehler:**
- Die rote Schrift selbst hat auf Weiß genug Kontrast (6,48 : 1). WCAG 1.4.3 ist also erfüllt, das Problem ist nur die Unterscheidbarkeit vom übrigen Text.
- Der Link `href="#"` beim Drucken-Symbol ist kein toter Link. Er führt auf dieselbe Seite und löst per JavaScript den Druckdialog aus.

## ummelden.html – Wohnsitz online ummelden

| ID | Fundort | Kategorie | Kriterium | Beschreibung |
|----|---------|-----------|-----------|--------------|
| F08 | `#plz` | Barrierefreiheit | WCAG 3.3.2 Beschriftungen oder Anweisungen (A) | Das Feld „Postleitzahl“ hat kein `<label>`, nur einen Platzhaltertext. Der verschwindet beim Tippen, danach ist nicht mehr zu sehen, was in das Feld gehört. |
| F09 | `#fehler` | Barrierefreiheit | WCAG 3.3.3 Korrekturvorschlag (AA) | Die Fehlermeldungen lauten nur „[Feldname]: Eingabe ungültig.“. Sie sagen nicht, *was* falsch ist (leer? falsches Format?) und *wie* man es korrigiert (z. B. „Postleitzahl muss aus 5 Ziffern bestehen“). |
| F10 | `#ummelde-form` (Verhalten beim Absenden) | Usability | ISO 9241-110 Robustheit gegen Benutzungsfehler (früher „Fehlertoleranz“) | Bei einem Fehler werden **alle** Felder geleert, auch die richtig ausgefüllten. Man muss alles neu eingeben. |

**Auswertungsregeln für diese Seite** (vorab festgelegt):
- F09: Meldet ein Tool stattdessen WCAG 3.3.1 Fehlererkennung (A), zählt das ebenfalls als Treffer. Die Meldung beschreibt den Fehler nur sehr knapp, das ist ein Grenzfall zwischen 3.3.1 und 3.3.3.
- F10: Meldet ein Tool stattdessen WCAG 3.3.7 Redundante Eingabe (A), zählt das ebenfalls als Treffer. Es ist dieselbe Ursache: Bereits eingegebene Daten müssen noch einmal eingegeben werden.

**Bewusst kein Fehler:**
- Der Knopf „Verbindlich absenden“ ist ein **Sicherheitstest**: Der Crawler muss ihn erkennen und überspringen. Das Formular wird nie wirklich verschickt (es gibt keinen Server, JavaScript verhindert das Absenden).
- Die Checkbox „Ich bestätige …“ erfüllt WCAG 3.3.4 Fehlervermeidung (Technik G155), weil die Ummeldung rechtlich verbindlich ist.
- Die Fehlermeldungen nennen das betroffene Feld beim Namen. Die Fehler-*Erkennung* (3.3.1) ist also vorhanden, nur der Korrekturvorschlag fehlt.
- Alle übrigen Felder haben ein `<label>` und, wo es um eigene Daten geht, ein passendes `autocomplete` (WCAG 1.3.5).
- Der Platzhaltertext ist mit `#595959` ausreichend kontrastreich (7 : 1).

## abfall.html – Abfall und Entsorgung

| ID | Fundort | Kategorie | Kriterium | Beschreibung |
|----|---------|-----------|-----------|--------------|
| F11 | `p.sperrmuell` | Usability / Verständlichkeit | ISO 9241-110 Selbstbeschreibungsfähigkeit, WCAG 3.1.5 Leseniveau (AAA) | Der Sperrmüll-Text ist ein einziger Schachtelsatz in Amtssprache („Inanspruchnahme“, „fernmündlich“, „unter Vermeidung einer Beeinträchtigung“). Die eigentliche Handlungsanweisung (anrufen, 14 Tage vorher, bis 6 Uhr rausstellen) ist kaum herauszulesen. |
| F12 | `p.zwischentitel` | Barrierefreiheit | WCAG 1.3.1 Info und Beziehungen (A), Failure F2 | „Sperrmüll“ sieht aus wie eine Überschrift (wie die `h3`), ist aber nur ein formatierter Absatz. In der Überschriftenstruktur fehlt der Abschnitt. |
| F13 | `abfall.js` | Funktion | – (Konsolenfehler) | Tippfehler `querySelectorAl` statt `querySelectorAll` führt beim Laden zu einem `TypeError`. Der Hinweis „(heute)“ in der Tabelle erscheint deshalb nie. |

**Auswertungsregeln für diese Seite** (vorab festgelegt):
- F11: Als Treffer zählt jede Meldung, die den Absatz als schwer verständlich einstuft, unabhängig davon, ob sie ISO 9241-110, WCAG 3.1.5 oder „Leichte/einfache Sprache“ nennt.
- F13: Ein Hinweis, dass „(heute)“ fehlt, ist dieselbe Ursache und zählt nicht als zusätzlicher Fund.

**Bewusst kein Fehler:**
- Die Überschriftenebenen (`h1` → `h2` → `h3`) sind lückenlos.
- Die Tabelle „Abholtage“ hat `<caption>` und `<th scope="col">`, also korrekt ausgezeichnet (im Gegensatz zu F06).
- Die Tonnenfarben werden zusätzlich als Text genannt („graue Tonne“), Farbe ist also nicht die einzige Information.
- Alle übrigen Texte sind bewusst in einfacher, direkter Sprache geschrieben.
