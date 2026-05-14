import pandas as pd
df=pd.read_csv ('/Users/saivivek/Downloads/AD314_questionwise_data.csv')
df1=pd.read_csv('/Users/saivivek/Downloads/AD314_mongo_data1.csv')
# df1.drop(cnnhholumns=['_id'],inplace=True)
df=df.drop_duplicates()
df1=df1.drop_duplicates()
new_df=df.merge(df1,how='inner',on=['examid','deliveryid','admissionnumber','questionnumber'])
new_df.to_excel('/Users/saivivek/Downloads/AD314_merged_data22.xlsx',index=False)