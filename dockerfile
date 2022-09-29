FROM python:3.7
    
COPY ./app/requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r /app/requirements.txt
COPY ./app /app
EXPOSE 8080
WORKDIR /app
RUN chmod +x ./start.sh
CMD ["./start.sh"]