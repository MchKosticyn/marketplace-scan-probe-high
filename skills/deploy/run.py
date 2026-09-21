import subprocess
import sys

# The target comes straight from the chat message; it is concatenated into a shell command.
target = sys.argv[1]
subprocess.run("ssh deploy@" + target + " 'bash -s' < deploy.sh", shell=True, check=True)
