"""Generuje statyczną makietę struktury strony do katalogu docs/ (GitHub Pages).

Makieta pokazuje tylko podstrony i sekcje z PROJEKT-dekoracja-ilustracja.md.
Brakujące treści są oznaczone [DO UZUPEŁNIENIA: ...]; nic nie jest wymyślone.

Uruchomienie: python3 makieta/generuj.py
"""

from html import escape
from pathlib import Path

WYJSCIE = Path(__file__).resolve().parent.parent / "docs"

MARKA = "dekoracja.ilustracja"
INSTAGRAM = "https://www.instagram.com/dekoracja.ilustracja/"


def brak(opis):
    return f"<mark>[DO UZUPEŁNIENIA: {escape(opis)}]</mark>"


def decyzja(opis):
    return f"<mark>[DO DECYZJI: {escape(opis)}]</mark>"


def akapit(tresc):
    return f"<p>{tresc}</p>"


def lista(elementy, numerowana=False):
    tag = "ol" if numerowana else "ul"
    pozycje = "".join(f"<li>{e}</li>" for e in elementy)
    return f"<{tag}>{pozycje}</{tag}>"


def faq(pytania):
    return "".join(f"<h3>{escape(p)}</h3><p>{brak('odpowiedź Oli')}</p>" for p in pytania)


FAQ_OGOLNE = [
    "Ile kosztuje?",
    "Ile wcześniej trzeba zarezerwować termin?",
    "Jakie zdjęcia są potrzebne? Czy mogą być z telefonu?",
    "Czy portret jest rysowany ręcznie, czy generowany przez AI?",
    "Czy dostanę plik, wydruk, czy oprawiony obraz? Jaki format?",
    "Ile kosztuje i ile trwa wysyłka? Czy wysyłacie za granicę?",
    "Ile poprawek jest w cenie?",
]

FAQ_LIVE = [
    "Ile kosztuje live painting na weselu?",
    "Ile trwa malowanie na weselu?",
    "Ilu gości zdążysz narysować?",
    "Czego potrzebujesz od sali?",
    "Ile kosztuje dojazd poza Lublin?",
]


def strona_uslugi(opis_akapitu, sekcje_wlasne, pytania=FAQ_OGOLNE, cta="Wyceń i zamów", cel="cennik/"):
    """Wspólny układ strony usługi: akapit, cena, sekcje, proces, galeria, opinie, FAQ, CTA."""
    return [
        ("Akapit otwierający", akapit(brak(opis_akapitu))),
        ("Cena", akapit("Cena od: " + brak("kwota w zł"))),
        *sekcje_wlasne,
        ("Jak wygląda zamówienie", lista([brak("kroki procesu")], numerowana=True)
         + akapit('<a href="{root}jak-zamowic/">Szczegóły: jak zamówić</a>')),
        ("Realizacje", akapit(brak("galeria realizacji z opisem (alt), tylko za zgodą klienta"))),
        ("Opinie", akapit(brak("opinie z datą i miastem, tylko za zgodą"))),
        ("Najczęstsze pytania", faq(pytania)),
        ("Zamówienie", akapit(f'<a class="cta" href="{{root}}{cel}">{escape(cta)}</a>')),
    ]


