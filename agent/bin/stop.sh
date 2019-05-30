#!/bin/bash
AGENT_DIR=$(dirname $0)/..
PID_FILE=$AGENT_DIR/agent.pid

running() {
  ps -p $(cat $PID_FILE) -o pid | grep $(cat $PID_FILE) > /dev/null
}

if [ -f $PID_FILE ] && running; then
  PID=$(cat $PID_FILE)
  kill -9 $PID
  while running; do
    sleep 1
  done
  rm -f $PID_FILE
  echo "Agent has stopped"
else
  echo "Agent is not running"
fi
