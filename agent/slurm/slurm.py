import logging

import util.process

from slurm.queue import SlurmQueue


class SlurmClient(object):
  def queue(self, partition=None, timeout=None):
    cmd = ['squeue']

    if partition is not None:
      cmd += ['-p', partition]

    out, _ = util.process.get_command_output(cmd, timeout=timeout)
    return SlurmQueue.from_squeue_output(out)
