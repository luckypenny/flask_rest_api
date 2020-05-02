# Predictor (DevOps Engineer Task)

참고) model.py 리턴값을 (0~100) 사이로 랜덤하게 리턴하도록 수정

## Installation (git clone)
- Clone this source code.
```
$ git clone https://github.com/luckypenny/flask_rest_api.git
```

## Running (docker container)
- Run docker container(s) using docker compose file.
```
$ cd flask_rest_api
$ docker-compose up -d 
```

## Testing (curl)
- Request HTTP POST for predictions.
```
$ curl -H "Content-Type: application/json" --request POST -d '{"url":"https://upload.wikimedia.org/wikipedia/commons/c/c0/Douglas_adams_portrait_cro pped.jpg"}' http://localhost:5000/predictions
{"id": 0}
```
- Get the predicted result by HTTP GET.
```
$ curl http://localhost:5000/predictions/0
{"age": 42}
```
