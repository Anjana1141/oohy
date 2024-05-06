FROM node:14
WORKDIR /usr/src/app
COPY app.js /usr/src/app/
EXPOSE 3000
CMD ["node", "app.js"]
