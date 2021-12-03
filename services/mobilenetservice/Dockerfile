FROM node:14.18.1

WORKDIR /usr/src/mobilenetservice

COPY package*.json ./

RUN npm install

COPY ./src ./src

ENTRYPOINT ["node", "src/main.js"]