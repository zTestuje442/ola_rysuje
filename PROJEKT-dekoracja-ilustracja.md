# Projekt: strona www dla dekoracja.ilustracja (Ola Waniek)

Kontekst zebrany w rozmowie z Claude (claude.ai, 30.10.2026). Plik do pamięci projektu w Claude Code.

## 0. Zasady pracy dla Claude Code (czytaj najpierw)

- Nie wymyślaj treści. Wszystkie teksty, ceny, opinie, liczby i realizacje pochodzą od Oli. Gdy czegoś brakuje, wstaw jawny znacznik `[DO UZUPEŁNIENIA: ...]`, nie lorem ipsum ani zmyślone dane.
- Treść musi być w HTML renderowanym po stronie serwera. FAQ, cennik i akapity otwierające nie mogą być doładowywane przez JS, ukryte w grafikach ani w zakładkach ładowanych skryptem.
- Jedno źródło prawdy: dane edytowane w polach panelu zasilają jednocześnie widok i JSON-LD.
- Pola rejestrowane w kodzie (PHP albo acf-json w repozytorium), nie klikane w panelu.
- Zmiany chirurgiczne, minimalny kod, bez spekulacyjnych funkcji.
- Każdy krok kończy się weryfikacją w formacie: [Krok] → weryfikacja: [sprawdzenie].

## 1. Klientka i biznes

- **Marka:** dekoracja.ilustracja. Osoba: Ola (Aleksandra) Waniek. Instagram: https://www.instagram.com/dekoracja.ilustracja/ (ok. 10 tys. obserwujących).
- **Nazwa prawna (wg rejestrów):** DEKOLU ALEKSANDRA WANIEK, adres rejestrowy Antoniówka (woj. mazowieckie). Faktycznie działa w Lublinie.
- **Oferta:** ręcznie rysowane ilustracje na zamówienie. Główne produkty: podziękowania dla rodziców (wesele), portrety ślubne / pary młodej ze zdjęcia, portrety na prezent (urodziny, rocznice), live painting na weselach.
- **Technika:** wg jej opisu wszystko rysowane na tablecie graficznym, pliki w wersji cyfrowej w 3 wymiarach. Czy pracuje też tradycyjnie: do potwierdzenia.
- **Sprzedaż:** online z wysyłką pocztą/kurierem w całej Polsce; baza w Lublinie.
- **Dowód społeczny:** Wesele z klasą: 51 opinii, średnia 5,0/5, ceny 600–2000 zł, obecna od 2021 r. Na różnych profilach podaje „ponad 1000” albo „ponad 1200” portretów (do ujednolicenia).
- **Ceny wg obecnego katalogu (do potwierdzenia na 2027):** podziękowania 2 ilustracje ok. 1800 zł, 3 ilustracje ok. 2000 zł; portret pary od ok. 600 zł.
- **Cel klientki:** pojawiać się w odpowiedziach czatów AI (ChatGPT, Claude, Gemini, Perplexity, Copilot, Google AI Overviews / AI Mode), gdy ktoś szuka takiej artystki.

## 2. Audyt obecnej widoczności (stan 28.10.2026)

W żadnym z kilkunastu testowych zapytań niszowych marka się nie pojawiła. Znajduje ją tylko ktoś, kto zna nazwę.

| Kanał | Problem |
|---|---|
| weselezklasa.pl | Literówka „Dekoracja Ilustacja”, lokalizacja Warszawa, pinezka mapy w USA, ogłoszenie uśpione, brak live paintingu |
| Facebook /olagrafik | Kategoria „Graphic Designer”, stary opis „projekty logo”, e-mail na domenie olakasperska.pl, link do niezindeksowanej dekolu.pl |
| linktr.ee/dekolu | Nie linkuje do strony |
| dekolu.pl | Brak zindeksowanych podstron. Status do sprawdzenia ręcznie |
| LinkedIn | Podaje Świdnik |
| Live painting | Brak jakiegokolwiek publicznego śladu, że go oferuje |
| Etsy, Pakamera, Allegro, Mapy Google, wedding.pl, janachowska, TikTok, prasa | Brak |

