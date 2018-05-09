import sys
import pandas as pd 

def incidents(input_path, output_path, dT=0.3):
    df = pd.read_csv(input_path, index_col='id')
    df_sorted = df.reset_index().sort_values('time', ascending=False)
    d = df_sorted.as_matrix()

    result = {}
    len_ = df_sorted.shape[0]

    for i in range(len_):
        count = 0
        for j in range(i+1, len_):
            if d[i,1] == d[j,1] and d[i,2] == d[j,2] and abs(d[i,3] - d[j,3]) <= dT:
                count += 1
            else:
                break
        result[d[i,0]] = count

    df_result = pd.DataFrame.from_dict(result, orient='index')
    df_result = df_result.reset_index().astype('int').sort_values('index').rename(columns={'index': 'id', 0: 'count'})
    df_result.to_csv(output_path, index=False)
    
    return print('You can see the file in the directory you have chosen')

if __name__ == '__main__':
    try:
        incidents(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    except Exception as e:
        print(e)