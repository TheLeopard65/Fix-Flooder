import subprocess

target = "192.168.100.225"
command = f"ping {target} -t -l 65500"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

while True:
    output = process.stdout.readline()
    print(output.strip().decode())