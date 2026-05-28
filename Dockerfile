FROM python:3.13-slim

WORKDIR /runtime

COPY . .

RUN pip install --no-cache-dir -r requirements.lock.txt

CMD ["pytest"]
