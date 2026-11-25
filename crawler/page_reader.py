"""Liest Elemente einer geöffneten Seite aus: Links, (später) Buttons und Eingabefelder."""

from playwright.sync_api import Page


def get_links(page: Page) -> list[dict]:
    """Gibt alle Links der Seite zurück, jeweils mit Text und Ziel.

    Beispiel für ein Ergebnis:
    [{"text": "Startseite", "href": "index.html"}, ...]
    """
    links = []

    # Locator = "Suchanfrage" nach Elementen; .all() liefert jedes gefundene Element einzeln
    for link in page.locator("a").all():
        links.append({
            "text": link.inner_text().strip(),   # sichtbarer Linktext ohne Leerzeichen am Rand
            "href": link.get_attribute("href"),  # Linkziel genau so, wie es im HTML steht
        })

    return links
