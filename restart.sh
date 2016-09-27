#!/bin/sh
echo 'is Stopping....'
ps aux | grep 'manage.py' | awk '{print "kill -9 "$2";"}' | sh

echo 'restart....'
nohup /root/project/blog_old/manage.py runserver 0.0.0.0:8001 &

echo 'finish!'