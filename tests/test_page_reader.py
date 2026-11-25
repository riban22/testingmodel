"""Tests für crawler/page_reader.py – geprüft wird an den Musterstadt-Seiten."""

from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from crawler.page_reader import get_buttons, get_inputs, get_links

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
        {"text": "", "href": "#"},  # Drucker-Symbol ohne Text (F05)
        {"text": "Wohnsitz online ummelden", "href": "ummelden.html"},
    ]


def test_get_buttons_ummelden(page):
    open_page(page, "ummelden.html")

    buttons = get_buttons(page)

    assert buttons == [
        {"text": "Verbindlich absenden", "type": "submit"},
    ]


def test_get_buttons_kontakt_findet_div_button_nicht(page):
    open_page(page, "kontakt.html")

    buttons = get_buttons(page)

    # "Rückruf anfordern" ist nur ein <div> (F14) und wird deshalb NICHT gefunden
    assert buttons == []


def test_get_inputs_kontakt(page):
    open_page(page, "kontakt.html")

    inputs = get_inputs(page)

    assert inputs == [
        {"name": "name", "type": "text", "label": "Name",
         "placeholder": None, "required": True},
        {"name": "telefon", "type": "tel", "label": "Telefonnummer",
         "placeholder": None, "required": True},
    ]


def test_get_inputs_ummelden_plz_ohne_label(page):
    open_page(page, "ummelden.html")

    inputs = get_inputs(page)

    # Die Namen aller Felder, in der Reihenfolge auf der Seite
    names = [field["name"] for field in inputs]
    assert names == ["vorname", "nachname", "geburtsdatum", "strasse",
                     "plz", "ort", "einzugsdatum", "bestaetigt"]

    # Das PLZ-Feld hat kein Label, nur einen Platzhalter (F08)
    plz = inputs[names.index("plz")]
    assert plz["label"] is None
    assert plz["placeholder"] == "Postleitzahl"

    # Alle anderen Felder haben ein Label
    for field in inputs:
        if field["name"] != "plz":
            assert field["label"], f"Feld {field['name']} hat kein Label"