**Ustalenie spójnych danych (NAP), wszędzie identycznie:**
- Nazwa: „dekoracja.ilustracja – Ola Waniek”; „DEKOLU Aleksandra Waniek” tylko jako nazwa prawna (stopka, regulamin, `legalName` w schema).
- Miasto: Lublin (pracownia), „wysyłka w całej Polsce”, „live painting: Lublin i okolice + cała Polska z dopłatą”.
- Jeden e-mail w domenie marki, jeden telefon.
- Domena: preferowana dekoracjailustracja.pl; jeśli zostaje dekolu.pl, wszystkie profile muszą do niej linkować, a H1 strony głównej zawiera „dekoracja.ilustracja”.

## 3. Jak AI wybiera źródła (wnioski z researchu)

- Asystenci przy pytaniach o polecenie firmy prawie zawsze szukają w sieci, rozbijają pytanie na kilka zapytań (query fan-out) i cytują fragmenty, które najbardziej bezpośrednio odpowiadają (cena, miasto, proces, opinie).
- Backendy: Google AI Overviews / AI Mode / Gemini → indeks Google + Profil Firmy; Claude → Brave Search; Copilot → Bing; ChatGPT → historycznie Bing, obecnie w dużej mierze własny indeks; Perplexity → własny pipeline.
- Wniosek: strona musi być zindeksowana w Google, Bing i Brave.
- Google (maj 2026): optymalizacja pod generatywne AI to „wciąż SEO”; llms.txt jest ignorowany; nie ma specjalnej schemy dla AI.
- Dowody: badanie GEO (Princeton/IIT Delhi, KDD 2024): cytaty, statystyki i źródła podnoszą widoczność, upychanie słów kluczowych obniża. Ahrefs (2025): wzmianki o marce korelują z widocznością w AI znacznie silniej niż backlinki; wzmianki na YouTube najsilniej. BrightLocal (2026): w lokalnych zapytaniach AI ok. 28,6% cytowań to Profil Firmy w Google, ok. 42% strony firm. To w większości dane z rynku USA i korelacje, nie dowód przyczynowości.

## 4. Konkurencja i co ją wyróżnia

- **Live painting:** Dorota Szczepaniak / nightbird-art.pl (Lublin, bezpośrednia konkurencja: obraz olejny, 65 rekomendacji na FB, aktywny TikTok, podstrona oferty weselnej, artykuł „Czym jest live wedding painting?”). Dalej m.in. bellaliveart.pl, bujnowlosa.pl, colorisfloris.pl, malowalenaslubie.pl (cena w schema), bartoszaugustyniak.pl.
- **Podziękowania dla rodziców:** kikapaper.pl, artbyzuska.pl, kwietnikobrazow.pl, wlodekrysuje.com, zewecki.pl, szkicewspomnien.pl.
- **Portret ślubny ze zdjęcia / ilustracja z tabletu:** twarzecodziennosci.pl (Product + Offer w schema), dariaguc.pl, lukrecjakot.pl, Pakamera.
- **Portret cyfrowy na prezent:** fraza zalewana tanimi portretami AI (np. 69 zł, „w 5 minut”). Ola musi komunikować „ręcznie rysowany”.
- **Frazy lubelskie** („live painting Lublin”, „malarka Lublin”) są słabo obsadzone: wygrywają agregatory (Oferteo, OLX, bookanartist). To największa szansa.
- **Wspólny mianownik zwycięzców:** jedna podstrona = jedna intencja; cena w zł na stronie (często w schema); opis procesu i logistyki; FAQ językiem klientów; profil w 1–2 katalogach ślubnych z opiniami; treści definicyjne.

