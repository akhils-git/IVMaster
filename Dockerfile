# FROM python:3.8-alpine

FROM python
RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install openai
# RUN pip install face-recognition

RUN mkdir /app
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -U Flask
RUN pip install -U datetime
# RUN pip install -U numpy
# RUN pip install -U pandas
CMD ["python", "index.py"]
