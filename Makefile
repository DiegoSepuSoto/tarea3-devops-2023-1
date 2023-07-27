all: test

up:
	docker-compose up -d

down:
	docker-compose down

test:
	make test-1 && make test-2 && make test-3 && make test-4

test-1:
	pytest ./ui-testing/test1_agrega2directores.py

test-2:
	pytest ./ui-testing/test2_agregapelculaLaNaranjaMecnica.py

test-3:
	pytest ./ui-testing/test3_agregapelculaBastardosSinGloria.py

test-4:
	pytest ./ui-testing/test4_agregafilmografaDeChristopherNolan.py