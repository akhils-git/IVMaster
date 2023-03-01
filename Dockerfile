# FROM python:3.8-alpine

FROM python
RUN pip install numpy
RUN pip install torch
RUN pip install cv2

RUN mkdir /app
ADD . /app
WORKDIR /app
EXPOSE 5002

CMD ["python", "index.py"]