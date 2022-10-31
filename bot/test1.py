import pandas as pd


csv = pd.read_csv('./startupnation_articles.csv')

df = pd.DataFrame(csv, columns=['title','url','tag'])
print(df['title'][0])