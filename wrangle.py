import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import env
from datetime import date

##########ACQUIRE########################



##########PREPARE########################

def prepd_data(df):
#splits the path into two colums, I will keep 'path_2' and drop 'path'
    df['path_2'] = df.path.str.split('/').str[1]
#Found empty string values in path_2. This code replaces the empty cells with 'NaN'
#in order to drop nulls later.
    df['path_2'].replace('', np.nan, inplace=True)
#merge date and time columns
    df['date'] = df['date'] +' '+ df['time']#concat time and date
#datetime conversion and set index   
    df['date'] = pd.to_datetime(df['date'])
    df = df.set_index('date').sort_index()
#drop columns. these columns have no use.
    df = df.drop(columns=['time', 'id_x', 'slack', 'id_y', 'Name', 'deleted_at', 'path'])
#rename columns
    df = df.rename(columns = {'name':'cohort', 'start_date':'class_start_date', 'end_date':'class_end_date'})
#converts dtypes for listed features
    convert_dict_int = {'cohort_id':int, 'program_id':int, 'class_start_date':'datetime64[ns]', 'class_end_date':'datetime64[ns]', 'created_at':'datetime64[ns]', 'updated_at':'datetime64[ns]'}
    df = df.astype(convert_dict_int)

    return df

#new df summarization
def summarize(df):
    print(df.shape)
    print(f'___________________________')
    print(df.info())
    print(f'___________________________')      
    print(df.isnull().sum())
