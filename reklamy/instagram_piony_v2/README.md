# Instagram Reels — piony v2

Trzy poprawione piony 1080×1920, na podstawie zrzutów interfejsu przesłanych przez użytkownika. Zachowano poprzednie wersje w folderze meta_adaptacje.

Zdjęcie i dekoracje wypełniają cały kadr. Wybielenie jest lokalne, pod treścią, a nie na całej dolnej części. Nagłówki umieszczono wyżej. Prawy pas ikon jest chroniony w obszarze, w którym występuje na zrzucie; nie blokuje całej wysokości grafiki.

Profil ręczny: pole treści X=120–960, Y=190–1220; blokada prawego pasa X=880–1080, Y=1010–1660; obszar CTA/opisu Y≥1230. Granice są przybliżeniem, nie pomiarem plików źródłowych reklamy: zrzuty pokazują ekran, a skalowanie i kadrowanie oryginalnego materiału nie są znane. Roboczo zastosowano wariant wypełnienia ekranu 710×1536 materiałem 1080×1920 (skala 0,8; obcięcie około 77 px obrazu na ekranie z każdej strony). Odtworzony podgląd jest wyłącznie symulacją.

Pierwszy zrzut użytkownika pokazuje kwadrat z czarnymi pasami; nie wykorzystano jego granic do ustalenia marginesów pełnoekranowego pionu. Drugi zrzut posłużył do orientacyjnego położenia CTA, konta i ikon.

Każdy tekst i ikona ma osobne granice. Raporty obejmują geometrię, kolizje, kontrast rzeczywistych pikseli, pisownię i integralność PNG. Ta wersja nie jest certyfikacją aktualnych reguł Meta i nie jest automatycznie przenoszona na Stories lub Facebook. Warunki oferty wymagają potwierdzenia.

## Pliki

| Kreacja | PNG do reklamy | Symulacja interfejsu | Strefy |
|---|---|---|---|
| Opieka medyczna | [PNG](01_opieka_medyczna_1080x1920.png) | [Podgląd](01_opieka_medyczna_1080x1920_symulacja_instagram.png) | [Strefy](01_opieka_medyczna_1080x1920_strefy.png) |
| Ubezpieczenia grupowe | [PNG](02_ubezpieczenia_grupowe_1080x1920.png) | [Podgląd](02_ubezpieczenia_grupowe_1080x1920_symulacja_instagram.png) | [Strefy](02_ubezpieczenia_grupowe_1080x1920_strefy.png) |
| Dobrego pracownika trudno zastąpić | [PNG](03_dobrego_pracownika_1080x1920.png) | [Podgląd](03_dobrego_pracownika_1080x1920_symulacja_instagram.png) | [Strefy](03_dobrego_pracownika_1080x1920_strefy.png) |

[Pobierz całą paczkę](Trzy_piony_Instagram_v2.zip). Symulacje służą do porównania kompozycji; do kampanii użyj czystych plików PNG.

Kontrola niezależna: `python sprawdz_raporty.py`.
