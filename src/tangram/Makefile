DOCKERVER :=`cat VERSION`
.DEFAULT_GOAL := docker

docker:
	docker build  --tag="fils/p418tangram:$(DOCKERVER)"  --file=./Dockerfile .

dockerlatest:
	docker build  --tag="fils/p418tangram:latest"  --file=./build/Dockerfile .

publish: docker
	docker push fils/p418tangram:$(DOCKERVER)

tag:
	docker tag fils/p418tangram:$(DOCKERVER) gcr.io/top-operand-112611/p418tangram:$(DOCKERVER)

publishgcr: 
	docker push gcr.io/top-operand-112611/p418tangram:$(DOCKERVER)
