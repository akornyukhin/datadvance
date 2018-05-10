# datadvance
DATADVANCE test task

To run script from terminal:
python app.py <input_path> <output_path> <dT>



Initial task:

"У нас есть набор "инцидентов", N штук. Каждый инцидент имеет id с последовательными значениями от 0 до N-1, два категориальных признака с какими-то целыми значениями от 0 до M-1, и признак времени с каким-то (нецелым) значением от 0 до 1.
 
Например, следующий скрипт генерирует случайный набор таких инцидентов при N=10, M=2, и выписывает в csv-файл:
 
# ====
import numpy as np<br />
import pandas as pd
 
M = 2<br />
N = 10
 
df = pd.DataFrame({'feature1':np.random.randint(M, size=(N,)),<br />
                   'feature2':np.random.randint(M, size=(N,)),<br />
                   'time':np.random.rand(N)<br />
                   })
 
df.to_csv('incidents.csv', index_label='id')
# =====
 
Пример сгенерированного файла:
 
id,feature1,feature2,time<br />
0,1,0,0.206520219143<br />
1,0,0,0.233725001118<br />
2,0,1,0.760992754734<br />
3,1,1,0.92776979943<br />
4,1,0,0.569711498585<br />
5,0,1,0.99224586863<br />
6,0,0,0.593264390713<br />
7,1,0,0.694181201747<br />
8,1,1,0.823812651856<br />
9,0,1,0.906011017725
 
Задача заключается в следующем: надо написать на Python или C/C++ функцию, которая получает на вход dT и файл с инцидентами, и вычисляет для каждого из N инцидентов количество инцидентов из того же файла, которые удовлетворяют следующим условиям:<br />
1) предшествуют данному инциденту по времени, при этом разница по времени не превосходит dT;<br />
2) имеют значения feature1 и feature2, совпадающие с соответствующими значениями данного инцидента.
 
Например, в случае dT=0.3 для приведенного выше примера ответ должен выглядеть так:
 
id,count<br />
0,0<br />
1,0<br />
2,0<br />
3,1<br />
4,0<br />
5,2<br />
6,0<br />
7,1<br />
8,0<br />
9,1
 
Функция должна считывать csv-файл с инцидентами, вычислять результаты для всех инцидентов и выписывать их в csv-файл указанного вида.
 
Основной нюанс: функция должна рабoтать достаточно быстро, а именно не дольше минуты при M=100, N=1000000, dT=0.3."
 
Также направляю дополнительную информацию к заданию, обратите, пожалуйста, внимание:
К решению на python:
1) python3 из сборки anaconda3 версии не ниже 4.3.14
2) без установки дополнительных библиотек через conda/pip
3) код должен быть оформлен в виде функции в файле
4) код должен работать на linux (ubuntu 14.04 и выше), либо mac osx 10 и выше (с указанной сборкой анаконды в п.1)
5) Потребление памяти не более 2гб
