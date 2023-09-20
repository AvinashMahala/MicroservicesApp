FROM python:3.10.4
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade -r requirements.txt
COPY . /app

CMD python main.py