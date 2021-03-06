# CaaS
## Calculator-As-A-Service.
#### Quick-n-dirty calculator service created for the purpose of exploring the *Falcon* API framework

### Requires:
* python 3.6+
* pip install -r requirements.txt

---
### GET request syntax: 
/calc/\<constant\>   
```
  /calc/pi
  /calc/tau
  /calc/e
```

### POST request syntax: 
```
 -H "Content-Type: application/json" -d '{"problem": "\<problem-expression\>"}' localhost:8080/calc
```
---
### There are 6 different caculator *operations*:
  + addition: 1+2
  + subtraction: 3-2
  + multiplication: 4*5
  + division: 6/2
  + powers: 2^5

  **NOT YET IMPLEMENTED**
  + roots: (can use inverse power syntax or **root\<x\>(y)** to specify the x root of y) 
    - square-root root2(9) = 3 = 9^(1/2)
    - cube-root root3(27) = 3 = 27^(1/3)

### Operator Combinations
Use parens to group multiple operations according to standard mathematical grouping rules:   
**Examples:**
```
 Problem: ((1/2)*(2^5))/(10-8)^2 
 Answer:  (.5)*(32)/4  =  16/4  =  4
```

---
### Setup
```
 $ git clone https://github.com/bfanselow/CaaS.git
 $ virtualenv -p python3 venv
 $ . venv/bin/activate
 (venv) $ pip install -r requirements.txt
```

---
### Run the service with simple_server (binds to **0.0.0.0:8080**)
```
 (venv) cd app/
 (venv) $ python caas.py 
```

### Run with gunicorn (binds to **0.0.0.0:8080**)
```
 (venv) $ ./gunicorn_start.sh
  OR
 (venv) $ cd app 
 (venv) $ gunicorn caas:api [-b <ip>:<port>]
```

### Run in Docker container (binds to **0.0.0.0:8080**)
```
 $ docker build . -t docker-caas
 $ docker run --name caas -d -p 8080:8080 docker-caas
```

---
### Testing (pytest)
TODO

---
### Examples API calls
#### Infomational *index* call:
```
 (venv) $ curl localhost:8080/calc/
 {"type": "info", "message": "GET a math constant (pi,tau,e) as a resource, or POST a math problem in json format - example: {'problem': '(3*3)+2'}"}
```
 
#### GET constant value:
```
 (venv) $ curl localhost:8080/calc/pi
 {"constant": "pi", "value": 3.141592653589793}
```

#### POST invalid expression:
```
 (venv) $ curl -H "Content-Type: application/json" -d '{"problem": "bogus"}' localhost:8080/calc
 {"type": "error", "message": "Request error: Invalid character in expression: [b]"}
```

#### POST simple expression:
```
 (venv) $ curl -H "Content-Type: application/json" -d '{"problem": "2+3"}' localhost:8080/calc
 {"problem": "2+3", "answer": 5.0}
```

#### POST complex expression:
```
 (venv) $ curl -H "Content-Type: application/json" -d '{"problem": "((4+3)-5)^5"}' localhost:8080/calc
 {"problem": "((4+3)-5)^5", "answer": 32.0}
```

#### How complex can we get?:
```
 (venv) $ curl -H "Content-Type: application/json" -d '{"problem": "3*((((4+3)-5)^5)/8)"}' localhost:8080/calc
 {"problem": "(((4+3)-5)^5)/8", "answer": 4.0}
```

### Testing
**Unit-Testing**
``` 
$ python -m pytest -v tests/unit/test_compute.py
$ python -m pytest -v tests/unit/test_compute_exc.py
  OR simply
$ python -m pytest -v tests/unit/
``` 
**Integration-Testing**
``` 
$ python -m pytest -v tests/integration/test_service.py
``` 
