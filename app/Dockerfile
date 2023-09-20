#descargar todas las librerias en docker

FROM python:3.8

WORKDIR / app
COPY requeriments.txt /app/requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /app/requeriments.txt

COPY . app/

#mantiene en ejecución constante el contenedor
CMD bash -c "while true; do sleep 1; done"