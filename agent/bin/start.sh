#!/bin/bash
module add slurm

AGENT_DIR=$(dirname $0)/..

PID_FILE=$AGENT_DIR/agent.pid

if [ -f $PID_FILE ] && [ -f /proc/$(cat $PID_FILE)/status ]; then
  PID=$(cat $PID_FILE)
  echo "Agent is already running wit pid $PID"
else
  PYTHON="python3"
  $PYTHON $AGENT_DIR/__main__.py $@ 1> /dev/null 2> /dev/null &
  echo $! > $PID_FILE
  PID=$(cat $PID_FILE)
  echo "Agent has started with pid $PID"
fi
