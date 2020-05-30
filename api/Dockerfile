# ###############################################
#
# This Dockerfile helps to build an image with 
# necessary dependencies for the api to be 
# funtional.
#
#################################################
FROM python:3.8.1-slim-buster 

ARG UID
ARG GID
ARG USER=api
ARG GROUP=api

COPY requirements.txt /
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Proccesses in containers should be started with a non-root user.
RUN groupadd -g ${GID} ${GROUP} && useradd -m -u ${UID} -g ${GROUP} ${USER}
USER ${USER}

# Copy the project files into the home directory.
WORKDIR /home/${USER}/
COPY . .
CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "--chdir", "src", "main:app" ]
