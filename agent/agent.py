import database
import logging
import time

from metric.metric import Metric


class Agent(object):
  def __init__(self, config):
    self.frequency = config.get('frequency', 5)

    database_config = config.get('database', {})
    db_type = database.get_client_type(database_config.get('type', 'graphite'))
    self.db_client = db_type(database_config['address'], database_config['port'])

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
    m1 = Metric('local.random.diceroll')
    m1.consume(1488)
    return [m1]

  def push_to_db(self, metrics):
    self.db_client.push_metrics(metrics)
