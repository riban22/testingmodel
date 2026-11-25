"""Gemeinsame Vorbereitung für alle Tests.

pytest lädt diese Datei automatisch. Alles, was hier als Fixture steht,
können alle Testdateien im Ordner tests/ benutzen, ohne es zu importieren.
"""

from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

# Ordner mit den Musterstadt-Seiten
MUSTERSTADT = Path(__file__).parent.parent / "musterstadt"


@pytest.fixture(scope="session")
def browser():
    """Startet einmal einen Browser für alle Tests."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser  # hier laufen die Tests
        browser.close()


@pytest.fixture
def page(browser):
    """Gibt jedem Test einen frischen Tab."""
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def open_page(page):
    """Öffnet eine Musterstadt-Seite direkt als Datei (ohne Webserver).

    Benutzung im Test: open_page("index.html")
    """
    def _open(filename):
        page.goto((MUSTERSTADT / filename).as_uri())
        return page
    return _open
