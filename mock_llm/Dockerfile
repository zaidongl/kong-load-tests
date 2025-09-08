FROM openresty/openresty:1.27.1.1-0-alpine
LABEL image.authors="https://github.com/zaidongl"

EXPOSE 8080
WORKDIR /usr/local/openresty/nginx
RUN mkdir -p /usr/local/openresty/nginx/data
COPY ./mock_response.json ./data/mock_response.json
COPY ./nginx.conf ./conf/nginx.conf


