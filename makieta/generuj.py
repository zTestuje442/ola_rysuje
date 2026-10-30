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


ZDANIE_MARKI = "Ręcznie rysowane podziękowania dla rodziców i portrety ze zdjęcia. Lublin, wysyłka w całej Polsce."


def strona(adres, menu, title, meta, sekcje, h1=None):
    """H1 domyślnie = title bez nazwy marki. menu=None: strona tylko w stopce."""
    return (adres, menu, title, meta, h1 or title.removesuffix(f" | {MARKA}"), sekcje)


# Title (do ok. 60 znaków) i meta (do ok. 155) wg mapy fraz z 30.10.2026.
# [w nawiasach] = do potwierdzenia przez Olę. Adres "" = strona główna.
STRONY = [
    strona("", "Start",
           f"Podziękowania dla rodziców i portrety | {MARKA}",
           "Ręcznie rysowane podziękowania dla rodziców, portrety ślubne i portrety z pasjami ze zdjęcia. "
           "Ola Waniek, Lublin. Wysyłka w całej Polsce, 51 opinii 5,0.",
           [
               ("Kim jestem", akapit(escape(ZDANIE_MARKI) + " "
                                     + brak("reszta akapitu: kim jest Ola, co robi, za ile od"))),
               ("Oferta", lista([
                   '<a href="{root}podziekowania-dla-rodzicow/">Podziękowania dla rodziców</a>',
                   '<a href="{root}portret-z-zainteresowaniami/">Portret z zainteresowaniami</a>',
                   '<a href="{root}portret-ze-zdjecia/">Portret ze zdjęcia</a>',
                   '<a href="{root}portret-slubny-pary-mlodej/">Portret ślubny pary młodej</a>',
                   '<a href="{root}live-painting-na-weselu/">Live painting na weselu</a>',
                   '<a href="{root}ilustracje-dla-firm/">Ilustracje dla firm</a>',
               ])),
               ("Jak zamówić", akapit(brak("skrót procesu") + ' <a href="{root}jak-zamowic/">Więcej</a>')),
               ("Opinie", akapit(brak("wybrane opinie") + ' <a href="{root}opinie/">Wszystkie opinie</a>')),
               ("Zamówienie", akapit('<a class="cta" href="{root}cennik/">Wyceń i zamów</a>')),
           ],
           h1=f"{MARKA} – ręcznie rysowane podziękowania dla rodziców i portrety ze zdjęcia | Ola Waniek, Lublin"),
    strona("podziekowania-dla-rodzicow/", "Podziękowania dla rodziców",
           f"Podziękowania dla rodziców na wesele | {MARKA}",
           "Ręcznie rysowane portrety rodziców w strojach z Waszego ślubu. Zestaw [liczba] ilustracji "
           "od [cena] zł, wysyłka w całej Polsce. Zarezerwuj termin.",
           strona_uslugi("co, dla kogo, gdzie, za ile", [
               ("Pakiety", akapit(brak("pakiety i ich ceny"))),
               ("Stroje i szczegóły", akapit(brak("stroje z dnia ślubu i inne szczegóły"))),
               ("Terminy", lista([
                   "Rezerwacja: " + brak("ile wcześniej"),
                   "Przesłanie zdjęć: " + brak("do kiedy"),
               ])),
           ])),
    strona("portret-z-zainteresowaniami/", "Portret z zainteresowaniami",
           f"Portret z zainteresowaniami na prezent | {MARKA}",
           "Ręcznie rysowany portret ze zdjęcia z pasjami, pracą i ulubionym zwierzakiem. "
           "Prezent na urodziny i rocznicę od [cena] zł, wysyłka w całej Polsce.",
           strona_uslugi("co, dla kogo, gdzie, za ile", [
               ("Co może być w tle", akapit(brak("pasje, praca, zwierzak i inne"))),
               ("Okazje", akapit(brak("urodziny, rocznice i inne"))),
               ("Ręcznie rysowany, nie AI", akapit(brak("czym różni się od portretu generowanego przez AI"))),
           ])),
    strona("portret-ze-zdjecia/", "Portret ze zdjęcia",
           f"Portret ze zdjęcia na zamówienie | {MARKA}",
           "Portret osoby, pary lub rodziny rysowany ręcznie na tablecie graficznym, to nie filtr ani AI. "
           "Od [cena] zł, realizacja ok. [X] tyg., wysyłka w Polsce.",
           strona_uslugi("co, dla kogo, gdzie, za ile", [
               ("Kogo rysuję", akapit(brak("osoba, para, rodzina; liczba osób"))),
               ("Ręcznie, nie filtr ani AI", akapit(brak("jak powstaje portret na tablecie graficznym"))),
               ("Czas realizacji", akapit(brak("ile tygodni"))),
           ])),
    strona("portret-slubny-pary-mlodej/", "Portret ślubny",
           f"Portret ślubny pary młodej ze zdjęcia | {MARKA}",
           "Ilustracja pary młodej na pamiątkę ślubu, rocznicę lub jako prezent ślubny. "
           "Rysowana ręcznie ze zdjęcia, od [cena] zł. Pracownia w Lublinie, wysyłka w Polsce.",
           strona_uslugi("co, dla kogo, gdzie, za ile", [
               ("Warianty", lista([
                   "Pamiątka ślubu: " + brak("opis"),
                   "Na rocznicę: " + brak("opis"),
                   "Prezent ślubny: " + brak("opis"),
                   "Odtworzenie starego zdjęcia ślubnego: " + brak("opis"),
               ])),
           ])),
    strona("live-painting-na-weselu/", "Live painting",
           f"Live painting na weselu, Lublin | {MARKA}",
           "Maluję na żywo podczas Waszego wesela – goście widzą, jak powstaje pamiątka. "
           "Lublin i okolice, dojazd w całej Polsce. Sprawdź wolne terminy na 2027.",
           strona_uslugi("co dokładnie robi Ola na weselu, gdzie, za ile", [
               ("Status oferty", akapit(decyzja("strona tylko jeśli Ola potwierdzi, że robi live painting"))),
               ("Jak to wygląda", akapit(brak("technika: tablet z wydrukiem czy media tradycyjne"))),
               ("Godziny i liczba portretów", akapit(brak("godziny obecności, liczba portretów"))),
               ("Zasięg i dojazd", akapit(brak("Lublin i okolice, dopłata za dojazd"))),
               ("Wymagania od sali", akapit(brak("stolik, gniazdko, inne"))),
           ], pytania=FAQ_LIVE, cta="Zapytaj o termin", cel="kontakt/")),
    strona("ilustracje-dla-firm/", "Ilustracje dla firm",
           f"Ilustracje dla firm na zamówienie | {MARKA}",
           "Ilustracje do książek, materiałów reklamowych i na tekstylia oraz postacie dla marek. "
           "Graficzka z 8-letnim doświadczeniem, Lublin. Zapytaj o wycenę.",
           [
               ("Status oferty", akapit(decyzja("czy Ola chce pokazywać ofertę dla firm na stronie"))),
               ("Zakres", akapit(brak("ilustracje do książek, reklam, na tekstylia, postacie dla marek"))),
               ("Realizacje", akapit(brak("wybrane prace dla firm, tylko za zgodą klienta"))),
               ("Wycena", akapit('<a class="cta" href="{root}kontakt/">Zapytaj o wycenę</a>')),
           ]),
    strona("cennik/", "Cennik",
           f"Cennik portretów i podziękowań | {MARKA}",
           "Aktualne ceny 2027: podziękowania dla rodziców, portrety ze zdjęcia, z zainteresowaniami i ślubne, "
           "live painting. Formaty, czas realizacji i koszt wysyłki.",
           [
               ("Konfigurator ceny", akapit(brak(
                   "konfigurator: klient wybiera opcje i widzi cenę, potem wysyła Oli zamówienie lub zapytanie "
                   "z wybranymi opcjami; pole „Skąd Pani o mnie wie?” z opcją „ChatGPT/AI”"))),
               ("Ceny", akapit(brak("tabela cen w HTML z tych samych danych co konfigurator: "
                                    "warianty, dopłaty, wydruki, wysyłka; ceny 2027"))),
               ("Co dalej", akapit("Ola odpowiada na każde zamówienie lub zapytanie: " + brak("w jakim czasie i jak"))),
           ]),
    strona("jak-zamowic/", "Jak zamówić",
           f"Jak zamówić portret z wysyłką | {MARKA}",
           "Od zdjęcia do gotowej ilustracji: rezerwacja terminu, przesłanie zdjęć, szkic do akceptacji, "
           "poprawki i wysyłka w całej Polsce. Sprawdź, jak to wygląda.",
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
    strona("opinie/", "Opinie",
           f"Opinie o portretach i podziękowaniach | {MARKA}",
           "Co mówią pary młode i rodzice o ilustracjach Oli? Ponad 50 opinii ze średnią 5,0 "
           "i zdjęcia gotowych prac z wręczenia podziękowań.",
           [("Opinie klientów", akapit(brak("opinie z datą i miastem, tylko za zgodą")))]),
    strona("o-mnie/", "O mnie",
           f"Ola Waniek – ilustratorka z Lublina | {MARKA}",
           "Jestem Ola, ilustratorka i graficzka. Od [rok] r. rysuję portrety i podziękowania dla rodziców – "
           "ponad [1000/1200] prac. Pracownia w Lublinie.",
           [
               ("Ola Waniek", akapit(brak("wykształcenie, doświadczenie, liczba portretów, technika, Lublin"))),
               ("Przy pracy", akapit(brak("zdjęcie Oli przy pracy z opisem"))),
           ]),
    strona("blog/", "Blog",
           f"Blog o portretach i podziękowaniach | {MARKA}",
           "Poradniki o ręcznie rysowanych portretach i podziękowaniach dla rodziców: pomysły, ceny, "
           "wybór zdjęcia i live painting na weselu.",
           [("Planowane wpisy", lista([
               "Podziękowania dla rodziców na wesele – pomysły i ceny 2027",
               "Czym jest live painting na weselu i ile kosztuje?",
               "Jak wybrać zdjęcie do portretu na zamówienie?",
           ]))]),
    strona("kontakt/", "Kontakt",
           f"Kontakt i rezerwacja terminu | {MARKA}",
           "Napisz, jaki portret chcesz zamówić i na kiedy. Odpowiadam w ciągu [X] dni. "
           "Lublin, wysyłka w całej Polsce, live painting na weselach.",
           [
               ("Dane kontaktowe", lista([
                   "E-mail: " + brak("e-mail w domenie marki"),
                   "Telefon: " + brak("telefon"),
                   "Pracownia: Lublin, wysyłka w całej Polsce",
               ])),
               ("Formularz", akapit(decyzja("osobny formularz kontaktowy (np. live painting) czy tylko e-mail i telefon"))),
           ]),
    strona("regulamin/", None, f"Regulamin | {MARKA}", f"Regulamin zamówień {MARKA}.",
           [("Treść", akapit(brak("regulamin zweryfikowany przez prawnika")))]),
    strona("polityka-prywatnosci/", None, f"Polityka prywatności | {MARKA}", f"Polityka prywatności {MARKA}.",
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
    for adres, nazwa, *_ in STRONY:
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


def renderuj(adres, title, meta, h1, sekcje):
    root = "../" if adres else ""
    tresc = "".join(f"<section><h2>{escape(n)}</h2>{h.format(root=root)}</section>" for n, h in sekcje)
    return (
        "<!doctype html>\n"
        '<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="robots" content="noindex, nofollow">\n'
        f"<title>{escape(title)}</title>\n"
        f'<meta name="description" content="{escape(meta)}">\n'
        f"<style>{STYL}</style>\n</head>\n<body>\n"
        '<p class="uwaga">Makieta struktury strony. Bez grafik i bez ostatecznych treści.</p>\n'
        f'<header><p><a href="{root}">{MARKA}</a></p>{menu(root, adres)}</header>\n'
        f"<main><h1>{escape(h1)}</h1>{tresc}</main>\n"
        f"{stopka(root)}\n</body>\n</html>\n"
    )


def generuj(katalog=WYJSCIE):
    for adres, _, title, meta, h1, sekcje in STRONY:
        plik = Path(katalog) / adres / "index.html"
        plik.parent.mkdir(parents=True, exist_ok=True)
        plik.write_text(renderuj(adres, title, meta, h1, sekcje), encoding="utf-8")


if __name__ == "__main__":
    generuj()
    print(f"Wygenerowano {len(STRONY)} stron w {WYJSCIE}")
