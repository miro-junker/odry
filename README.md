# Design
- do hlavičky foto studentů
- do patičky loga sponzorů

# Todo
- h1 / h2 / h3 (/ h4 / h5 / h6)
- značka u odkazů, které vedou ven
- transitions
- vycentrovat text v menu
- hezčí h2 nadpis?
- loga do patičky
- font-size, line-height, perex color
- knihoviny i lokálně

# Refactor
- udělat nějaké makro z pagination

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
- návod do administrace

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

# Instalace Windows
- spustit konzoli jako root
- pip install Django==1.11.5
- pip install Pillow
- pip install markdown
- pip install django-bleach

- python manage.py createsuperuser

- problém s odlášeným účtem

# Instalace Debian
- apt-get install git
virtualenv --python=python3.4 myvenv
- apt-get install python-pip
- pip install virtualenv
- apt-get install python3-venv
- source prod_venv/bin/activate
- pip install Django==1.11.5
- pip install markdown
- pip install django-bleach
- pip install Pillow
(- pip install whitenoise -tj. knihovna na staticke soubory)
python manage.py collectstatic


zvážit:
turnkey core
ShellInBox, Django Administration Console
SSL
iPython?
Webmin (configuring Apache2 & MySQL)