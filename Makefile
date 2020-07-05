server:
	docker-compose up server

build:
	docker-compose run build

shell:
	docker run --rm -it \
      -v $(pwd):/src \
      klakegg/hugo:0.73.0-alpine \
      shell