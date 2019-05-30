class DatabaseClient(object):
  def __init__(self, config):
    raise NotImplementedError

  @staticmethod
  def db_type():
    raise NotImplementedError('Specify database name')

  def push_metrics(self, metrics, prefix=''):
    raise NotImplementedError
