@echo off
echo Running pytest with coverage...
coverage run -m pytest
coverage report -m
coverage html
start htmlcov\index.html
