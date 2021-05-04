FROM python:3.6

RUN mkdir -p /usr/local/WB
RUN pip install flask
RUN pip install flask-sqlalchemy
RUN pip install marshmallow-sqlalchemy
RUN pip install flask_marshmallow
COPY docker-entrypoint.sh /usr/local/bin/
RUN ln -s /usr/local/bin/docker-entrypoint.sh /entrypoint.sh # backwards compat
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

ENTRYPOINT ["docker-entrypoint.sh"]
