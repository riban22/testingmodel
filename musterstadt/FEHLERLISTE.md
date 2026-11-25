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
