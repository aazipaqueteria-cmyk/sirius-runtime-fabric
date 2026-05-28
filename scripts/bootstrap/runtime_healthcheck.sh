#!/bin/bash

echo "[+] checking runtime"

docker --version || exit 1
python3 --version || exit 1
git --version || exit 1

echo "[OK] runtime stable"
