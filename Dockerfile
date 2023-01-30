FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

COPY . /app/

RUN pip install -U pip
RUN pip install -r requirements.txt

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]