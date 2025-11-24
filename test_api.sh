#!/bin/bash

json=$(curl -s http://127.0.0.1:5000/weather?city=London || true)
html=$(curl -s http://127.0.0.1:5000/weather-ui?city=London || true)

# Check wildcard match (correct way)
if [[ $json == *"temperature"* ]] && [[ $html == *"<html>"* ]]; then
  echo "Test Passed: Both API and UI working!"
  exit 0
else
  echo "Test Failed!"
  echo "JSON Response: $json"
  echo "HTML Response: $html"
  exit 1
fi
