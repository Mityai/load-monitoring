class Aggregator(object):
  def __init__(self, config):
    raise NotImplementedError

  @classmethod
  def type():
    raise NotImplementedError('Specify aggregator type')

  def aggregate(self):
    raise NotImplementedError
