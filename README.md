# CaaS
### Simple Calculator-As-A-Service with Falcon


### Setup
```
 $ git clone https://github.com/bfanselow/CaaS.git
 $ cd pGaaS/
 $ virtualenv -p python3 venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
```

### Run the service (default bind is 127.0.0.1:8080)
```
 (venv) $ gunicorn app:api [-b <ip>:<port>]
```

### Testing (pytest)

