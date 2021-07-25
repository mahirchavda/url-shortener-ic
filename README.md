# URL Shortener REST API

## Installation

### Locally
* Create a python virtual environment.
* Update the _SHORTENER_WEB_SERVER_ value in the __.flaskrun__ file.
* Install dependencies
```
pip install -r requirements.txt
```
* Run flask server
```
flask run --host=0.0.0.0
```

### Using Docker
* Update the _SHORTENER_WEB_SERVER_ value in the __.flaskrun__ file.
* Create a urlshortener container
```
docker-compose up
```

## Testing

### Sample curl command

```bash
curl http://127.0.0.1:5000/api/shorten -X POST -H 'Content-Type:application/json' -d '{"url":"https://google.com"}'  
```

### Using pytest
* Install dev dependencies
```
pip install -r requirements_dev.txt
```
* Run test cases
```
pytest -v
```
