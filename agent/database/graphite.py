import pickle
import socket
import struct

from database.database import DatabaseClient
from metric.metric import Metric


class GraphiteClient(DatabaseClient):
  def __init__(self, address, port):
    self.address = address
    self.port = port

    self.sock = socket.socket()
    try:
        self.sock.connect((self.address, self.port))
    except socket.error:
      raise SystemExit("Couldn't connect to {server} on port {port}".format(self.address, self.port))

  @staticmethod
  def db_type():
    return 'graphite'

  def push(self, tuples):
    payload = pickle.dumps(tuples, protocol=2)
    header = struct.pack("!L", len(payload))
    self.sock.sendall(header)
    self.sock.sendall(payload)

  def push_metrics(self, metrics):
    tuples = []
    for metric in metrics:
      tuples.append(metric.graphite_format(pickle=True))
    self.push(tuples)
