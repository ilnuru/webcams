FROM nginx:1.15.5-alpine

RUN mkdir /static/ /media_app/

COPY default.conf /etc/nginx/conf.d/default.conf

VOLUME /static/

VOLUME /media_app/

CMD ["nginx", "-g", "daemon off;"]
