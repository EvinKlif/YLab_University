Инструкция по установки:

1. cd .\YLab_University\
2. pip install -r requirements.txt
3. зайти в файл db и изменить поле SQLALCHEMY_DATABASE_URL на адресс своего postgres
4. сделать alembic revision --autogenerate -m 'Test'
5. alembic upgrade head
6. uvicorn main:app --host 0.0.0.0 --port 8000
7. проверить тесты


