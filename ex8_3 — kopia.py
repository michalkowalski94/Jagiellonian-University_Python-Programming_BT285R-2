#Create a script that will perform and display bash command: "ls *.py|wc -l
import subprocess

cmd1 = ["ls *.py"]
process1 = subprocess.Popen(cmd1,stdout=subprocess.PIPE, shell=True)

cmd2=['wc', '-l']
process2 = subprocess.Popen(cmd2,stdin=process1.stdout,stdout=subprocess.PIPE)
stdin, stdout = process2.communicate() 
print stdin, stdout
