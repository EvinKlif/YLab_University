Инструкция по установки:

1. cd .\YLab_University\
2. cd .\YLab_University\
3. pip install -r requirements.txt
4. зайти в файл db и изменить поле SQLALCHEMY_DATABASE_URL на адресс своего postgres
5. сделать alembic revision --autogenerate -m 'Test'
6. alembic upgrade head
7. uvicorn main:app --host 0.0.0.0 --port 8000
8. проверить тесты


