# syntax=docker/dockerfile:1

FROM node:21-alpine3.18

WORKDIR /app

COPY app/public/ /app/public
COPY app/src/ /app/src
COPY app/package.json /app/

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
