#!/bin/bash

python app/bot.py &
python -m http.server 80 &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?