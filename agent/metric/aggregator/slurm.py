import datetime

from metric.aggregator.aggregator import Aggregator
from metric.holder import MetricHolder
from metric.metric import Metric
from slurm.client import SlurmClient


class SlurmAggregator(Aggregator):
  def __init__(self, config):
    self.client = SlurmClient()

  @staticmethod
  def type():
    return "slurm"

  def aggregate(self):
    queue = self.client.queue()

    metrics = MetricHolder()

    metrics.merge(self._queue_sizes(queue))

    return metrics.metrics()

  def _queue_sizes(self, queue):
    queue_sizes = {}
    for job in queue.jobs:
      if job.partition not in queue_sizes:
        queue_sizes[job.partition] = 0
      queue_sizes[job.partition] += 1

    metric_holder = MetricHolder()
    for queue_name, size in queue_sizes.items():
      metric_holder.add(Metric('{queue}.jobs_num'.format(queue=queue_name)).consume(size, queue.date))
    return metric_holder
