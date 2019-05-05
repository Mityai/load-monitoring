import datetime

from metric.aggregator.aggregator import Aggregator
from metric.holder import MetricHolder
from metric.metric import Metric
from slurm.client import SlurmClient


class SlurmAggregator(Aggregator):
  def __init__(self):
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
    for queue, size in queue_sizes.items():
      metric_holder.add(Metric("{queue}.jobs_num").consume(size, queue.date))
    return metric_holder
