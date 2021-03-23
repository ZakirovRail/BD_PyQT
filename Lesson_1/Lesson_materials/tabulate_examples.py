"""tabulate - это модуль, который позволяет красиво отображать табличные данные."""
# pip install tabulate

from tabulate import tabulate

# генерация таблицы без шапки
# TUPLES_LIST = [('Python', 'interpreted', '1991'),
#                ('JAVA', 'compiled', '1995'),
#                ('С', 'compiled', '1972')]
#
# print(tabulate(TUPLES_LIST))
#
# print()
#
# # генерация таблицы с шапкой
# TUPLES_LIST = [('Python', 'interpreted', '1991'),
#                ('JAVA', 'compiled', '1995'),
#                ('С', 'compiled', '1972')]
#
# COLUMNS = ['programming language', 'type', 'year']
# print(tabulate(TUPLES_LIST, headers=COLUMNS))


# =========================

TUPLES_LIST = [('programmins language', 'type', 'year'),
               ('Python', 'interpreted', '1991'),
               ('JAVA', 'compiled', '1995'),
               ('С', 'compiled', '1972')]

print(tabulate(TUPLES_LIST, headers="firstrow"))

"""
programmins language    type           year
----------------------  -----------  ------
Python                  interpreted    1991
JAVA                    compiled       1995
С                       compiled       1972
"""












