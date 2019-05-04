from slurm.slurm import SlurmClient


def main():
  client = SlurmClient()
  print(len(client.queue().queue))


if __name__ == '__main__':
  main()
