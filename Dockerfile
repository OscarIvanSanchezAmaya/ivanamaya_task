FROM python:3
WORKDIR /srv/app
COPY app.py resume_OscarIvanSanchezAmaya.pdf ./
#RUN pip3 install --upgrade pip
RUN pip3 install flask --progress-bar off
RUN pip3 install waitress --progress-bar off
CMD [ "python" , "./app.py" ]