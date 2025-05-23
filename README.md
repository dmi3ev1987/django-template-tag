
## Как запустить проект

  

Cоздать и активировать виртуальное окружение:

  

* Если у вас Linux/macOS

  

```

python3 -m venv venv

source env/bin/activate

```

  

* Если у вас windows

  

```

python -m venv venv

source env/scripts/activate

```

  

Обновите менеджер пакетов pip:

  

```

python -m pip install --upgrade pip

```

  
  

Установить зависимости из файла requirements.txt:

  

```

pip install -r requirements.txt

```

  

## Создать и применить миграции

  

```

python manage.py makemigrations
python manage.py migrate

```

  

## Создать суперпользователя


```

python manage.py createsuperuser

```


## Для тестирования меню можно заполнить БД данными из JSON


```

python manage.py loaddata db.json

```


## Запустить приложение


```

python manage.py runserver

```

## Пример готового меню


![Tree menu example](docs/images/tree-menu-example.jpg)
  

## Работа с Ruff линтером и форматтером
  

```

# Check and auto-fix all files in the project:
ruff check --fix

  

# Check/fix a specific file:
ruff check --fix path/to/file.py

  

# Preview fixes before applying:
ruff check --fix --diff

  

# For formatting, use:
ruff format

```

  
  

### Автор проекта

  

[Дмитриев Андрей](https://github.com/dmi3ev1987)