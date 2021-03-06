import logging
import pickle
import socket
import struct

from database.database import DatabaseClient
from metric.metric import Metric


class GraphiteClient(DatabaseClient):
  def __init__(self, config):
    self.address = config['address']
    self.port = config['port']

    self.sock = socket.socket()
    try:
        self.sock.connect((self.address, self.port))
    except socket.error:
      raise SystemExit("Couldn't connect to {server} on port {port}".format(self.address, self.port))

  @staticmethod
  def db_type():
    return 'graphite'

  def push_pickle(self, tuples):
    payload = pickle.dumps(tuples, protocol=2)
    header = struct.pack("!L", len(payload))
    self.sock.sendall(header)
    self.sock.sendall(payload)

  def push_metrics(self, metrics, prefix=''):
    tuples = []
    for metric in metrics:
      tuples.append(metric.graphite_format(prefix=prefix, pickle=True))

    logging.debug('Send metrics:\n{}'.format('\n'.join(map(lambda t: str(t), tuples))))
    self.push_pickle(tuples)
