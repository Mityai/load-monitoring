import argparse
import json
import logging
import sys

from agent import Agent


def parse_args(argv):
  parser = argparse.ArgumentParser()
  parser.add_argument('--config', type=str, help='Path to agent JSON config', required=True)
  parser.add_argument('--debug', action='store_true')
  args = parser.parse_args()

  args.config = json.load(open(args.config))

  if args.debug:
    args.config['cluster'] = 'test'

  return args


def main(argv):
  args = parse_args(argv)
  if args.debug:
    logging.basicConfig(level=logging.DEBUG)
  else:
    logging.basicConfig(level=logging.INFO)

  logging.info('Agent config:\n{}'.format(json.dumps(args.config, indent=2)))
  agent = Agent(args.config)
  agent.run()


if __name__ == '__main__':
  main(sys.argv[1:])
