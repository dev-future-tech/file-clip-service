# file-clip-service

## Install Conda

## Create Conda Runtime:

```bash
# Create the runtime
$ conda create --name telemetry-api-dev python=3.12

# Activate the runtime
$ conda activate telemetry-api-dev

# Setup dependencies
$ python-m pip install -r requirements.txt
```


## Running the Application

### Without Telemetry

```bash
$ flask --app app --debug run
* Serving Flask app 'app'
 * Debug mode: on
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
INFO:werkzeug: * Restarting with stat
WARNING:werkzeug: * Debugger is active!
INFO:werkzeug: * Debugger PIN: 766-025-122
```

## With Telemetry

```bash
$ opentelemetry-instrument --service_name borrowing-service --logs_exporter otlp flask run -p 5000
 * Debug mode: off
INFO:werkzeug:WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
INFO:werkzeug:Press CTRL+C to quit
```

