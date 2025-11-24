#!/bin/bash

sleep 3

json=$(curl -s http://127.0.0.1:5000/weather?city=London || true)
html=$(curl -s http://127.0.0.1:5000/weather-ui?city=London || true)

if [[ $json == *"temperature"* ]] && [[ $html == *"<html>"* ]]; then
  echo "Test Passed: Both API and UI working!"
  exit 0
else
  echo "Test Failed!"
  echo "JSON response was: $json"
  echo "HTML response was: $html"
  exit 1
fi
