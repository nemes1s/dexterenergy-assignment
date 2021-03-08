FROM python:latest
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY main.py /code/main.py
COPY run.sh /code/run.sh
COPY lasttimestamp_base.txt /code/lasttimestamp.txt

CMD ["/code/run.sh"]