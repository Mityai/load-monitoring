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
    return self

  def graphite_format(self, prefix='', pickle=False):
    ts = int(self.timestamp.timestamp())

    name = self.name
    if prefix:
      name = '{prefix}.{name}'.format(prefix=prefix, name=name)

    if pickle:
      return (name, (ts, self.value))

    return '{name} {value} {timestamp}'.format(name=name,
                                               value=self.value,
                                               timestamp=ts)
