import subprocess


def run_command(cmd):
  process = subprocess.Popen(
    cmd,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
  )
  return process


def run_command_wait(cmd, timeout=None):
  process = run_command(cmd)
  process.wait(timeout=timeout)
  return process


def get_command_output(cmd, timeout=None):
  process = run_command_wait(cmd, timeout)
  return map(str, process.communicate())
