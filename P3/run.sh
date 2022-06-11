#!/bin/bash

#Run

docker build -t simplehttpserver .

docker run -p 8000:8000 simplehttpserver
