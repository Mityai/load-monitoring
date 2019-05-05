from database.database import DatabaseClient
from metric.metric import Metric


class GraphiteClient(DatabaseClient):
  @staticmethod
  def db_type():
    return 'graphite'

  def push_raw(self, raw):
    print(raw)

  def push_metric(self, metric):
    assert isinstance(metric, Metric)

    self.push_raw(metric.graphite_format())

  def push_metrics(self, metrics):
    for metric in metrics:
      self.push_metric(metric)
