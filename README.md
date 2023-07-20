# KingTide-Challenge
Tech test for king tide

<hr>

## Preparando el entorno
```` shell
$ python3 -m venv venv
$ source venv/bin/activate
$ export PYTHONPATH=$PWD
````

## Instalando dependencias
```` shell
pip install fastapi pymongo uvicorn
pip install python-multipart
pip install boto3
````

## Ejecutando API 
```` shell
uvicon server:app --reload
````

## Ver la documentación

<a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs </a>

# Acerca del ejercicio

Nunca habia trabajado desde cero con MongoDB y FastAPI Asi que decidí usar ese stack

- Relice la definicion de los schemas base con ayuda de pydantic https://docs.pydantic.dev
- Ralice la integración d ela base de datos con mongoDB usando pymongo https://pymongo.readthedocs.io/en/stable/
- y monte la API con ayuda de FastAPI https://fastapi.tiangolo.com








