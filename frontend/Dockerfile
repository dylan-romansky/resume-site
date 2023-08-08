FROM node:latest AS node

WORKDIR /app

COPY package.json package-lock.json ./
#the following are to make the build not fail on bad
#internet connections, like the ones I'm often stuck with
RUN npm config set fetch-retry-mintimeout 1000000;
RUN npm config set fetch-retry-maxtimeout 6000000;
RUN npm config set fetch-timeout 1000000;
RUN npm install
COPY . .
RUN npm run build --prod
#RUN npm build --omit=dev

#EXPOSE 4200
#CMD ["npm", "start"]

FROM  nginx:alpine
COPY --from=node /app/dist/resume-site /opt/resume-site
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
