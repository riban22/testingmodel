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


# JavaScript, das im Browser läuft: holt den Text des zugehörigen <label>.
# element.labels enthält alle Labels, die per for="..." mit dem Feld verbunden sind.
_LABEL_SCRIPT = """
element => {
    if (element.labels && element.labels.length > 0) {
        return element.labels[0].innerText.trim();
    }
    return null;
}
"""


def get_inputs(page: Page) -> list[dict]:
    """Gibt alle Eingabefelder der Seite zurück, mit Beschriftung und Eigenschaften.

    Buttons (<input type="submit"> usw.) und versteckte Felder zählen nicht dazu.

    Beispiel für ein Ergebnis:
    [{"name": "vorname", "type": "text", "label": "Vorname",
      "placeholder": None, "required": True}, ...]
    """
    inputs = []
    selector = (
        "input:not([type='submit']):not([type='button']):not([type='hidden']),"
        " select, textarea"
    )

    for field in page.locator(selector).all():
        inputs.append({
            "name": field.get_attribute("name"),
            "type": field.get_attribute("type"),
            "label": field.evaluate(_LABEL_SCRIPT),           # None = kein Label vorhanden
            "placeholder": field.get_attribute("placeholder"),  # grauer Text im leeren Feld
            "required": field.get_attribute("required") is not None,  # Pflichtfeld?
        })

    return inputs
