web: gunicorn Advoget.wsgi --chdir backend --limit-request-line 8188 --log-file -
worker: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=Advoget worker --loglevel=info
beat: REMAP_SIGTERM=SIGQUIT celery --workdir backend --app=Advoget beat -S redbeat.RedBeatScheduler --loglevel=info
