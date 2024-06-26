#!/bin/bash

source myenv/bin/activate
python -m pip install -r requirements.txt
python3 words.py
deactivate