## 5. Co robić / czego unikać

**Robić:** konkretne fakty na stronie (ceny, czasy, liczby, cytaty z opinii); wzmianki zewnętrzne (katalogi, media, blogi, YouTube); Profil Firmy w Google + spójne katalogi; klasyczne SEO (indeksacja, szybkość, tekst w HTML); indeksacja w Bing i Brave.

**Nie robić:** llms.txt jako strategia (można dodać, ale bez oczekiwań); upychanie słów kluczowych; fałszywe lub kupowane opinie (w Polsce nieuczciwa praktyka rynkowa); masowe podstrony miejskie generowane AI (wystarczy jedna dla Lublina i jedna „wysyłka w całej Polsce”); kupowanie linków; trzymanie oferty i cennika tylko w grafikach.

## 6. Struktura strony (mapa)

Każda strona: własny URL, jeden H1, cena, proces, 5–8 pytań FAQ, galeria z opisanymi `alt`, opinie, CTA.

| URL | Rola |
|---|---|
| `/` | H1 np. „dekoracja.ilustracja – ręcznie rysowane portrety ślubne i na prezent \| Ola Waniek, Lublin”. Pierwszy akapit: kim jest, co robi, gdzie, za ile od |
| `/podziekowania-dla-rodzicow/` | Najważniejsza strona (tu są popyt i opinie). Pakiety, stroje z dnia ślubu, termin rezerwacji, termin przesłania zdjęć |
| `/portret-slubny-ze-zdjecia/` | Portret pary, rocznice, odtworzenie starego zdjęcia |
| `/live-painting-na-weselu/` | Co dokładnie robi, godziny, zasięg i dojazd, cena od, wymagania od sali, 3–5 realizacji z nazwą sali i miejscowości. Bez tej strony AI nie połączy Oli z live paintingiem |
| `/portret-na-prezent/` | Urodziny, rocznice, Dzień Matki. Akcent „ręcznie rysowany, nie AI” |
| `/cennik/` | Konfigurator ceny: klient wybiera opcje, widzi cenę i wysyła Oli zamówienie lub zapytanie z wybranymi opcjami. Obok tabela cen w HTML (warianty, formaty, wydruki, wysyłka) z tych samych danych |
| `/jak-zamowic/` | Rezerwacja, umowa, zdjęcia, szkic, poprawki, wydruk/plik, wysyłka, płatność |
| `/opinie/` | Wybrane opinie z datą i miastem |
| `/o-mnie/` | Wykształcenie (komunikacja wizualna, PŁ), doświadczenie, liczba portretów, technika, Lublin, zdjęcie przy pracy |
| `/blog/` | Na start 2–4 poradniki z konkretnymi liczbami (pomysły i ceny podziękowań, czym jest live painting, jak wybrać zdjęcie, portret ręczny vs AI) |
| `/kontakt/`, regulamin, polityka prywatności | — |

**Wzorcowe pytania FAQ:** ile kosztuje; ile wcześniej rezerwować; jakie zdjęcia są potrzebne (czy z telefonu); czy rysowane ręcznie czy AI; plik, wydruk czy oprawiony obraz i jaki format; koszt i czas wysyłki, wysyłka za granicę; ile poprawek w cenie; (live) ile trwa, ilu gości zdąży narysować, czego potrzebuje od sali, ile kosztuje dojazd.

**Schema.org (JSON-LD):**
- Strona główna: `ProfessionalService` + `Person` (Ola Waniek, ilustratorka), `name`, `legalName`, `areaServed: ["Lublin","Polska"]`, `addressLocality: "Lublin"`, `priceRange`, pełne `sameAs` (Instagram, Facebook, katalogi, Pinterest).
- Strony usług: `Service` z `Offer` (`price`, `priceCurrency: "PLN"`).
- `FAQPage` na podstronach.
- `Review`/`AggregateRating` tylko dla opinii zebranych na własnej stronie. Nie kopiować oceny z Wesele z klasą.

