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
