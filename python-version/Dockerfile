FROM python:3.9-alpine

WORKDIR workdir
RUN pip install cffi
COPY _ffi_test.py requirements.txt ./
RUN pip install -r requirements.txt && python _ffi_test.py
COPY stderr-changing.py ./
CMD python stderr-changing.py
