# syntax=docker/dockerfile:1

FROM python
WORKDIR /app
COPY . /app

# Install Cloud SQL Proxy
RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O cloud_sql_proxy && \
    chmod +x cloud_sql_proxy

COPY docker-service-account.json /cloudsql/key.json

ENV GOOGLE_APPLICATION_CREDENTIALS=/cloudsql/key.json

RUN pip3 install -r requirements.txt
EXPOSE 8080


# Start Cloud SQL Proxy & Flask app using a shell script
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
