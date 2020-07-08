server:
	docker-compose up server

build:
	docker-compose run build

format-md:
	docker-compose run format-md

lint-md:
	docker-compose run lint-md

permissions:
	sudo chown -R $$USER:$$USER .

hugo_shell:
	docker run --rm -it \
      -v $(pwd):/src \
      klakegg/hugo:0.73.0-alpine \
      shell