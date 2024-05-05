FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /api-gateway
WORKDIR /api-gateway
COPY requirements.txt /soap-service/
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . /soap-service/
ARG URL=0.0.0.0:9000
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 9000 --reload"] 