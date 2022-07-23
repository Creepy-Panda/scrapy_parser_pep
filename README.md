## Scrapy Parser Pep

## Стек технологий
![Scrapy](https://img.shields.io/badge/Python-Scrapy-yellow?style=for-the-badge&logo=appveyor)

## Описание
Асинхронный парсер PEP правил с официальной документации Python

## Порядок запуска

Клонируйте репозиторий
```
git clone git@github.com:Creepy-Panda/scrapy_parser_pep.git
```

Переходим в папку с проектом, создаем виртуальное окружение, устанавливаем зависимости и запускаем парсер
```
cd pep_parser
python3 -m venv venv
pip install -r requirements.txt
scrapy crawl pep
```
После выполнения команды появится папка results в которой два файла:

1. ```pep_(дата)``` - Cписок всех PEP: номер, название и статус
2. ```status_summary_(дата)``` - Cодержит сводку по статусам PEP и колличество всех документов
