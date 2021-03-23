import os

# os.mkdir('test_dir')

if not os.path.exists('test_dir'):
    os.mkdir('test_dir')

dir_struct = os.listdir("..")
print(dir_struct)  # ['os_examples.py', 'rundom_file.py', 'subproc_2.py', 'return_code.py', 'test_dir', 'subproc_1.py']


dirs = [d for d in dir_struct if os.path.isdir(d)]
print(dirs)  # ['test_dir']


fls = [f for f in dir_struct if os.path.isfile(f)]
print(fls)  # ['os_examples.py', 'rundom_file.py', 'subproc_2.py', 'return_code.py', 'subproc_1.py']


base_path = os.path.basename('/etc/fstab')
print(base_path)  # fstab

dir_path = os.path.dirname('/etc/fstab')
print(dir_path)  # /etc


dir_tuple = os.path.split('/etc/foo//fstab')
print(dir_tuple)  # ('/etc/foo', 'fstab')
