FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000
CMD [ "python3.8", "manage.py", "runserver", "0.0.0.0:8000" ]