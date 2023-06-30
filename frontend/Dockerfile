FROM node:latest AS node

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install
COPY . .
RUN npm run build --prod

FROM  nginx:alpine
COPY --from=node /app/dist/resume-site /usr/share/nginx/html