# (adres, nazwa w menu, H1, sekcje [(nagłówek H2, HTML)]). Adres "" = strona główna.
STRONY = [
    ("", "Start",
     f"{MARKA} – ręcznie rysowane portrety ślubne i na prezent | Ola Waniek, Lublin",
     [
         ("Kim jestem", akapit(brak("2–3 zdania: kim jest Ola, co robi, gdzie, za ile od"))),
         ("Oferta", lista([
             '<a href="{root}podziekowania-dla-rodzicow/">Podziękowania dla rodziców</a>',
             '<a href="{root}portret-slubny-ze-zdjecia/">Portret ślubny ze zdjęcia</a>',
             '<a href="{root}live-painting-na-weselu/">Live painting na weselu</a>',
             '<a href="{root}portret-na-prezent/">Portret na prezent</a>',
         ])),
         ("Jak zamówić", akapit(brak("skrót procesu") + ' <a href="{root}jak-zamowic/">Więcej</a>')),
         ("Opinie", akapit(brak("wybrane opinie") + ' <a href="{root}opinie/">Wszystkie opinie</a>')),
         ("Zamówienie", akapit('<a class="cta" href="{root}cennik/">Wyceń i zamów</a>')),
     ]),
    ("podziekowania-dla-rodzicow/", "Podziękowania dla rodziców",
     "Podziękowania dla rodziców",
     strona_uslugi("co, dla kogo, gdzie, za ile", [
         ("Pakiety", akapit(brak("pakiety i ich ceny"))),
         ("Stroje i szczegóły", akapit(brak("stroje z dnia ślubu i inne szczegóły"))),
         ("Terminy", lista([
             "Rezerwacja: " + brak("ile wcześniej"),
             "Przesłanie zdjęć: " + brak("do kiedy"),
         ])),
     ])),
    ("portret-slubny-ze-zdjecia/", "Portret ślubny",
     "Portret ślubny ze zdjęcia",
     strona_uslugi("co, dla kogo, gdzie, za ile", [
         ("Warianty", lista([
             "Portret pary: " + brak("opis"),
             "Portret na rocznicę: " + brak("opis"),
             "Odtworzenie starego zdjęcia ślubnego: " + brak("opis"),
         ])),
     ])),
    ("live-painting-na-weselu/", "Live painting",
     "Live painting na weselu",
     strona_uslugi("co dokładnie robi Ola na weselu, gdzie, za ile", [
         ("Jak to wygląda", akapit(brak("technika: tablet z wydrukiem czy media tradycyjne"))),
         ("Godziny i liczba portretów", akapit(brak("godziny obecności, liczba portretów"))),
         ("Zasięg i dojazd", akapit(brak("Lublin i okolice, dopłata za dojazd"))),
         ("Wymagania od sali", akapit(brak("stolik, gniazdko, inne"))),
     ], pytania=FAQ_LIVE, cta="Zapytaj o termin", cel="kontakt/")),
    ("portret-na-prezent/", "Portret na prezent",
     "Portret na prezent",
     strona_uslugi("co, dla kogo, gdzie, za ile; ręcznie rysowany, nie AI", [
         ("Okazje", akapit(brak("urodziny, rocznice, Dzień Matki i inne"))),
         ("Ręcznie rysowany, nie AI", akapit(brak("czym różni się od portretu generowanego przez AI"))),
     ])),
    ("cennik/", "Cennik",
     "Cennik",
     [
         ("Konfigurator ceny", akapit(brak(
             "konfigurator: klient wybiera opcje i widzi cenę, potem wysyła Oli zamówienie lub zapytanie "
             "z wybranymi opcjami; pole „Skąd Pani o mnie wie?” z opcją „ChatGPT/AI”"))),
         ("Ceny", akapit(brak("tabela cen w HTML z tych samych danych co konfigurator: "
                              "warianty, dopłaty, wydruki, wysyłka; ceny 2027"))),
         ("Co dalej", akapit("Ola odpowiada na każde zamówienie lub zapytanie: " + brak("w jakim czasie i jak"))),
     ]),
    ("jak-zamowic/", "Jak zamówić",
     "Jak zamówić",
     [
         ("Krok po kroku", lista([
             'Wybór opcji w <a href="{root}cennik/">konfiguratorze</a> i wysłanie zamówienia lub zapytania',
             "Kontakt od Oli: " + brak("w jakim czasie i jak"),
             "Rezerwacja terminu: " + brak("opis"),
             "Umowa: " + brak("opis"),
             "Kwestionariusz: " + brak("opis"),
             "Zdjęcia: " + brak("opis"),
             "Szkic do akceptacji: " + brak("opis"),
             "Poprawki: " + brak("ile w cenie"),
             "Plik lub wydruk: " + brak("opis"),
             "Wysyłka: " + brak("kurier, czas, opakowanie"),
             "Płatność: " + brak("opis"),
         ], numerowana=True)),
     ]),
    ("opinie/", "Opinie",
     "Opinie",
     [("Opinie klientów", akapit(brak("opinie z datą i miastem, tylko za zgodą")))]),
    ("o-mnie/", "O mnie",
     "O mnie",
     [
         ("Ola Waniek", akapit(brak("wykształcenie, doświadczenie, liczba portretów, technika, Lublin"))),
         ("Przy pracy", akapit(brak("zdjęcie Oli przy pracy z opisem"))),
     ]),
    ("blog/", "Blog",
     "Blog",
     [("Wpisy", akapit(brak("2–4 poradniki na start")))]),
    ("kontakt/", "Kontakt",
     "Kontakt",
     [
         ("Dane kontaktowe", lista([
             "E-mail: " + brak("e-mail w domenie marki"),
             "Telefon: " + brak("telefon"),
             "Pracownia: Lublin, wysyłka w całej Polsce",
         ])),
         ("Formularz", akapit(decyzja("osobny formularz kontaktowy (np. live painting) czy tylko e-mail i telefon"))),
     ]),
    ("regulamin/", None,
     "Regulamin",
     [("Treść", akapit(brak("regulamin zweryfikowany przez prawnika")))]),
    ("polityka-prywatnosci/", None,
     "Polityka prywatności",
     [("Treść", akapit(brak("polityka prywatności zweryfikowana przez prawnika")))]),
]

