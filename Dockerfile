FROM python:3.12.7-bookworm

ADD app.py /
ADD requirements.txt /

RUN python -m pip install -r requirements.txt

EXPOSE 8070

CMD ["opentelemetry-instrument", "--service_name", "borrowing-service", "--logs_exporter", "otlp", "flask", "run", "-p",  "8070"]
