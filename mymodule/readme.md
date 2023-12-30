#installation on ubuntu
sudo apt-get install redis
sudo apt-get install celery

#version check
redis-cli --version

#start redis server
sudo systemctl status redis

#start redis client
redis-cli

#project side requirement
pip3 install redis
pip3 install celery


#start of celery
__cmd_terminal__
celery -A tasks worker --pool-prefork --loglevel=info --concurrency=29

__on_program_py_file__
app.worker_main(["worker", '--loglevel=INFO', '--include=tasks', '--concurrency=20']) #direct calling from program


#some important commands
keys agen* 
keys *
config set maxmemory 9999
config rewrite
config set stop-write-on-bgsave-errorno
SET mykey "Hello World"  ---> GET mykey
