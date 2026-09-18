FROM python

WORKDIR /app

COPY ./src/requirements.txt .

RUN pip install -r requirements.txt

COPY ./src/main.py .

EXPOSE 5000

CMD ["python3","main.py"]