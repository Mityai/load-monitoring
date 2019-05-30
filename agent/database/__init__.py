from database.graphite import GraphiteClient

DB_CLIENTS = {
  GraphiteClient.db_type(): GraphiteClient,
}

def get_client(db_type, config):
  return DB_CLIENTS[db_type](config)
