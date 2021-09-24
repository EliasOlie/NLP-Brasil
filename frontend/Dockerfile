FROM node:12

WORKDIR /front

COPY ./package.json /front

RUN npm install

COPY . .

EXPOSE 8080

CMD ["yarn", "start"]