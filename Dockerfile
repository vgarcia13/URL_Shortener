FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
COPY dockerutils/wait-for-postgres.sh /dockerutils/wait-for-postgres.sh
RUN chmod +x dockerutils/wait-for-postgres.sh
# Set the timezone.
ENV TZ=America/Mexico_City
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
