# Design
- do hlavičky foto studentů

# Todo
- bootstrap 4
- frontend

# Fáze 1
- fotogalerie = externí služba (např. rajče)
- search google

# Fáze 2
- homepage: carousel, novinky, shortcut odkazy, nejbližší událost, sudý/lichý týden, svátek
- favicon
- mapa
- zpětné odkazy z detail-stránek (aktualita, událost, galerie)
- vlastní fotogalerie, nahrávání fotek
- videa
- vlastní vyhledávání
- potvrzení při mazání
- tabulky (markdown)
- h1 odkaz nikoliv z homepage
- data bez času v administraci
- české url na login
- rychloodkazy z webu do administrace pro přihlášené
- bootstrap 4 v administraci
- zvýraznit dnešek v kalendáři

# Fáze 3
- drobečková navigace? (jak vyřešit hierarchii statických stránek?)
- SEO URL (statické stránky, potom i aktuality, akce a galerie) 
- ajaxové dočítání aktualit?
- české slovní názvy měsíců v datumech
- flash messages po mazání, přidávání, editaci
- jen heslo, jméno netřeba
- jazykové mutace
- obrázky do administrace
- různé pozadí pro sudé a liché řádky v tabulkách
- překlady titulků ve formulářích

# Poznámky
- běží to na Savaně (zachovat kvůli e-mailům)
- formuláře stačí jako statická stránka

# Použití
- aktivace prostředí: `venv/Scripts/activate`
- spuštění serveru: `python manage.py runserver`
- pro aktualizaci modelu: `python manage.py migrate schoolapp`
- vytvoření admina: `python manage.py createsuperuser`

# Deploy
- `pip install Pillow` - obrázková knihovna