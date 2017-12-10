# Todo
- bootstrap 4 (i v administraci)
- vsechny admin url zacinaji na /sprava
- přejmenovat upload na download a zviditelnit

# Fáze 1
- upload dokumentů (PDF) - pro začátek možná přes kopírování souborů nebo FTP klient
- fotogalerie = externí služba (např. rajče)

# Fáze 2
- favicon
- zpětné odkazy z detail-stránek (aktualita, událost, galerie)
- vlastní fotogalerie, nahrávání fotek
- videa
- vyhledávání
- potvrzení při mazání
- tabulky (markdown)
- h1 odkaz nikoliv z homepage
- data bez času v administraci
- české url na login

# Fáze 3
- drobečková navigace? (jak vyřešit hierarchii statických stránek?)
- SEO URL (statické stránky, potom i aktuality, akce a galerie) 
- ajaxové dočítání aktualit?
- české slovní názvy měsíců v datumech
- flash messages po mazání
- jen heslo, jméno netřeba
- jazykové mutace

# Poznámky
- běží to na Savaně (zachovat kvůli e-mailům)
- formuláře stačí jako statická stránka

# Použití
- aktivace prostředí: `venv/Scripts/activate`
- spuštění serveru: `python manage.py runserver`
- pro aktualizaci modelu: `python manage.py migrate schoolapp`
- vytvoření admina: `python manage.py createsuperuser`