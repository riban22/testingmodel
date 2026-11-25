"""Aktionen auf einer Seite: klicken und tippen – mit Sicherheitsregel.

Sicherheitsregel aus der CLAUDE.md:
Aktionen wie "Löschen", "Bezahlen", "Verbindlich absenden" werden erkannt
und standardmäßig übersprungen.
"""

from playwright.sync_api import Locator, Page

from crawler.page_reader import element_text

# Wortteile, die auf eine folgenreiche Aktion hindeuten (alles kleingeschrieben).
# Es reicht, wenn einer davon IRGENDWO in der Beschriftung vorkommt:
# "senden" passt also auch auf "Absenden" und "Verbindlich absenden".
DANGEROUS_WORDS = [
    "senden",      # absenden, versenden
    "verbindlich",
    "löschen",
    "entfernen",
    "bezahlen",
    "zahlen",
    "kaufen",
    "bestellen",
    "buchen",
    "kündigen",
    "beantragen",
    "anfordern",
    "abmelden",
]


def is_dangerous(text: str) -> bool:
    """True, wenn die Beschriftung nach einer folgenreichen Aktion klingt."""
    text = text.lower()
    return any(word in text for word in DANGEROUS_WORDS)


def safe_click(element: Locator, allow_dangerous: bool = False) -> bool:
    """Klickt auf ein Element – außer die Aktion ist gefährlich.

    Gibt True zurück, wenn geklickt wurde, sonst False.
    Mit allow_dangerous=True kann man die Sperre bewusst aufheben
    (nur für die eigene Test-Website gedacht).
    """
    text = element_text(element)

    if is_dangerous(text) and not allow_dangerous:
        print(f"Übersprungen (gefährliche Aktion): {text!r}")
        return False

    element.click()
    return True


def fill_input(page: Page, name: str, value: str) -> None:
    """Tippt einen Wert in das Eingabefeld mit dem angegebenen name-Attribut."""
    page.locator(f"[name='{name}']").fill(value)
