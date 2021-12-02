FROM node:14.18.1-alpine

WORKDIR /usr/src/mobilenetservice

COPY package*.json ./

RUN apk add --no-cache --virtual .gyp \
        python3 \
        make \
        g++ \
    && npm install \
    && apk del .gyp

COPY ./src ./src

ENTRYPOINT ["node", "/src/main.js"]