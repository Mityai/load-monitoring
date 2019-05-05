from metric.aggregator.slurm import SlurmAggregator

AGGREGATORS = {
  SlurmAggregator.type(): SlurmAggregator,
}

def get_aggregator(manager_type):
  return AGGREGATORS[manager_type]()
