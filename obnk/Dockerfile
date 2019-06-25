FROM python:2.7.10-slim
MAINTAINER Pol Alvarez <pol.avms@gmail.com>

# Install the os requirements
RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -qq -y build-essential libpq-dev postgresql-client-9.4 gcc python-setuptools python-dev libffi-dev libpango1.0-0 libcairo2 vim libav-tools netcat

RUN easy_install pip && pip install --upgrade pip
# Create the intall path
RUN mkdir -p /data/obnk
# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /data/obnk
COPY . /data/obnk
ADD config/run.sh /run.sh
ADD config/wait-for.sh /wait-for.sh
RUN chmod +x /run.sh
RUN chmod +x /wait-for.sh
CMD /run.sh
