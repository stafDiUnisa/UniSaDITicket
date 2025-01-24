bind = 'unix:/run/gunicorn.sock'
workers = 3
loglevel = 'debug'
accesslog = '/var/log/gunicorn/access_uni_ticket'
acceslogformat ="%(h)s %(l)s %(u)s %(t)s %(r)s %(s)s %(b)s %(f)s %(a)s"
errorlog =  '/var/log/gunicorn/error_uni_ticket'
capture_output=True