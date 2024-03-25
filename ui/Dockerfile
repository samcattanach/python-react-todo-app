# syntax=docker/dockerfile:1

FROM node:21-alpine3.18

WORKDIR /app

COPY app/public/ /app/public
COPY app/src/ /app/src
COPY app/package.json /app/

RUN npm install

# pass in API endpoint
ARG FLASK_APP_URL
RUN echo "FLASK_APP_URL=${FLASK_APP_URL}" > .env


EXPOSE 3000

CMD ["npm", "start"]
