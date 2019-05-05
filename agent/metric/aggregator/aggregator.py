class Aggregator(object):
  @classmethod
  def type():
    raise NotImplementedError('Specify aggregator type')

  def aggregate(self):
    raise NotImplementedError
