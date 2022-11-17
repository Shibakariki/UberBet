# start by pulling the python image
FROM python:3.8.8

RUN mkdir /code

WORKDIR /code

ADD requirements.txt /code/


RUN /usr/local/bin/python -m pip install --upgrade pip

RUN apt-get install default-libmysqlclient-dev
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

ADD . /code/

EXPOSE 5000
#COPY sshd_config /etc/ssh/sshd_config

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]