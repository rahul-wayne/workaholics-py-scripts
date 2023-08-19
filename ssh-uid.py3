#!/usr/bin/python3


import subprocess

def ssh_command(host, user, command):
    ssh_cmd = ['ssh', f"{user}@{host}", command]
    result = subprocess.run(ssh_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode(), result.stderr.decode()

if __name__ == "__main__":

  
    vmlist = input("enter file name containing IP list:")
    userid = input("Enter user ID:")
    user = 'root'
    command = f'grep "{userid}" /etc/passwd|tr -d "\n"'
    with open(vmlist) as file:
        servers = [line.strip() for line in file if line.strip()]

    for host in servers:
        stdout, stderr = ssh_command(host, user, command)
        if stdout:
            print(f"{host}:", stdout)
        else:
            print(f"{host}:", "no access")
        if stderr:
            print("Error:")
            print(stderr)
