from database import DatabaseClient

class GraphiteClient(DatabaseClient):
  def __init__(self):
    pass

  @staticmethod
  def db_type():
    return 'graphite'

  def push_metrics(self, metrics):
    print('metrics len {}'.format(len(metrics)))
    pass
