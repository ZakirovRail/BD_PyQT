from subprocess import Popen, PIPE

# PROC = Popen("dir", shell=True, stdout=PIPE)  #  Linux OS?
PROC = Popen("pwd", shell=True, stdout=PIPE)  # for MacOS command
print(PROC)  # <subprocess.Popen object at 0x7f9a3212eac0>

PROC_2 = Popen("ls -l", shell=True, stdout=PIPE)  # for MacOS command
print(PROC_2)  # <subprocess.Popen object at 0x7f9a96b29fd0>

OUT = PROC.stdout.read().decode('cp866')
print(OUT)  # /Users/zakirovrjicloud.com/Python/BD_PyQT/Lesson_1/Lesson_materials/1. subprocess

OUT_2 = PROC_2.stdout.read().decode('cp866')
print(OUT_2)
"""
total 8
-rw-r--r--  1 zakirovrjicloud.com  staff  634 Mar 15 13:22 1.py
"""
