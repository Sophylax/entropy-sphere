#!/bin/bash

python -m http.server 80 &
python app/bot.py