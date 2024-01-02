FROM python:3.8-slim-buster

WORKDIR /app

COPY ./requirements.txt .
COPY ./server.py .
COPY . .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt


EXPOSE 8000
CMD ["python", "server.py"]
#CMD ["uvicorn", "pyrestapi.api:app", "--host", "0.0.0.0", "--port", "8000"]