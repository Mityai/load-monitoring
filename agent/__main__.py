import argparse
import json
import logging
import sys

from agent import Agent


def parse_args(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--config', type=str, help='Path to agent JSON config', required=True)
  args = parser.parse_args()

  args.config = json.load(open(args.config))
  logging.info('Agent config:\n{}'.format(json.dumps(args.config, indent=2)))
  return args


def main(argv):
  logging.basicConfig(level=logging.INFO)
  args = parse_args(argv)

  agent = Agent(args.config)
  agent.run()


if __name__ == '__main__':
  main(sys.argv[1:])
