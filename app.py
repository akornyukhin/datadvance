import sys
import pandas as pd
import numpy as np

from tqdm import tqdm

def incidents(input_path, output_path, dT=0.3):
    df = pd.read_csv(input_path, index_col='id')

    df['feature3'] = (df.feature1 * 100).astype('str') + df.feature2.astype('str')
    df = df.loc[:,['time','feature3']]
    df_sorted = df.reset_index().sort_values(['feature3','time'], ascending=False)

    d = df_sorted.as_matrix()

    len_ = df_sorted.shape[0]
    result = np.zeros(shape=(len_))

    for i in tqdm(range(len_)):
        count = 0
        for j in range(i+1, len_):
                if abs(d[i,1] - d[j,1]) <= dT:
                    if d[i,2] == d[j,2]:
                        count += 1
                    else:
                        break
        result[int(d[i,0])] = count

    df_result = pd.DataFrame(result, columns=['count'], dtype='int32')
    df_result = df_result.reset_index().astype('int').sort_values('index').rename(columns={'index': 'id', 0: 'count'})
    df_result.to_csv(output_path, index=False, index_label='id', sep=';')
    
    return print('You can see the file in the directory you have chosen')

if __name__ == '__main__':
    try:
        incidents(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    except Exception as e:
        print(e)