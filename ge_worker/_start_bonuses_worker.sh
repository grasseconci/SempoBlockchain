celery -A bonuses worker --loglevel=INFO --concurrency=4 --pool=eventlet -Q=processor