# Design
- do patičky loga sponzorů

# Todo
- detekovat a vyřešit 500
- lepší markdown parser (lepší BR)
- odstranit z repo configy a db, nechat jen .dist (a dát do gitinore)
- pojmenovat česky fields v administraci
- do patičky loga
- dát do adminu bootstrap 4 & font awesome
- nasměrovat DNS
- h1 / h2 / h3 (/ h4 / h5 / h6)
- hezčí h2 nadpis?

- vyřešit logování

- nastavit někam jinam SECURITY_KEY a DEBUG
- zálohovat db & uploadované soubory
- značka u odkazů, které vedou ven
- transitions
- vycentrovat vertikálně text v menu
- font-size, line-height, perex color
- detekovat / problém s odlášeným účtem
- postgres na produkci? https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
- ufw firewall?

# Refactor
- udělat nějaké makro z pagination

# Fáze 1
- fotogalerie = externí služba (např. rajče)
- search google
- formuláře jako statická stránka

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
- 404 stránka

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
- vícejazyčné překlady?

# Poznámky
- ssodry.cz běží na Savaně (zachovat kvůli e-mailům)

# Použití
- aktivace development prostředí: `venv/Scripts/activate`
- spuštění develompment serveru: `python manage.py runserver`
- aktualizace modelu: `python manage.py migrate schoolapp`
- vytvoření admina: `python manage.py createsuperuser` (používat vždy username `admin`)

# Instalace development (Windows)
- spustit konzoli jako root
- `pip install Django==1.11.5 Pillow markdown django-bleach whitenoise`
- `python manage.py createsuperuser` (používat vzdy username `admin`)

# Instalace production (Raspbian)
- Raspberry Pi Configuration:
    change password p6
    enable ssh & vnc
    language cs, country cz
    timezone europe / prague
- `sudo apt-get update`
- sudo apt-get -y install mc nginx (python3-pip python3-dev libpq-dev postgresql postgresql-contrib)
- zkopírovat data do /home/odry/program
- python3 -m venv pienv
- source pienv/bin/activate
- pip install Django==1.11.5 markdown django-bleach Pillow whitenoise gunicorn (psycopg2)
- python3 manage.py collectstatic
- nastavit DJANGO_SECRET_KEY v ./start
- `deactivate`
- cp home/pi/odry/program/gunicorn.service /etc/systemd/system/gunicorn.service
- sudo nano /etc/systemd/system/gunicorn.service
- sudo systemctl start gunicorn
- sudo systemctl enable gunicorn
- cp /home/pi/odry/program/nginx_odryproject /etc/nginx/sites-available/odryproject
- sudo nano /etc/nginx/sites-available/odryproject
    nastavit ip
- sudo ln -s /etc/nginx/sites-available/odryproject /etc/nginx/sites-enabled
- sudo nginx -t (jenom test správnosti syntaxe)
- sudo systemctl restart nginx

(- pokud mám ufw firewall, tak: sudo ufw 8000
    sudo ufw allow 'Nginx Full')

- pokud bude třeba vytvořit admina: `python manage.py createsuperuser` (používat vždy username `admin`)
- zkontrolovat settings.py ALLOWED_HOSTS
- nakonfigurovat SSL/TLS https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-16-04

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
