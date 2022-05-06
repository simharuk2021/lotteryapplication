#!/bin/bash
ls -l
source venv/bin/activate
declare -a directories=("front_end_api" "day_api" "numbers_api" "rollover_api")
for dir in "${directories[@]}"
do
  cd ${dir}
  pip3 install -r testing.txt
  python3 -m pytest --cov=application --cov-report=xml --junitxml=junit/test-results.xml
  cd ..
done