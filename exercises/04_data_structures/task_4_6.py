# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
names = ['Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

data = ospf_route.split()
popa = data.pop(2)

print(f'''
{names[0]:<21} {data[0]:<21}
{names[1]:<21} {data[1].strip("[]"):<21}
{names[2]:<21} {data[2].rstrip(","):<21}
{names[3]:<21} {data[3].rstrip(","):<21}
{names[4]:<21} {data[4]:<21}
''')

