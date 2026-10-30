# Konfigurator ceny ilustracji: instrukcja

Plik do wklejenia: `konfigurator-wordpress.html` (wszystko w jednym pliku, bez wtyczek).

## Jak wkleić do WordPressa
1. Otwórz stronę (np. „Cennik”) w edytorze WordPressa.
2. Dodaj blok **„Własny HTML”** (ang. *Custom HTML*): kliknij „+” i wpisz „HTML”.
3. Skopiuj **całą** zawartość pliku `konfigurator-wordpress.html` i wklej do bloku.
4. Kliknij „Podgląd”, potem „Zaktualizuj / Opublikuj”.

Uwaga: blok musi wklejać administrator strony. Na darmowym planie WordPress.com skrypty są blokowane (tam konfigurator nie zadziała); na zwykłym hostingu z WordPressem działa.

## Jak zmienić ceny i teksty
Na samej górze pliku jest sekcja **USTAWIENIA** (`RK_CONFIG`):
- `kolejnaOsoba: 200` i `pupil: 150` – dopłaty za każdą kolejną osobę i każdego pupila.
- W `rodzaje` każdy rodzaj ilustracji ma `cena` (cena za `osobyWCenie` osób), `nazwa`, `opis` i listę `wCenie`.
  - Portret podstawowy: 650 zł za 1 osobę (+200 zł za każdą kolejną: 850, 1050, 1250…).
  - Portret z zainteresowaniami: 800 zł za 1 osobę (1000, 1200, 1400…).
  - Zestaw 3 ilustracji dla rodziców: 2500 zł; licznik pokazuje dodatkowe osoby (+200 zł każda).
- `wydruki` – cennik wydruków: `przesylka` (20 zł, doliczana raz) i lista `formaty` z ceną za `plotno` i `papier`.
- `maxOsob` / `maxPupili` – górny limit liczników.
- `poprawki` – tekst i lista poprawek w rozwijanym polu.

## Jak podmienić obrazki podglądu
W `obrazki` wpisz adres obrazka dla każdego rodzaju (`"podstawowy"`, `"zainteresowania"`, `"zestaw"`).
Możesz też dodać dokładniejsze klucze: `"podstawowy-2-1"` = portret podstawowy, 2 osoby, 1 pupil.
1. Wgraj ilustrację do **Media → Biblioteka**.
2. Kliknij ją → **Kopiuj adres URL**.
3. Wklej adres w cudzysłów, np. `"podstawowy": "https://twojastrona.pl/wp-content/uploads/portret.jpg"`.

Puste `""` = wyświetla się rysowany schemat. Najlepiej pionowe obrazki w proporcji ok. 3:4.
