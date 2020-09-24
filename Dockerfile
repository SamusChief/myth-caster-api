# Initialize, use Python 3
FROM python:3
ENV PYTHONUNBUFFERED 1

# Create working directory for application code
RUN mkdir /code
WORKDIR /code

# Install requirements and run code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
