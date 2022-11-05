# start by pulling the python image
FROM python:3.8.8

# copy the requirements file into the image
COPY ./requirements.txt /app/requirements.txt
COPY ./app /app

# switch working directory
WORKDIR /app

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN apt-get install default-libmysqlclient-dev
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . /app

# configure the container to run in an executed manner
ENTRYPOINT [ "python" ]

CMD ["app.py" ]