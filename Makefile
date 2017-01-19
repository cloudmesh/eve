UNAME=$(shell uname)
export ROOT_DIR=${PWD}/cloudmesh_eve
MONGOD=mongod --dbpath ~/.cloudmesh/data/db --bind_ip 127.0.0.1
EVE=cd $(ROOT_DIR); python run.py

define banner
	@echo
	@echo "###################################"
	@echo $(1)
	@echo "###################################"
endef

ifeq ($(UNAME),Darwin)
define terminal
	osascript -e 'tell application "Terminal" to do script "$(1)"'
endef
endif
ifeq ($(UNAME),Linux)
define terminal
	echo "Linux not yet supported, fix me"
endef
endif
ifeq ($(UNAME),Windows)
define terminal
	echo "Windows not yet supported, fix me"
endef
endif



setup:
	# brew update
	# brew install mongodb
	# brew install jq
	rm -rf ~/.cloudmesh/data/db
	mkdir -p ~/.cloudmesh/data/db

kill:
	killall mongod

mongo:
	$(call terminal, $(MONGOD))

eve:
	$(call terminal, $(EVE))

deploy: setup mongo eve
	echo deployed

test:
	$(call banner, "SERVICE")
	curl -s -i http://127.0.0.1:5000 
	$(call banner, "PEOPLE")
	@curl -s http://127.0.0.1:5000/people  | jq
	$(call banner, "CLUSTER")
	@curl -s http://127.0.0.1:5000/cluster  | jq
	$(call banner, "COMPUTER")
	@curl -s http://127.0.0.1:5000/computer  | jq

clean:
	rm *~


genie:
	git clone https://github.com/drud/evegenie.git
	cd evegenie; pip install -r requirements.txt
json:
	python evegenie/geneve.py sample.json
	less sample.settings.py
