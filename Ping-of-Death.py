import subprocess
import platform

target = "127.0.0.1"

if platform.system() == "Windows":
    command = f"ping {target} -t -l 65500"  # Windows command
else:
    command = f"ping {target} -s 65500"  # Linux command

process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
while True:
    output = process.stdout.readline()
    if output: print(output.strip().decode())
