#!/usr/bin/env python


from prometheus_client import start_http_server, Summary
import random
import time


# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    print(f'process request, sleep {t}s...')
    time.sleep(t)

if __name__ == '__main__':
    print('starting http server')
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        t = int(random.random() * 10)
        process_request(t)