## 7. Architektura techniczna (decyzja)

**Cel:** motyw do Elementora z własnymi polami w panelu, tak żeby Ola sama edytowała dane w przystępny sposób, bez dotykania układu.

- **Motyw:** lekki motyw potomny Hello Elementor. Zawiera: rejestrację CPT, grupy pól, własne widgety Elementora, generator JSON-LD.
- **Pola:** Secure Custom Fields (darmowy fork ACF z repeaterem i stroną opcji). Pola rejestrowane w kodzie, wersjonowane w git.
- **Widgety własne zamiast dynamic tags:** lead usługi, cennik, proces, FAQ, galeria realizacji, opinie, dane kontaktowe. Czytają pola i renderują HTML po stronie serwera. Wystarczy darmowy Elementor.
- **JSON-LD:** generowany w `wp_head` z tych samych pól co widok.
- **Uprawnienia:** Ola ma rolę Redaktora bez dostępu do edytora Elementora (Menedżer ról), odchudzone menu admina. Układ ustawia tylko Alek.
- **Zamówienia (decyzja Alka, 30.10.2026):** bez sklepu, koszyka i WooCommerce, bez zamawiania przez WhatsApp. Konfigurator na `/cennik/` wysyła Oli zamówienie lub zapytanie z opcjami wybranymi przez klienta; Ola sama odzywa się do klienta. Ceny muszą być też w HTML (tabela), bo konfigurator działa w JS. Live painting: zapytanie o termin.

### Model danych

| Gdzie | Pola edytowane przez Olę |
|---|---|
| Strona opcji „Dane pracowni” | Nazwa, e-mail, telefon, miasto, obszar, linki do profili (`sameAs`), liczba portretów, zasady wysyłki |
| CPT Usługi | Akapit otwierający (2–3 zdania: co, dla kogo, gdzie, za ile), czas realizacji, kroki procesu (repeater), FAQ (repeater), realizacje (relacja), rodzaj CTA (konfigurator / zapytanie o termin), cena od (tylko usługi spoza konfiguratora, np. live painting) |
| CPT Realizacje | Zdjęcie, opis (źródło `alt`), okazja, format, miasto lub sala, checkbox „mam zgodę klienta” (bez niego realizacja nie trafia na front) |
| CPT Opinie | Treść, imię, miasto, data, źródło, zgoda |
| Strona opcji „Cennik” | Ceny bazowe, dopłaty (osoba, pupil), wydruki, wysyłka |

**Cena:** ceny wpisywane w jednym miejscu (strona opcji „Cennik”). Konfigurator, tabela cen, „cena od” na stronach usług i JSON-LD są z niej liczone. Ręcznie wpisywana wyłącznie tam, gdzie usługi nie ma w konfiguratorze (live painting). Nigdy dwa miejsca z tą samą ceną.

## 8. Plan prac przed napisaniem motywu (kolejność)

Ścieżka główna, po kolei:

1. **Ustalenia z Olą (blokuje resztę):** brief na jedną stronę: usługi i warianty; live painting (czy, jak: tablet z wydrukiem czy farby, godziny, zasięg, dopłata za dojazd); ceny 2027; formy dostawy (plik/wydruk/rama), czas realizacji, liczba poprawek, termin rezerwacji; nazwa, domena, e-mail, telefon, liczba portretów.
   → weryfikacja: każde pole wypełnione, zero „do ustalenia”, Ola potwierdziła na piśmie.
2. **Mapa stron i fraz:** tabela URL, fraza, H1, title, meta, typ szablonu.
   → weryfikacja: każda usługa ma jeden URL, żadna fraza nie jest przypisana do dwóch stron, każdy URL ma typ szablonu.
