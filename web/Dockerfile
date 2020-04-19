FROM node:12.16.1-buster-slim as builder

WORKDIR /app

COPY package.json .
RUN npm install --silent
RUN npm install -g @vue/cli

COPY . .
RUN npm run build

FROM nginx:mainline
COPY --from=builder /app/dist /usr/share/nginx/html

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d