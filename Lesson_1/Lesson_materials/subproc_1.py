import os
from subprocess import run, Popen

# files = [f.name for f in os.scandir() if f.is_file() and f.name.lower().endswith(".py")]
# print('Files for packing: ', files)
#
#
# # with Popen(['Keka.app', 'test.zip', *files]) as packer:  # tried on MacOS
# with Popen(['7z', 'a', 'test.zip', *files]) as packer:  # for Windows
#     print(packer.args)
#     print('We are waiting compressing...')
# print('All files are compressed')
#
#
# os.rename('test.zip', 'backup.zip')

# ======================================
py_proc = run(["python3", "-V"])
print(py_proc)

# return_code = py_proc.check_returncode()  # check the value of returncode
# print(return_code)
"""
Python 3.8.2
CompletedProcess(args=['python3', '-V'], returncode=0) # If returncode = 1 it's mean was an error, if returned 0, means all OK
"""