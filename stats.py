#!/usr/bin/env python


import collections
import random
import time

from prometheus_client import Gauge, start_http_server


cpu_metrics = Gauge(
    'instance_fake_cpu_seconds_total', 'Fake amount of CPU used',
    ['project_id', 'resource_type', 'resource_id', 'resource_name']
)

memory_metrics = Gauge(
    'instance_fake_memory_usage_bytes', 'Fake amount of memory used',
    ['project_id', 'resource_type', 'resource_id', 'resource_name']
)


def update_stats():
    cpu_data = collections.defaultdict(int)

    for project in ('my-project0', 'my-project1', 'my-project2'):
        for node in range(10):
            val = int(random.random() * 100)

            cpu_data[node] += val

            print(f'Set cpu={cpu_data[node]} and memory={val} for {node}')
            cpu_metrics.labels(
                project_id=project,
                resource_type='instance_fake_monitoring',
                resource_id=f'fffffff-fffff-{node}',
                resource_name=f'Server {node}'
            ).set(cpu_data[node])

            memory_metrics.labels(
                project_id=project,
                resource_type='instance_fake_monitoring',
                resource_id=f'fffffff-fffff-{node}',
                resource_name=f'Server {node}'
            ).set(val)


if __name__ == '__main__':
    start_http_server(8000)
    while True:
        update_stats()
        time.sleep(1)
