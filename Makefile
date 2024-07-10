
up:
	docker-compose up -d

down:
	docker-compose down

dev:
	docker exec -it mygptreader-web-1 /bin/bash

logs:
	docker logs -f  mygptreader-web-1

clean:
	docker stop mygptreader-web-1
	docker rm mygptreader-web-1
	docker rmi liyaodev/my-gpt-reader:v1.0.0
