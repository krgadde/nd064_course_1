FROM python:3.9
LABEL maintainer="Katie Gamanji"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# command 
CMD ["python", "app.py"]