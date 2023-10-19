#!/usr/bin/env bash
# Runs linting scripts and type checking
# black - opinionated code formatter
# ruff - lints, finds mistakes, and sorts import statements
# mypy - checks type annotations

set -e

files=(
  "{{ cookiecutter.package_name }}"
  "tests"
)

# Print out the commands being run
set -x

black "${files[@]}"
ruff --fix "${files[@]}"
mypy "${files[@]}"
