# Adaptacje wzorów — kontrola stref

Trzy kreacje w dwóch niezależnych układach: 1080×1080 i 1080×1920. Zachowano charakter referencji; fotografie i tła były edytowane z użyciem AI, tekst i ikony zostały złożone programowo. Nie są to kopie 1:1.

Kontrola geometryczna sprawdza każdy napis i ikonę, pełne granice, zapas 8 px, kolizje oraz prawy pas Reels. Podglądy `_strefy.png` pokazują wynik. Logo może znajdować się w górnej strefie ostrzegawczej. Dolna część pionów zawiera wyłącznie tło.

Profile są konserwatywnymi parametrami roboczymi, NIE potwierdzoną aktualną specyfikacją Meta. Próba odczytu oficjalnych źródeł jest zapisana w JSON. Nie deklarujemy zweryfikowania w rzeczywistym Menedżerze reklam. Wymagana końcowa kontrola podglądu konkretnego umiejscowienia w Meta. Cena 59 zł, terminy 2/5 dni oraz warunki wymagają potwierdzenia oferty. Zrezygnowano z graficznych przycisków dublujących CTA Meta.

## Pliki do pobrania

| Kreacja | Kwadrat | Pion | Strefy w pionie |
|---|---|---|---|
| Opieka medyczna | [PNG](01_opieka_medyczna_1080x1080.png) | [PNG](01_opieka_medyczna_1080x1920.png) | [Podgląd](01_opieka_medyczna_1080x1920_strefy.png) |
| Ubezpieczenia grupowe | [PNG](02_ubezpieczenia_grupowe_1080x1080.png) | [PNG](02_ubezpieczenia_grupowe_1080x1920.png) | [Podgląd](02_ubezpieczenia_grupowe_1080x1920_strefy.png) |
| Dobrego pracownika trudno zastąpić | [PNG](03_dobrego_pracownika_1080x1080.png) | [PNG](03_dobrego_pracownika_1080x1920.png) | [Podgląd](03_dobrego_pracownika_1080x1920_strefy.png) |

Paczka: [Trzy kreacje — kwadraty, piony, strefy i raporty](Trzy_kreacje_kwadrat_i_pion_strefy.zip). W GitHub użyj pobierania surowego pliku (Download raw file).

Niezależna kontrola plików: `python sprawdz_raporty.py`. Sprawdza hasze PNG, ich rzeczywiste wymiary, granice każdego obiektu i zapisane wyniki kontrastu. Test celowego przesunięcia poza strefę musi zakończyć się wykryciem błędu.
