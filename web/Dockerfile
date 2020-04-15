FROM node:12.16.1-buster-slim

RUN npm install -g @vue/cli

WORKDIR /home/node/web
COPY package.json .
RUN npm install
USER node
CMD npm run serve
