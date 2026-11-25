"""Phase 0: Erstes Playwright-Skript.

Öffnet eine Seite in Chromium, gibt den Seitentitel aus
und speichert einen Screenshot.
"""

from pathlib import Path

from playwright.sync_api import sync_playwright

# example.com ist offiziell für Beispiele reserviert – wir rufen sie nur einmal lesend auf
URL = "https://example.com"
OUTPUT_FILE = Path("screenshots") / "example.png"


def take_screenshot(url: str, output_file: Path) -> None:
    """Öffnet die Seite und speichert einen Screenshot."""
    # Zielordner anlegen, falls er noch nicht existiert
    output_file.parent.mkdir(exist_ok=True)

    # "with" sorgt dafür, dass Playwright am Ende sauber beendet wird
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Browser starten (unsichtbar = "headless")
        page = browser.new_page()      # neuen Tab öffnen
        page.goto(url)                 # Seite laden
        print("Titel der Seite:", page.title())
        page.screenshot(path=output_file, full_page=True)
        browser.close()

    print("Screenshot gespeichert:", output_file)


# Wird nur ausgeführt, wenn man die Datei direkt startet
# (nicht, wenn sie später von einer anderen Datei importiert wird)
if __name__ == "__main__":
    take_screenshot(URL, OUTPUT_FILE)
