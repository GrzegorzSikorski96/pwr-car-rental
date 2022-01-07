### Autor

Inż. Grzegorz Sikorski

**Uczelnia:** Politechnika Wrocławska\
**Kierunek:** Automatyka i robotyka, studia stacjonarne II stopnia\
**Specjalność:** Technologie informacyjne w systemach automatyki\
**Wydział:** Wydział Elektroniki, Fotoniki i Mikrosystemów

### Projekt

**Temat:** Planowanie czynności serwisowych w firmie wypożyczającej długoterminowo samochody


### Uruchomienie aplikacji
* Wymagania
  * Baza danych MySql 8.0
  * Python 3.9
  * Make (Opcjonalnie)
  * Docker (Opcjonalnie)

### Uruchamianie aplikacji - docker

* Skopiuj zawartość pliku `.env.dist` do pliku `.env` oraz zmień wartości zmiennych zgodnie z potrzebą. Aplikacja powinna działać bez żadnych zmian.
* Polecenie `make run` uruchomienie aplikacji.
* Polecenie `make test` uruchenie testów.
* Polecenie `make bash` przejście do konsoli dockerowej.
* Aplikacja dostępna pod adresem `127.0.0.1:<PORT Z PLIKU .ENV>`.

### Uruchamianie aplikacji

* Utworzyć wirtualne środowisko python (venv) w projekcie używajac polecenia `python3 -m venv venv`
* Aktywować wirtualne środowisko
  * Windows: `venv\Scripts\activate`
  * Linux: `source venv/bin/activate`
* Skopiuj zawartość pliku `.env.dist` do pliku `.env` oraz zmień wartości zmiennych zgodnie z potrzebą.
* Uruchomienie servera: `python3 manage.py runserver`
