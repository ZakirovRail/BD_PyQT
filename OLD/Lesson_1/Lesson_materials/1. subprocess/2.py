from subprocess import call

RETURNCODE = call('Sublime Text')
if RETURNCODE == 0:
    print("All Ok")
else:
    print("Error")
