# Django
## Instalace 
```bash
pip install django
pip freeze > requirements.txt
django-admin startproject <nazev_projektu> .
```

## Struktura projektu
- `MovieDB` - složka projektu (obsahuje informace o celém projektu)
  - `__init__.py` - je zde jen proto, aby daná složka byla package
  - `asgi.py` - nebudeme potřebovat
  - `settings.py` - nastavení projektu
  - `urls.py` - zde jsou nastavené url adresy
  - `wsgi.py` - nebudeme potřebovat
- `manage.py` - hlavní skript pro práci s projektem (souštění serveru, testů, migrací,...)

## Spuštění serveru
```bash
python manage.py runserver
```

## .gitignore
Správný projekt má nastavení pro ingorované soubory v git repozitáři v souboru `.gitignore`.

## .env
Slouží k ukládání citlivých informací (SECRET_KEY, hesla, přístupové údaje,...).

### Instalace
```bash
pip install python-dotenv
pip freeze > requirements.txt
```

Vytvoříme soubour s názvem `.env` v kořenovém adresáři projektu.

Do souboru `settings.py` vložíme:
```python
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY', default='django-insecure-)si+fpno3#)=7__vx-4%ni^&n1wvaz9bju1e+s8*i!e9qt!@f)')
```

## Vytvoření superuživatele
```bash
python manage.py createsuperuser
```

## Aplikace
### Vytvoření
```bash
python manage.py startapp <název_aplikace>
```

### Struktura aplikace
- `viewer` - složka aplikace
  - `migrations` - složka obsahující migrační skripty
  - `__init__.py` - je tu zde jen proto, aby daná složka byla package
  - `admin.py` - nastavení administrační stránky
  - `apps.py` - nastavení aplikace - nebudeme upravovat
  - `models.py` - zde bude definice modelů (databáze)
  - `tests.py` - zde budou testy
  - `views.py` - zde budou views (funkcionalita)

  ### Registrace aplikace
Do souboru `settings.py` musíme novou aplikaci zaregistrovat do seznamu 
`INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'viewer',
]
```