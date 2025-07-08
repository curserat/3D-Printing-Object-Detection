FROM python:3.12
WORKDIR /src

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python3", "/src/object-detection/fruit-vision/fruit.py"]