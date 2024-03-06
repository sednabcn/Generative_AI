import pandas as pd     
df=pd.read_csv("form_tok.csv",sep='|')
print(df.shape)
df_tok=df.loc[:,df.columns[[1,2]]]


df_tok.rename(columns=lambda x:x.strip(), inplace=True)
print(df_tok.columns)
print(df_tok.head(5))
df_tok.to_csv("Tokenized_formulas.csv")
df_tok.to_excel("Tokenized_formulas.xlsx")
