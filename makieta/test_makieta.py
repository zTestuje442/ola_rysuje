"""Testy makiety. Uruchomienie: python3 -m unittest discover makieta"""

import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path

import generuj

DOCS = generuj.WYJSCIE


class Parser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.h1 = 0
        self.linki = []
        self.meta = {}
        self.lang = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "h1":
            self.h1 += 1
        elif tag == "a":
            self.linki.append(a.get("href", ""))
        elif tag == "meta" and "name" in a:
            self.meta[a["name"]] = a.get("content")
        elif tag == "html":
            self.lang = a.get("lang")


def strony():
    return sorted(DOCS.rglob("index.html"))


def parsuj(plik):
    p = Parser()
    p.feed(plik.read_text(encoding="utf-8"))
    return p


class TestMakieta(unittest.TestCase):
    def test_docs_zgodne_z_generatorem(self):
        with tempfile.TemporaryDirectory() as tmp:
            generuj.generuj(tmp)
            nowe = {p.relative_to(tmp): p.read_text(encoding="utf-8") for p in Path(tmp).rglob("index.html")}
        obecne = {p.relative_to(DOCS): p.read_text(encoding="utf-8") for p in strony()}
        self.assertEqual(nowe, obecne, "docs/ nieaktualne: uruchom python3 makieta/generuj.py")

    def test_kazda_strona_z_planu_istnieje(self):
        for adres, *_ in generuj.STRONY:
            self.assertTrue((DOCS / adres / "index.html").is_file(), adres)

    def test_jeden_h1_noindex_lang(self):
        for plik in strony():
            p = parsuj(plik)
            self.assertEqual(p.h1, 1, plik)
            self.assertEqual(p.meta.get("robots"), "noindex, nofollow", plik)
            self.assertEqual(p.lang, "pl", plik)

    def test_linki_wewnetrzne_dzialaja(self):
        for plik in strony():
            for href in parsuj(plik).linki:
                if href.startswith("https://"):
                    continue
                cel = (plik.parent / href).resolve() / "index.html"
                self.assertTrue(cel.is_file(), f"{plik}: {href}")

    def test_brak_wypelniaczy_i_nazwy_roboczej(self):
        for plik in strony():
            tekst = plik.read_text(encoding="utf-8").lower()
            for zakazane in ("lorem", "ipsum", "ola_rysuje", "ola rysuje"):
                self.assertNotIn(zakazane, tekst, plik)


if __name__ == "__main__":
    unittest.main()
