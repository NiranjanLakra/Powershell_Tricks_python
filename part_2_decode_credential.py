import subprocess

cmd1="C:\\Users\\win10\\Documents\\SystemFile.xml"
cmd2="$pass=Import-Clixml -Path "+cmd1+" ; $pass.GetNetworkCredential().password"
data=subprocess.Popen(["powershell", cmd2],stdout=subprocess.PIPE)
result=data.communicate()[0]

print(result)
