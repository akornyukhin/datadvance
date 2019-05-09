# datadvance
DATADVANCE test task

To run script from terminal: <br />
**python app.py input_path output_path dT** 



Initial task:

You have N incidents. Each of the incident has an _id_ [0, N-1] and two _categorical features_ with values [0,M-1] and a _timestamp_.
 
The following script generates and exmaple with N=10 and M=2

## ====
import numpy as np<br />
import pandas as pd
 
M = 2<br />
N = 10
 
df = pd.DataFrame({'feature1':np.random.randint(M, size=(N,)),<br />
                   'feature2':np.random.randint(M, size=(N,)),<br />
                   'time':np.random.rand(N)<br />
                   })
 
df.to_csv('incidents.csv', index_label='id')
## =====
 
Generated file example:
 
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
 
# ====

The task is to write a sript which gets a dT argument and a csv file with incidents, and for each incidents calculate the number of other incidents which full-fill the following rules:
* the incident was prior to the overviewed incident and the timedifference is <=DT
* the feaure1 and feature2 fields are the same as overviewed incident's fields
The results should be written in a csv-file.


For example for dT=0.3 the output should be as followed:
 
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


