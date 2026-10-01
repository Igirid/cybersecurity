FROM alpine:latest

RUN apk add python3 py3-pip

COPY . /src

WORKDIR /src

RUN python3 -m venv .venv

RUN .venv/bin/pip install -r requirements.txt

# EXPOSE 8080

CMD [".venv/bin/python", "solution.py"]
# CMD ["python3", "solution.py"]