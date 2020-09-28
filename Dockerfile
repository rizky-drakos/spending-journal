FROM node:latest as builder
# Copy WEB code to the right place.
WORKDIR /app
COPY web .
# Install WEB's dependencies and build.
RUN npm install && npm run build


FROM heroku/heroku:16
# Install Vim, Nginx, Python3.6 and Pip.
RUN apt update && apt-get install software-properties-common --yes && \
    add-apt-repository ppa:deadsnakes/ppa && apt update && \
    apt-get install python3.6 --yes && \
    apt install python3-pip --yes && \
    apt install nginx --yes && \
    apt install vim --yes
# Configure NGINX and copy WEB artifacts to the right place.
RUN sed -i '62d' /etc/nginx/nginx.conf
COPY web/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist /usr/share/nginx/html
# Copy the API code and install its dependencies.
WORKDIR /api
COPY api .
RUN python3.6 -m pip install -r /api/requirements.txt
# Enable Heroku Exec.
COPY heroku-exec.sh /app/.profile.d/heroku-exec.sh
RUN chmod +x /app/.profile.d/heroku-exec.sh && \
    rm /bin/sh && ln -s /bin/bash /bin/sh
# Start NGINX and API servers.
CMD gunicorn --bind 0.0.0.0:5000 --chdir src main:app --daemon && \
    service ssh start && \
    sed -i -e "s/__PORT__/${PORT}/g" /etc/nginx/conf.d/default.conf \
    && nginx -g 'daemon off;'