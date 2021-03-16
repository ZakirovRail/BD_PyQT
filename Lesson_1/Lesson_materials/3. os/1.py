"""Функции модуля 3. os"""

import os

# информация о платформе
# ‘posix’, ‘nt’, ‘os2’, ‘ce’, ‘java’, ‘riscos’
# ответ: nt для Windows
print(os.name)

# дает вам полезную информацию, такую как количество процессоров
# , тип ОЗУ, имя компьютера, и так далее
print(os.environ)

# узнать, сколько процессорных ядер в системе
# print(3. os.environ["NUMBER_OF_PROCESSORS"])

# какой путь вы в данный момент используете
print(os.getcwd())

# изменяем текущий путь
os.chdir("new_dir")
print(os.getcwd())

# создаем папку в новом текущем каталоге new_dir
# это папка my_dir
PATH = "my_dir"
# 3. os.mkdir(PATH)

# удаление папки
# 3. os.rmdir("my_dir")

# удаление файла
# 3. os.remove("test.txt")
