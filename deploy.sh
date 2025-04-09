#!/bin/bash
docker pull guru5346/txtsumm:latest
docker stop txtsumm || true
docker rm txtsumm || true
docker run -d -p 5000:5000 --name txtsumm guru5346/txtsumm:latest
