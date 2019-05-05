import datetime
import numbers


class Metric(object):
  def __init__(self, name):
    assert isinstance(name, str)

    self.name = name

  def consume(self, value, timestamp=None):
    assert isinstance(value, numbers.Number)
    assert timestamp is None or isinstance(timestamp, datetime.datetime)

    self.value = value
    self.timestamp = timestamp or datetime.datetime.now()

  def graphite_format(self, pickle=False):
    ts = int(self.timestamp.timestamp())
    if pickle:
      return (self.name, (ts, self.value))
    return '{name} {value} {timestamp}'.format(name=self.name,
                                               value=self.value,
                                               timestamp=ts)
