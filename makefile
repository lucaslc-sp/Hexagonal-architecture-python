clear:
	@printf "Clearing temp files... "
	@rm -f dist/*.gz
	@rm -rfd *.egg-info
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.log' -delete
	@echo "$(SUCCESS)"

env-switch-dev:
	@echo "switching for DEV..."
	@cp .env.dev .env

env-switch-staging:
	@echo "switching for STAGING..."
	@cp .env.staging .env

env-switch-prod:
	@echo "switching for PRODUCTION..."
	@cp .env.prod .env

system-packages:
	@printf "Instalando 'pip' e 'virtualenv'... "
	@curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	@python3  -q  get-pip.py 1> /dev/null --user
	@pip install -q -U pip
	@pip install -q virtualenv --user
	@rm get-pip.py
	@echo "$(SUCCESS)"

packages: env-create
	@printf "Installing libraries... "
	@venv/bin/pip install -q --no-cache-dir -r requirements-dev.txt
	@echo "$(SUCCESS)"

env-create: env-destroy
	@printf "Creating virtual environment... "
	@virtualenv -q -p python3.6 venv
	@echo "$(SUCCESS)"

env-destroy:
	@printf "Destroying virtual environment... "
	@rm -rfd venv
	@rm -rfd migrations
	@echo "$(SUCCESS)"

install: clear system-packages packages
	@echo "============================================"
	@echo "All right for development environment"
	@echo ""
	@echo "Type to activate the environment: "
	@echo ""
	@echo "source venv/bin/activate"
	@echo "============================================"

docker-up:
	@docker-compose --log-level ERROR up -d

docker-down:
	@docker-compose down