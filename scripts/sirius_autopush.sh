#!/bin/bash

cd ~/runtime/Sirius || exit 1

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

git add .

git commit -m "AUTO-SYNC RUNTIME ${TIMESTAMP}" || true

git push origin sirius-runtime-fabric --tags
