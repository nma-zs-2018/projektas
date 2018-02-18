 FROM python:3
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /code


 ADD requirements.txt /code/
 RUN pip install -r requirements.txt
WORKDIR /code
 ADD . /code/

 CMD python3 manage.py runserver 0.0.0.0:8000