class DatabaseClient(object):
  @staticmethod
  def db_type():
    raise NotImplemented('Specify database name')

  def push_metrics(self, metrics):
    raise NotImplemented
