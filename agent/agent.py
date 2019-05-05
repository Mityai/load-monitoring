import database
import logging
import metric.aggregator
import time

from metric.metric import Metric


class Agent(object):
  def __init__(self, config):
    self.config = config

    self.cluster = self.config.get('cluster', 'test')
    self.frequency = self.config.get('frequency', 5)

    database_config = self.config['database']
    db_type = database.get_client_type(database_config['type'])
    self.db_client = db_type(database_config['address'], database_config['port'])

    manager_config = self.config['workload_manager']
    self.metrics_aggregator = metric.aggregator.get_aggregator(manager_config['type'])

  def run(self):
    while True:
      try:
        self.tick()
      except Exception as e:
        logging.exception(e)
      time.sleep(self.frequency)

  def tick(self):
    metrics = self.aggregate_stats()
    self.push_to_db(metrics)

  def aggregate_stats(self):
    return self.metrics_aggregator.aggregate()

  def push_to_db(self, metrics):
    self.db_client.push_metrics(metrics, prefix=self.cluster)
