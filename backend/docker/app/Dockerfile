FROM tiangolo/uvicorn-gunicorn:python3.8

COPY requirement.txt /requirement.txt

RUN pip install --no-cache-dir -r /requirement.txt

COPY . /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8080"]
