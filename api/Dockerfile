FROM python:3.8.1-slim-buster 

ARG UID
ARG GID
ARG USER=default
ARG GROUP=default

RUN groupadd -g ${GID} ${GROUP} && useradd -m -u ${UID} -g ${GROUP} ${USER}
USER ${USER}
WORKDIR /home/${USER}/api
COPY requirements.txt .
RUN pip install --upgrade pip --user && pip install --no-cache-dir -r requirements.txt
ENV PATH /home/${USER}/.local/bin:${PATH}
CMD flask run --host=0.0.0.0
