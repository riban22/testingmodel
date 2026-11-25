"""Tests für crawler/actions.py – klicken, tippen und die Sicherheitsregel."""

import pytest

from crawler.actions import fill_input, is_dangerous, safe_click


# parametrize = derselbe Test läuft mehrmals mit verschiedenen Werten
@pytest.mark.parametrize("text", [
    "Verbindlich absenden",
    "Absenden",
    "Konto löschen",
    "Jetzt bezahlen",
    "Rückruf anfordern",
])
def test_is_dangerous_erkennt_gefaehrliche_aktionen(text):
    assert is_dangerous(text) is True


@pytest.mark.parametrize("text", [
    "Startseite",
    "Mehr erfahren",
    "Wohnsitz online ummelden",
    "Abfall und Entsorgung",
    "",
])
def test_is_dangerous_laesst_harmlose_aktionen_zu(text):
    assert is_dangerous(text) is False


def test_safe_click_folgt_harmlosem_link(open_page):
    page = open_page("index.html")

    clicked = safe_click(page.get_by_role("link", name="Bürgerservice"))

    assert clicked is True
    assert page.url.endswith("buergerservice.html")


def test_safe_click_ueberspringt_verbindlich_absenden(open_page):
    page = open_page("ummelden.html")

    clicked = safe_click(page.get_by_role("button", name="Verbindlich absenden"))

    assert clicked is False
    # Beweis, dass wirklich nichts passiert ist: keine Fehlermeldung, keine Bestätigung
    assert page.locator("#fehler").inner_text() == ""
    assert page.locator("#erfolg").inner_text() == ""


def test_fill_input_tippt_in_feld(open_page):
    page = open_page("kontakt.html")

    fill_input(page, "name", "Erika Mustermann")

    assert page.locator("[name='name']").input_value() == "Erika Mustermann"
