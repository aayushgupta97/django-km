FROM python:3.6-alpine

# install necessary packages
RUN set -x 										&&	\
	apk add --no-cache --virtual .build-deps 		\
	python 											\
	py-pip

COPY ./ /opt/

WORKDIR /opt/

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["manage.py", "runserver", "0.0.0.0:8000"]

ENTRYPOINT ["python"]