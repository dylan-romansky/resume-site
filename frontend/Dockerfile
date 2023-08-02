FROM node:latest AS node

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm config set fetch-retry-mintimeout 1000000;
RUN npm config set fetch-retry-maxtimeout 6000000;
RUN npm config set fetch-timeout 1000000;
RUN npm install
COPY . .
RUN npm run build --prod

#EXPOSE 4200
#CMD ["npm", "start"]

FROM  nginx:alpine
COPY --from=node /app/dist/resume-site /usr/share/nginx/html

EXPOSE 80
