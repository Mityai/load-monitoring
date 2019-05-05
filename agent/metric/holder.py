class MetricHolder(dict):
  def add(self, metric):
    assert metric.name not in self
    self[metric.name] = metric
    return self

  def merge(self, other):
    for name, metric in other.items():
      assert name not in self
      self[name] = metric
    return self

  def metrics(self):
    return list(self.values())
