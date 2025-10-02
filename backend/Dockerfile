FROM nvidia/cuda:12.4.1-runtime-ubuntu22.04 as dev

WORKDIR /app
COPY app/requirements.txt .
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip3 install --no-cache-dir torch==2.4.1+cu124 --index-url https://download.pytorch.org/whl/cu124 && \
    pip3 install --no-cache-dir -r requirements.txt
COPY app/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

FROM python:3.10-slim as prod
WORKDIR /app
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app/ .
RUN mkdir -p uploads text
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
