# OBnk

Online BaNKing REST API

## Docker management

The project is fully dockerized https://docs.docker.com/

Each part of the system is isolated and contained in a docker image.
An image is an inert, immutable, file that's essentially a snapshot of the system. Images are created with the build command, and they'll produce a container when started with run.

All services can communicate to each other through networks and exposed ports, these are the entry points, in this way we can have inter-service communication with the huge advantage of each service having its own custom and isolated container (with own dependencies, processes, file system ...). 

To build the image:

```
docker-compose build
```

To run the container in local environment for development purposes:

```
docker-compose -f docker-compose.yml -f envs/docker-compose.local.yml up -d 
```

Then we will have the http server listening on 127.0.0.1:8000


## Tests

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/0629c9d2abf64d63a63c)

Currently only postman integration tests are available. Run them with:

`./run_tests.sh`

Tests involving user IDs will fail because of the changing UUIDs generated. Currently, you need to specify the different user's ID and auth token manually in Postman.
