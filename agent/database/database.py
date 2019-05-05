class DatabaseClient(object):
  @staticmethod
  def db_type():
    raise NotImplementedError('Specify database name')

  def push_metrics(self, metrics, prefix=''):
    raise NotImplementedError
