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


def get_buttons(page: Page) -> list[dict]:
    """Gibt alle Buttons der Seite zurück, jeweils mit Text und Typ.

    Gefunden werden nur Elemente, die technisch als Button erkennbar sind:
    <button>, <input type="submit"/"button"> und Elemente mit role="button".
    Ein <div>, der nur per JavaScript klickbar ist, wird NICHT gefunden.

    Beispiel für ein Ergebnis:
    [{"text": "Verbindlich absenden", "type": "submit"}, ...]
    """
    buttons = []
    selector = "button, input[type='submit'], input[type='button'], [role='button']"

    for button in page.locator(selector).all():
        # Bei <input> steht die Beschriftung im Attribut "value", sonst als Text im Element
        tag = button.evaluate("element => element.tagName.toLowerCase()")
        if tag == "input":
            text = button.get_attribute("value") or ""
        else:
            text = button.inner_text().strip()

        buttons.append({
            "text": text,
            "type": button.get_attribute("type"),  # z. B. "submit" = schickt ein Formular ab
        })

    return buttons