STYL = """
body{font-family:system-ui,sans-serif;line-height:1.5;max-width:60rem;margin:0 auto;padding:0 1rem;color:#222;background:#fff}
.uwaga{background:#222;color:#fff;padding:.5rem 1rem;margin:0 -1rem}
nav ul{display:flex;flex-wrap:wrap;gap:.25rem 1rem;list-style:none;padding:0}
a{color:#0645ad}
[aria-current=page]{font-weight:bold}
mark{background:#fff3b0;color:#222}
.cta{display:inline-block;border:2px solid #222;padding:.5rem 1rem;text-decoration:none;color:#222}
footer{border-top:1px solid #ccc;margin-top:2rem;padding:1rem 0}
:focus-visible{outline:3px solid #0645ad;outline-offset:2px}
"""


def menu(root, biezacy):
    pozycje = []
    for adres, nazwa, _, _ in STRONY:
        if nazwa is None:
            continue
        aktywna = ' aria-current="page"' if adres == biezacy else ""
        pozycje.append(f'<li><a href="{root}{adres}"{aktywna}>{escape(nazwa)}</a></li>')
    return f'<nav aria-label="Główne menu"><ul>{"".join(pozycje)}</ul></nav>'


def stopka(root):
    return (
        "<footer>"
        f"<p><strong>{MARKA} – Ola Waniek</strong><br>"
        "Pracownia: Lublin. Wysyłka w całej Polsce.<br>"
        "DEKOLU Aleksandra Waniek, " + brak("adres rejestrowy, NIP") + "<br>"
        "E-mail: " + brak("e-mail") + ", telefon: " + brak("telefon") + "</p>"
        f'<p><a href="{INSTAGRAM}">Instagram</a> · '
        f'<a href="{root}regulamin/">Regulamin</a> · '
        f'<a href="{root}polityka-prywatnosci/">Polityka prywatności</a></p>'
        "</footer>"
    )


def renderuj(adres, h1, sekcje):
    root = "../" if adres else ""
    tytul = h1 if not adres else f"{h1} | {MARKA}"
    tresc = "".join(f"<section><h2>{escape(n)}</h2>{h.format(root=root)}</section>" for n, h in sekcje)
    return (
        "<!doctype html>\n"
        '<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        f"<title>{escape(tytul)}</title>\n<style>{STYL}</style>\n</head>\n<body>\n"
        '<p class="uwaga">Makieta struktury strony. Bez grafik i bez ostatecznych treści.</p>\n'
        f'<header><p><a href="{root}">{MARKA}</a></p>{menu(root, adres)}</header>\n'
        f"<main><h1>{escape(h1)}</h1>{tresc}</main>\n"
        f"{stopka(root)}\n</body>\n</html>\n"
    )


def generuj(katalog=WYJSCIE):
    for adres, _, h1, sekcje in STRONY:
        plik = Path(katalog) / adres / "index.html"
        plik.parent.mkdir(parents=True, exist_ok=True)
        plik.write_text(renderuj(adres, h1, sekcje), encoding="utf-8")


if __name__ == "__main__":
    generuj()
    print(f"Wygenerowano {len(STRONY)} stron w {WYJSCIE}")
