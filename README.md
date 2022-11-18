# Loberta_test_task

Steps to run project locally:

1) Once downloaded, initialize virtual environment

2) create .env file based on .env-template 

3) Install required dependecies via "pip install -r req.txt"

4) run migrations

5) create admin super user

6) start application, NOTE! - use admin credentials to login

7) Start celery beat: `celery -A link_check beat -l info`

8) Start celery worker: `celery -A link_check worker`

p.s. we have data migrations with 4 links to test. 
