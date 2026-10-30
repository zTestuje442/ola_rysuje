# dekoracja.ilustracja – strona www

Repozytorium strony dekoracja.ilustracja (Ola Waniek, Lublin). Nazwa repozytorium `ola_rysuje` jest robocza.

## Makieta struktury (podgląd online)

`docs/` to statyczna makieta podstron z planu (`PROJEKT-dekoracja-ilustracja.md`), bez grafik i ostatecznych treści. Braki oznaczone są `[DO UZUPEŁNIENIA: ...]`, sprawy otwarte `[DO DECYZJI: ...]`. Każda strona ma `noindex`.

- Edycja: zmień `makieta/generuj.py`, potem `python3 makieta/generuj.py` (nie edytuj `docs/` ręcznie).
- Testy: `python3 -m unittest discover -s makieta`.
- Podgląd lokalny: `python3 -m http.server -d docs` i http://localhost:8000.
- Podgląd online: GitHub Pages z gałęzi `staging`, katalog `/docs`.

## Gałęzie

`main` = produkcja, `staging` = podgląd. Zmiany na `feature/*` → PR do `staging` → po testach PR `staging` → `main`.