3. **Treści i materiały:** teksty od razu w układzie pól (sekcja dokumentu = pole); 8–10 realizacji na usługę z opisem; zgody klientów na wizerunek i opinie (RODO); bio i zdjęcie Oli.
   → weryfikacja: 100% stron ma gotowy tekst, każde zdjęcie ma opis i zgodę, ceny zgodne z briefem.
4. **Model zamówień i prawo:** decyzja: bez sklepu, konfigurator (30.10.2026); regulamin, polityka prywatności (przesyłanie zdjęć = dane osobowe), zapis o odstąpieniu od umowy dla produktów personalizowanych (do weryfikacji przez prawnika lub sprawdzony generator).
   → weryfikacja: decyzja zapisana, regulamin gotowy.
5. **Wireframe'y:** 7 typów stron (główna, usługa, cennik z konfiguratorem, jak zamówić, o mnie, wpis, kontakt), mobile first. Wspólne komponenty: hero z akapitem otwierającym w HTML, blok ceny, proces, FAQ w DOM, galeria, opinie, CTA, stopka z NAP. Plus wireframe'y panelu: formularze 4 encji i strona opcji.
   → weryfikacja: każdy URL ma szablon, wireframe'y wypełnione prawdziwą treścią, zaakceptowane przez Olę.
   **5b. Specyfikacja pól:** tabela: pole, typ, wymagane, limit znaków, podpowiedź dla Oli, gdzie się wyświetla, czy trafia do schema.
   → weryfikacja: każdy element z wireframe'u ma źródło w polu albo w stałym tekście motywu.
6. **Design system i specyfikacja techniczna:** kolory i fonty spójne z Instagramem, logo w SVG; jeden H1 na stronę; plan JSON-LD per szablon; lista widgetów i mapowanie pole → widget → schema; budżet wydajności (LCP < 2,5 s, obrazy WebP); minimalna lista wtyczek; robots.txt bez blokad dla Googlebota, Bingbota i botów AI.
   → weryfikacja: każdy szablon ma typy schema i listę komponentów, lista wtyczek zamknięta.

Równolegle od tygodnia 1:
- **Domena i hosting:** sprawdzić dekolu.pl, wybrać domenę, staging za hasłem z noindex.
  → weryfikacja: domena opłacona, staging działa i nie jest indeksowany.
- **Profile:** poprawić Wesele z klasą (nazwa, Lublin, reaktywacja, osobne ogłoszenie live painting), Facebook (kategoria artysta/ilustrator, nowy opis, e-mail w domenie marki).
  → weryfikacja: wyszukiwanie „dekoracja.ilustracja” nie pokazuje już „Ilustacja” ani „Warszawa”.
- **Profil Firmy w Google** (firma usługowa bez publicznego adresu, obszar Lublin + województwo), Bing Places, Apple Business Connect.
  → weryfikacja: profil zweryfikowany (trwa od kilku dni do kilku tygodni).

**Definition of ready przed kodem motywu:** kroki 1–6 przeszły weryfikację. Nie zaczynać od szablonu z placeholderami.

## 9. Kryteria akceptacji motywu

- [Specyfikacja pól] → weryfikacja: w szablonach Elementora nie ma treści wpisanej na sztywno.
- [Jedno źródło] → weryfikacja: zmiana telefonu na stronie opcji widoczna w stopce, w kontakcie i w JSON-LD (Rich Results Test).
- [Cena] → weryfikacja: zmiana ceny na stronie opcji „Cennik” zmienia cenę w konfiguratorze, na stronie usługi, w tabeli cen i w JSON-LD.
- [Zgody] → weryfikacja: realizacja bez zaznaczonej zgody nie pojawia się na froncie ani w galerii.
- [Treść w HTML] → weryfikacja: `curl` strony usługi zwraca cenę i pełny tekst FAQ bez wykonywania JS.
- [Użyteczność] → weryfikacja: Ola bez instrukcji dodaje pytanie FAQ i nową realizację w mniej niż 5 minut i nie widzi przycisku „Edytuj w Elementorze”.
- [Indeksacja] → weryfikacja: Search Console i Bing Webmaster Tools bez błędów; `site:domena` w Google, Bing i Brave zwraca wszystkie podstrony usług.

