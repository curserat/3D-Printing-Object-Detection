FROM python:3.12
WORKDIR /src

COPY . /src/
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "/src/object-detection/fruit-vision/fruit.py"]