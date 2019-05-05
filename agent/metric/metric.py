import datetime
import numbers


class Metric(object):
  def __init__(self, name):
    assert isinstance(name, str)

    self.name = name

  def set_value(self, value, timestamp=None):
    assert isinstance(value, numbers.Number)
    assert timestamp is None or isinstance(timestamp, datetime.datetime)

    self.value = value
    self.timestamp = timestamp or datetime.datetime.now()

  def graphite_format(self):
    return '{name} {value} {timestamp}'.format(name=self.name,
                                               value=self.value,
                                               timestamp=int(self.timestamp.timestamp()))
