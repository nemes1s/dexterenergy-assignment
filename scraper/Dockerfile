# FROM python:latest
# RUN apt-get update && apt-get -y install cron
# WORKDIR /code
# ADD requirements.txt /code/requirements.txt
# RUN pip install -r /code/requirements.txt
# COPY main.py /code/main.py
# COPY lasttimestamp_base.txt /code/lasttimestamp.txt
# COPY crontab /etc/cron.d/crontab
# RUN chmod 0644 /etc/cron.d/crontab
# RUN /usr/bin/crontab /etc/cron.d/crontab

# CMD ["cron", "-f"]

FROM python:latest
# RUN apt-get update && apt-get -y install cron
WORKDIR /code
ADD requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt
COPY main.py /code/main.py
COPY run.sh /code/run.sh
COPY lasttimestamp_base.txt /code/lasttimestamp.txt
# COPY crontab /etc/cron.d/crontab
# RUN chmod 0644 /etc/cron.d/crontab
# RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["/code/run.sh"]