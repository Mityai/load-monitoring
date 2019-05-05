from graphite import GraphiteClient

DB_CLIENTS = {
  GraphiteClient.db_type(): GraphiteClient,
}
