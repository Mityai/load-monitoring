class SlurmJob(object):
  NAME_TO_FIELD = {
    'JOBID':      'job_id',
    'PARTITION':  'partition',
    'NAME':       'name',
    'USER':       'user',
  }

  def set_field(self, field, value):
    setattr(self, self.NAME_TO_FIELD[field], value)
