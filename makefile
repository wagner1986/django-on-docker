file= docker-compose.yml
file-prod= docker-compose.prod.yml
compose-file= $(file-prod)

build:
	docker-compose -f $(compose-file) build

up:
	docker-compose -f $(compose-file)  stop && docker-compose -f $(compose-file)  up -d --build

daemon:
	docker-compose -f $(compose-file)  up

start:
	docker-compose -f $(compose-file)  start

stop:
	docker-compose -f $(compose-file)  stop

restart:
	docker-compose -f $(compose-file)  stop && docker-compose -f $(compose-file)  start

shell-nginx:
	docker exec -ti aws_nx01 /bin/sh

shell-web:
	docker exec -ti aws_dz01 /bin/sh

shell-db:
	docker exec -ti aws_db01 /bin/sh

log-nginx:
	docker-compose logs aws_nx01  

log-web:
	docker-compose logs webapp  

log-db:
	docker-compose logs db

collectstatic:
	docker exec aws_dz01 /bin/sh -c "python manage.py collectstatic --noinput"  

createuser:
	docker-compose run webapp python /srv/starter/manage.py createsuperuser 
