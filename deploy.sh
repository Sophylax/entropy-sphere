#!/bin/sh

python app/bot.py &
python app/web.py &

wait -n
exit $?