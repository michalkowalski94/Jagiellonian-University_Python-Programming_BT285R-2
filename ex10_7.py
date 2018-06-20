#Write a script that will execute command "ls" in shell and find file with shortest name
import subprocess
import os
cmd1 = ["ls", "-p"]
process1 = subprocess.Popen(cmd1,stdout=subprocess.PIPE, shell=True)
cmd2 = ["grep", "-v", "\"]
process2 = subprocess.Popen(cmd2,stdin=process1.stdout,stdout=subprocess.PIPE)
stdin, stdout = process2.communicate()
results = stdout.split('\n')
results = results.remove('')
print results
