import pandas as pd


df_state=pd.read_csv("C:/Users/acer/PycharmProjects/barikoi_task1/users.csv")

Dup_data = df_state[df_state.duplicated()]

print("\n\nDuplicate data : \n {}".format(Dup_data))

DF_RM_DUP = df_state.drop_duplicates(keep='last')

print('\n\nResult DataFrame after duplicate removal :\n', DF_RM_DUP.head(n=5))
