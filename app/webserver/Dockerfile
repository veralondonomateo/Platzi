#descargar todas las librerias en docker

FROM python:3.10

WORKDIR / app
COPY requeriments.txt /app/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requeriments.txt

COPY . /app

#mantiene en ejecución constante el contenedor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80" ]