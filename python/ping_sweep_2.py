import subprocess
for i in range(0, 255):
    subprocess.run(['ping', '-n', '1', "10.1.2.%d" % i])
