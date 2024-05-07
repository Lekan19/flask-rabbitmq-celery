## Project description
Created a straightforward API featuring a route for transmitting two integer values, which are then dispatched to a decoupled Messaging service. Within this setup, a dedicated worker undertakes the task of summing the two integers together.
### Tools: flask, flask-restx, celery, Rabbitmq, and DOcker
### Build docker images
Building flask-api image
```
docker build -t api-add .
```

Building the celery worker image
```
cd celerytask
docker build -t celery-add .
```
### Deploying docker services
```
docker stack deploy -c docker-compose/local-compose.yaml add

```

### Testing API
POST request to /api/addition
```
curl --request POST \
  --url http://127.0.0.1:8000/api/addition \
  --header 'Content-Type: application/json' \
  --data '{"x": 3, "y":3}'
```
GET request/api/result/<task_id>
```
curl --request GET \
  --url http://127.0.0.1:8000/api/result/<task_id>
```
