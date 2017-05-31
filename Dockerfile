FROM python:2-alpine
WORKDIR /
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY __main__.py .
CMD [ "python", "__main__.py" ]
EXPOSE 8080
