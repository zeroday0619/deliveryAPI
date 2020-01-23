![python 3.7](https://img.shields.io/badge/Python-3.7-blue.svg) ![version dev](https://img.shields.io/badge/version-dev-green.svg)

delivery API for Python
===================
## install
```
pip3 install pipenv
pip install pipenv
```
```
$ pipenv install
$ pipenv shell
$ python3 run.py
or
$python run.py
```

## 사용법
[https://api.zeroday0619.kr/v1/tracking](https://api.zeroday0619.kr/v1/tracking)

0 => DHL\n
1 => CJ 대한통운

###HTTP
```http
GET /v1/tracking HTTP/1.1
Content-Type: application/json
{
    "code": 0,
	"track_id": "0000000000"
}
```
### Python3
```python3
import requests

url = "https://api.zeroday0619.kr/v1/tracking"
payload = {
    "code": 0,
	"track_id": "0000000000"
}
headers = {
    'Content-Type': "application/json",
}
response = requests.request("GET", url, json=payload, headers=headers)
print(response.json())
```
### node.js
```node.js
var request = require("request");

var options = { method: 'GET',
  url: 'https://api.zeroday0619.kr/v1/tracking',
  headers: {
  'Content-Type': 'application/json'
  },
  body: { code: 0 ,track_id: '0000000000' },
  json: true 
};

request(options, function (error, response, body) {
  if (error) throw new Error(error);
  console.log(body);
});
```

## Response
```json
{
    "timestemp": "2020-01-04 22:11:23",
    "tracking": [
        {
            "from": {
                "origin": "SHANGHAI - SHANGHAI - CHINA MAINLAND"
            },
            "to": {
                "destination": "SEOUL - SEOUL - KOREA, REPUBLIC OF (SOUTH K.)"
            },
            "state": {
                "DeliveryStatus": "transit",
                "description": "발송물이 목적지 또는 경유지로 발송되었습니다. SHANGHAI - CHINA MAINLAND",
                "location": "SHANGHAI - CHINA MAINLAND",
                "date": "목요일, 1월 02, 2020 ",
                "time": "17:21"
            }
        }
    ]
}
``
