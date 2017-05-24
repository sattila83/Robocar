#!/bin/bash

rm -rf *.pyc
rm -rf test_*.py
rm -rf RPi
rm -rf __pycache__

python main.py positions.in
