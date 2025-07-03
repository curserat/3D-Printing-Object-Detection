FROM python:3.12
WORKDIR /src

COPY /object-detection /src/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "script.py"]