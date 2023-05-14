FROM python:3.8-alpine

WORKDIR /DockerHanseiTimetable

COPY requirements.txt .

RUN apk add --no-cache tzdata

ENV TZ=Asia/Seoul

RUN pip install -r requirements.txt

COPY . /DockerHanseiTimetable

CMD ["python", "./main.py"]