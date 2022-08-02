FROM python:3.9

# load necessary packages
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip \
	&& pip3 install -r /app/requirements.txt
COPY . /app
WORKDIR /app

EXPOSE 8080

CMD ["gunicorn",\
	"-b", "0.0.0.0:8080",\
	"api:api",\
	"--workers=1",\
	"--threads=10",\
	"--worker-class=gthread"]
