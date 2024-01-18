# Projekta README.md

## Projekta nosaukums: Datu ieguve un uzglabāšana no ss.lv

### Uzdevums:
Projekta mērķis ir automātiski iegūt un uzglabāt datus no ss.lv vietnes, konkrēti - automašīnu sludinājumu informāciju par dažādiem zīmoliem un modeļiem. Šo kodu var izmantot, lai iegūtu svaigus datus un analizēt automašīnas tirgus tendences.

### izmantoās Python bibliotēkas:

1. **os**: Šī bibliotēka tiek iizmantota, lai strādātu ar operētajsistēmas funkcijām, piemēram, pārbaudītu, vai fails jau eksistē pirms datu rakstīšanas.

2. **time**: Šī bibliotēka tiek izmantota, lai izveidotu kavējumus starp darbībām, piemēram, gaitīt, kamēr lapas elementi tiek ielādēti.

3. **pandas**: Šī bibliotēka nodrošina datu struktūrām un to pārveidošanu datu analīzei.

4. **selenium**: Selenium tiek izmatots automatizētai vietnes pārlūkošanai un interakcijai ar tās elementiem.

### Prokmmatūras izmantošanas metodes:

- **`wait_and_click`**: Gaida kamēr kļūst noklikšķināms un pēc tam to noklišķina, lai veiktu darbību.

- **`scrape_and_write_to_excel`**: Atver pārlūku, apmeklēt norādīto vietni un iegūst informāciju par automašīnām, pamatojoties uz dotajiem fitrēšanas kritērijiem. Pēc tam šie dati tiek saglabāti Excel failā.

- **`scrape_and_write_for_car_brands`**: Izveido sarakstu ar automašīnu zīmoliem un to filtru identikātoriem, kas tiek padoti `scrape_and_write_to_excel` funkcijai. Tiek veikta datu iegūšana un saglabāšana katram zīmolam atsevišķi.

- **Galvenais bloks**: Izsauc funkcijau  `scrape_and_write_for_car_brands` un veic datu iegūšanu un saglabāsanu visiem noteiktajiem automašīnu zīmoliem.

### Kā izmantot kodu:
1. Ievietojiet nepiecišamās Python bibliotēkas, izmatojot `pip install`.
2. Pārliecinieties, ka jums ir uzstādīts Google Chrome pārlūks, jo izmatojams `webdriver.Chrome`.
3. Izmainiet vai papildiniet automašinu zīmolus un to filtru identifikatorus pēc vajadzības.'
4. Palaidiet kodu un novērojiet, kā dati tiek iegūti un saglabāti Excel failā katram zīmolam.

Papildu zīmoli un filtru identifikātori var tikt pievienoti pēc nepecišamības 

## Atcerieties
- Kods ir paredzēts tikai ss.lv vietnes automašīnu sludinājumu iegušanai.
- Pirms darba sākšanas izpētiet vietnes lietošanas noteikumus un noscījumus