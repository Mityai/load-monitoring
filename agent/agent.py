import database
import logging
import time


class Agent(object):
  def __init__(self, config={}):
    self.frequency = config.get('frequency', 5)
    self.db_client = database.get_client(config.get('db_type', 'graphite'))

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
    return [1, 2, 3]

  def push_to_db(self, metrics):
    self.db_client.push_metrics(metrics)
