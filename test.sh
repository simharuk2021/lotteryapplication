#!/bin/bash
declare -a directories=("front_end_api" "day_api" "numbers_api" "rollover_api")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 
  sudo apt-get install python3-pip 
  sudo apt-get install python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip install -r testing.txt
  python3 -m pytest --cov=application --cov-report=xml --junitxml=junit/test-results.xml
  deactivate
  cd ..
done