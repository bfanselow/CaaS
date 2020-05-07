# CaaS
### Simple Calculator-As-A-Service with Falcon

## Types of problems, map to API resources:
```
  /calc/<problem>
  Examples:
  /calc/2+3
  /cacl/sin(30)?units=(rad|deg)
```
---
## There a 9 different caculator problem types:
  + addition: 1+2
  + subtraction: 3-2
  + multiplication: 4*5
  + division: 6/2
  + powers: 2^5
  + roots: (can use inverse power syntax or **root<x>(y)** to specify the x root of y) 
    - square-root root2(9) = 3 = 9^(1/2)
    - cube-root root3(27) = 3 = 27^(1/3)
  + sin(N) (defaults to units of degrees. Add query string "?units=rad" for radians
  + cos(N)
  + tan(N)

## Combinations
Use parens to group multiple operations according to standard mathematical grouping rules:
Examples
```
 Problem: (sin(45)*(2^5))/(10-8)^2 
 Answer:  (.5)*(32)/4  =  16/4  =  4
```
---
### Setup
```
 $ git clone https://github.com/bfanselow/CaaS.git
 $ cd pGaaS/
 $ virtualenv -p python3 venv
 $ source venv/bin/activate
 (venv) $ pip install -r requirements.txt
```

---
### Run the service (default bind is 127.0.0.1:8080)
```
 (venv) $ gunicorn app:api [-b <ip>:<port>]
```

---
### Testing (pytest)



---
### Examples
Simple addition:
```
curl http://127.0.0.1:8080//calc/simple/(2+3)
{"problem":"(2+3)", "answer":5}
```
Complex associative problem:
```
curl http://127.0.0.1:8080//calc/simple/((2+4)/(9-6))+4
{"problem":"((2+3)/(9-7))+4", "answer":7}
```
Simple powers:
```
curl http://127.0.0.1:8080//calc/simple/2^5
{"problem":"2^5", "answer":32}
```
