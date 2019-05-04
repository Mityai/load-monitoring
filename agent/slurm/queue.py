import logging

from slurm.job import SlurmJob


class SlurmQueue(object):
  FIELDS_TO_EXTRACT = [
    'JOBID',
    'PARTITION',
    'NAME',
    'USER',
  ]

  def __init__(self, jobs_queue):
    self.queue = jobs_queue

  @classmethod
  def from_squeue_output(cls, squeue_output):
    squeue_output_lines = squeue_output.split('\n')
    header = squeue_output_lines[0].split()

    jobs = list()
    for job_desc_line in squeue_output_lines[1:]:
      job_desc = job_desc_line.split()

      job = SlurmJob()
      for field in FIELDS_TO_EXTRACT:
        try:
          job.set_field(field, job_desc[header.index(field)])
        except ValueError as e:
          logging.exception(e)

      jobs.append(job)

    return cls(jobs)
