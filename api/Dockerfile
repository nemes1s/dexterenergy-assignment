FROM python:3.7

EXPOSE 8081

COPY ./app /app
ADD requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
