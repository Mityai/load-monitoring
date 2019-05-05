import datetime
import numbers


class Metric(object):
  def __init__(self, name):
    assert isinstance(name, str)

    self.name = name

  def consume(self, value, date=None):
    assert isinstance(value, numbers.Number)
    assert date is None or isinstance(date, datetime.datetime)

    self.value = value
    self.date = date or datetime.datetime.now()
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
