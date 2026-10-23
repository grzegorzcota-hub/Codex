# Instagram Reels — piony v4

Trzy poprawione piony 1080×1920, na podstawie zrzutów interfejsu przesłanych przez użytkownika. Zachowano poprzednie wersje w folderze meta_adaptacje.

Zdjęcie i dekoracje wypełniają cały kadr. Wybielenie jest lokalne, pod treścią, a nie na całej dolnej części. Nagłówki umieszczono wyżej. Prawy pas ikon jest chroniony w obszarze, w którym występuje na zrzucie; nie blokuje całej wysokości grafiki.

Profil ręczny: pole treści X=120–960, Y=190–1220; blokada prawego pasa X=880–1080, Y=1010–1660; obszar CTA/opisu Y≥1230. Granice są przybliżeniem, nie pomiarem plików źródłowych reklamy: zrzuty pokazują ekran, a skalowanie i kadrowanie oryginalnego materiału nie są znane. Roboczo zastosowano wariant wypełnienia ekranu 710×1536 materiałem 1080×1920 (skala 0,8; obcięcie około 77 px obrazu na ekranie z każdej strony). Odtworzony podgląd jest wyłącznie symulacją.

Pierwszy zrzut użytkownika pokazuje kwadrat z czarnymi pasami; nie wykorzystano jego granic do ustalenia marginesów pełnoekranowego pionu. Drugi zrzut posłużył do orientacyjnego położenia CTA, konta i ikon.

Każdy tekst i ikona ma osobne granice. Raporty obejmują geometrię, kolizje, kontrast rzeczywistych pikseli, pisownię i integralność PNG. Ta wersja nie jest certyfikacją aktualnych reguł Meta i nie jest automatycznie przenoszona na Stories lub Facebook. Warunki oferty wymagają potwierdzenia.

## Zmiany wersji 4

1. Opieka medyczna: odstęp nagłówek–podtytuł +10 px i podtytuł–belka +10 px; tekst cenowy wyśrodkowany w prawej części belki.
2. Ubezpieczenia: blok ikon i podpisów wyśrodkowany między podtytułem a „Także dla mniejszych firm”, według granic glifów.
3. Benefity: blok ikon i podpisów 25 px pod podtytułem.

Wszystkie główne ikony benefitów większe o 20% względem wersji 3. Pomiary w `weryfikacja_zmian_v4.json`. Do emisji użyj trzech PNG bez sufiksów `_strefy` i `_symulacja_instagram`. Paczka: `Trzy_piony_Instagram_v4.zip`.
