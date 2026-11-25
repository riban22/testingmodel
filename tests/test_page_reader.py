"""Tests für crawler/page_reader.py – geprüft wird an den Musterstadt-Seiten."""

from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from crawler.page_reader import get_links

# Ordner mit den Musterstadt-Seiten (relativ zu dieser Testdatei)
MUSTERSTADT = Path(__file__).parent.parent / "musterstadt"


@pytest.fixture(scope="module")
def browser():
    """Startet einmal einen Browser für alle Tests in dieser Datei."""
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


def open_page(page, filename):
    """Öffnet eine Musterstadt-Seite direkt als Datei (ohne Webserver)."""
    page.goto((MUSTERSTADT / filename).as_uri())


def test_get_links_startseite(page):
    open_page(page, "index.html")

    links = get_links(page)

    assert links == [
        {"text": "Startseite", "href": "index.html"},
        {"text": "Bürgerservice", "href": "buergerservice.html"},
        {"text": "Abfall und Entsorgung", "href": "abfall.html"},
        {"text": "Kontakt", "href": "kontakt.html"},
        {"text": "Mehr erfahren", "href": "parkausweis.html"},
    ]

def test_get_links_buergerservice(page):
    open_page(page, "buergerservice.html")

    links = get_links(page)

    assert links == [
        {"text": "Startseite", "href": "index.html"},
        {"text": "Bürgerservice", "href": "buergerservice.html"},
        {"text": "Abfall und Entsorgung", "href": "abfall.html"},
        {"text": "Kontakt", "href": "kontakt.html"},
        {"text": "", "href": "#"},
        {"text": "Wohnsitz online ummelden", "href": "ummelden.html"},
    ]