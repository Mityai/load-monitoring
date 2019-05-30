# Agent for collecting metrics about cluster load

## Description
Background daemon for collecting statistics about cluster load and sending aggregated metrics to specified database.
Implemented module for collecting statistics for SLURM based clusters and module for sending collected metrics to Graphite database.
Also it is easy to implement your own modules.

## Requirements
* `python 3.3` or higher

## Run command

### Using start/restart/stop scripts
To start daemon use command
```
./bin/start.sh --config <path/to/config.json> [--debug]
```

To stop running daemon use command
```
./bin/stop.sh
```

To restart running daemon use command
```
./bin/restart.sh --config <path/to/config.json> [--debug]
```

Read about passed parameters below.

### Manual
```
python3 __main__.py --config <path/to/config.json> [--debug]
```

* `--debug` for testing purposes (pushes statistics for cluster with name **test**)

## Configuration file

* `cluster`: name of cluster, this name will be a prefix for all collected metrics
* `frequency`: collect metrics every `frequency` seconds
* `database`: config for database module; `type` field must be equal to return value of [`db_type` method](https://github.com/Mityai/tmp-load/blob/master/agent/database/database.py#L4) of database module desired to use
* `workload_manager`: config for workload manager module; `type` field must be equal to return value of [`type` method](https://github.com/Mityai/tmp-load/blob/master/agent/metric/aggregator/aggregator.py#L4) of workload manager module desired to use

## Customization

Architecture provies an easy way to implement your own modules for collecting statistics and for sending it to your type of database.

### Collecting
To implement your own module just write a class in [metrics/aggregator](https://github.com/Mityai/tmp-load/tree/master/agent/metric/aggregator) inherited from [metric/aggregator/aggregator.py:Aggregator](https://github.com/Mityai/tmp-load/blob/master/agent/metric/aggregator/aggregator.py).
Then register it by adding to [`AGGREGATORS`](https://github.com/Mityai/tmp-load/blob/master/agent/metric/aggregator/__init__.py#L3) dictionary.
After that you can use it by setting `workload_manager.type` in config file to corresponding type name specified in `type` method.

### Database Client
To implement your own module just write a class in [database](https://github.com/Mityai/tmp-load/tree/master/agent/database) inherited from [database/database:DatabaseClient](https://github.com/Mityai/tmp-load/blob/master/agent/database/database.py).
Then register it by adding to [`DB_CLIENTS`](https://github.com/Mityai/tmp-load/blob/master/agent/database/__init__.py#L3) dictionary.
After that you can use it by setting `database.type` in config file to corresponding type name specified in `db_type` method.
