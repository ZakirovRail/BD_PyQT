import subprocess

# ret = subprocess.call("ls -l", shell=True)
"""
total 24
-rw-r--r--  1 zakirovrjicloud.com  staff  148 Mar 23 13:11 return_code.py
-rw-r--r--  1 zakirovrjicloud.com  staff    0 Mar 23 12:49 rundom_file.py
-rw-r--r--  1 zakirovrjicloud.com  staff  811 Mar 23 13:10 subproc_1.py
-rw-r--r--  1 zakirovrjicloud.com  staff   61 Mar 23 14:59 subproc_2.py
"""
#  ====================================================================================================================
# p = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
# out = p.stdout.read()
# print(out)
"""
b'total 24\n-rw-r--r--  1 zakirovrjicloud.com  staff  148 Mar 23 13:11 return_code.py\n-rw-r--r--  1 zakirovrjicloud.com  staff    0 Mar 23 12:49 rundom_file.py\n-rw-r--r--  1 zakirovrjicloud.com  staff  811 Mar 23 13:10 subproc_1.py\n-rw-r--r--  1 zakirovrjicloud.com  staff  478 Mar 23 15:01 subproc_2.py\n'
"""
#  ====================================================================================================================
p = subprocess.Popen("wc", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
out, err = p.communicate(b'aaa bbb \n  ccc ddd ')
print(out)  # b'       1       4      19\n'
print(err)  # b''

#  ====================================================================================================================
p1 = subprocess.Popen("ls -l", shell=True, stdout=subprocess.PIPE)
p2 = subprocess.Popen("wc", shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
out = p2.stdout.read()
print(out)  # b'       5      38     305\n'





#  ====================================================================================================================







#  ====================================================================================================================





#  ====================================================================================================================







#  ====================================================================================================================







#  ====================================================================================================================











