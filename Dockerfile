# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Warning: A port below 1024 has been exposed. This requires the image to run as a root user which is not a best practice.
# For more information, please refer to https://aka.ms/vscode-docker-python-user-rights`
EXPOSE 80

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# update pip
RUN python -m pip install -U pip setuptools wheel

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# install gunicorn
RUN python -m pip install gunicorn

WORKDIR /app
COPY . /app

# install breeze
RUN python -m pip install -e .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:80", "wsgi:app"]