## 10. Po starcie strony (marketing i pomiar)

**Katalogi i kanały (priorytet):** Profil Firmy w Google i Bing Places (obowiązkowo); Wesele z klasą (reaktywacja + live painting); wedding.pl; katalog.janachowska.pl; Pakamera (2–3 produkty); OLX Lublin, Oferteo Lublin; Pinterest; YouTube Shorts / TikTok (timelapse'y, relacje z wesel z nazwą sali i miejscowości); Instagram z linkiem bezpośrednio do strony. Etsy opcjonalnie przy sprzedaży za granicę; Allegro niski priorytet.

**Opinie:** prośba o opinię w Google do 20–30 ostatnich klientek; cel 15+ w 2 miesiące; tylko prawdziwe i nienagradzane.

**Wzmianki:** lubelskie media lokalne, sale weselne w okolicy Lublina, blogi ślubne i rankingi „top X”, fotografowie ślubni z Lublina, poradnik Wesele z klasą.

**Pomiar (co miesiąc, ten sam zestaw):** ChatGPT z wyszukiwaniem, Claude, Gemini, Perplexity, Copilot, Google AI Mode; arkusz: czy Ola wymieniona (0/1), pozycja, cytowane źródło, kogo wymieniono zamiast niej.

Prompty testowe:
1. Kto w Polsce robi ilustrowane podziękowania dla rodziców na wesele?
2. Polecisz ilustratorkę, która narysuje portret ślubny ze zdjęcia?
3. Malowanie na żywo na weselu Lublin – kogo polecasz?
4. Live painting na ślub w lubelskim, ceny
5. Ręcznie rysowany portret na urodziny mamy ze zdjęcia z wysyłką
6. Portret cyfrowy na prezent, ale rysowany przez człowieka, nie AI
7. Malarka Lublin portrety na zamówienie
8. Ile kosztują podziękowania dla rodziców w formie portretu?
9. Obraz ze zdjęcia na zamówienie – polscy artyści
10. Ilustracja ślubna na zamówienie – kto ma dobre opinie?
11. Co to jest dekoracja.ilustracja?
12. Atrakcje weselne Lublin artysta

Dodatkowo: Google Alerts na nazwę marki; w analityce osobny kanał dla odesłań z chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai; pytanie „skąd Pani o mnie wie?” w formularzu (z opcją „ChatGPT/AI”).

**Realistyczne terminy (szacunki):** 1–4 tygodnie indeksacja i poprawne wyniki na zapytanie o markę; 1–3 miesiące pierwsze pojawienia się w niszowych i lubelskich zapytaniach AI; 3–6 miesięcy stabilniejsza obecność w części promptów (odpowiedzi AI są z natury niestabilne, mierzyć odsetek w czasie); 6–18 miesięcy wejście marki do wiedzy modeli. Ogólnopolskich ogólnych fraz nie wygrywać szybko; strategia to długi ogon i Lublin.

## 11. Otwarte kwestie

- Czy i jak dokładnie Ola robi live painting (tablet z wydrukiem na miejscu czy media tradycyjne)? Jeśli tak, wyróżnić się formatem względem nightbird-art.pl (obraz olejny).
- Czy pracuje wyłącznie na tablecie?
- Domena: dekolu.pl (status nieznany) czy dekoracjailustracja.pl?
- Ceny 2027 i jedna liczba wykonanych portretów.
- Kwestie prawne zamówień na odległość (odstąpienie od umowy, RODO przy zdjęciach) do weryfikacji.
- Do sprawdzenia przy implementacji: obsługa Secure Custom Fields w aktualnej wersji Elementora oraz zakres darmowego Menedżera ról Elementora.
