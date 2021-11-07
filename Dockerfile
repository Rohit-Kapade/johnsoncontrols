FROM alpine:latest

RUN apk add bash
RUN apk add --no-cache python3-dev
RUN apk add py3-pip

RUN pip3 install --no-cache --upgrade pip setuptools
RUN pip install flask

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]


