[tool.poetry]
name = "financial-mng"
version = "0.1.0"
description = "API developed for family financial management"
authors = ["jcosta86 <costa.jeff1986@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.10.*"
fastapi = "^0.111.0"
uvicorn = "^0.30.1"


[tool.poetry.group.dev.dependencies]
pytest = "^8.2.2"
pytest-cov = "^5.0.0"
taskipy = "^1.13.0"
ruff = "^0.5.1"
httpx = "^0.27.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.ruff]
line-length = 79
extend-exclude = ['migrations']

[tool.ruff.lint]
preview = true
select = ['I', 'F', 'E', 'W', 'PL', 'PT']

[tool.ruff.format]
preview = true
quote-style = 'single'

[tool.pytest.ini_options]
pythonpath = "."
addopts = '-p no:warnings'

[tool.taskipy.tasks]
lint = 'ruff check . && ruff check . --diff'
format = 'ruff check . --fix && ruff format .'
run = 'fastapi dev fast_zero/app.py'
pre_test = 'task lint'
test = 'pytest -s -x --cov=fast_zero -vv'
post_test = 'coverage html'
