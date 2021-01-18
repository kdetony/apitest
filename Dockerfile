FROM rackspacedot/python37

WORKDIR /app

COPY api.py  .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3","api.py" ]
