FROM tiangolo/uwsgi-nginx-flask:python3.9
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install --no-cache-dir -r /var/www/requirements.txt
COPY ./app /app
