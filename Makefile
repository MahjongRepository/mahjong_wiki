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

convert-wiki-to-md:
	docker run --rm --volume "`pwd`:/data" --user `id -u`:`id -g` \
	pandoc/core:2.9.2.1 \
	hugo/content/english/riichi/wiki/daisharin.wiki \
	-o hugo/content/english/riichi/wiki/daisharin.md \
	-f mediawiki \
	-t gfm \
	--wrap preserve \
	--reference-links

shell:
	docker run --rm -it \
      -v $(pwd):/src \
      klakegg/hugo:0.73.0-alpine \
      shell