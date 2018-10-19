FROM ubuntu:latest
RUN apt-get update -y && \
    apt-get install -y python3-pip python-dev build-essential
COPY calc /app
WORKDIR /app
RUN pip3 install --proxy=$http_proxy -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["calculator.py"]
