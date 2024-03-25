# syntax=docker/dockerfile:1

FROM python
WORKDIR /app
COPY . /app

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/docker-service-account.json
RUN pip3 install -r requirements.txt
EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
