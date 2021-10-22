import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import env
from datetime import date

##########ACQUIRE########################
#db access
def get_connection(db, user=env.user, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

#Function accessesing db server, queries logs, and cohorts tables from the curriculm_logs db.
#curriculum_logs db. Queried all tables with a LEFT JOIN.
log_sql = "SELECT *\
              FROM logs\
              LEFT JOIN cohorts ON logs.cohort_id = cohorts.id;"

#Grabs dataset from get_connection function above and formats it into a pandas dataframe.
#acquires curriculum_logs dataset
def get_log_data():
    return pd.read_sql(log_sql,get_connection('curriculum_logs'))


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
#drops nulls (rows)
    df = df.dropna()
#take subset where path doesn't end with jpg
    df = df[~df.path_2.str.endswith('jpg')]
#take subset where path doesn't end with jpeg
    df = df[~df.path_2.str.endswith('jpeg')]
#take subset where path doesn't end with svg
    df = df[~df.path_2.str.endswith('svg')]
#strips the leading digits from the string
    df['path_2'] = df.path_2.str.lstrip('(\d)')
#strips digits
    df['path_2'] = df.path_2.str.strip('123')
#strips leading hypens
    df['path_2'] = df.path_2.str.lstrip('(-)')
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

#count and normalized plotting
def value_counts_and_frequencies(s: pd.Series, dropna=True) -> pd.DataFrame:

    return pd.merge(
        s.value_counts(dropna=False).rename('count'),
        s.value_counts(dropna=False, normalize=True).rename('proba'),
        left_index=True,
        right_index=True,
    )