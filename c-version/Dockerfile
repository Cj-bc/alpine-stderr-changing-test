FROM python:3.9-alpine

WORKDIR workdir
RUN apk add gcc musl-dev
RUN pip install cffi
COPY stderr-changing.c ./
RUN  gcc -o stderr-changing stderr-changing.c
CMD ./stderr-changing
