FROM python


RUN pip install prometheus-client

COPY stats.py /app/

CMD ["/app/stats.py"]
