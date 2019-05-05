from database.graphite import GraphiteClient

DB_CLIENTS = {
  GraphiteClient.db_type(): GraphiteClient,
}

def get_client_type(db_type):
  return DB_CLIENTS[db_type]
