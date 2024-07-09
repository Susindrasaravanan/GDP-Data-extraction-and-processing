import numpy as np
import pandas as pd
URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29" #url which contains three tables of economies
tables = pd.read_html(URL) #read the url 
df = tables[3] #take the third table
df.columns = range(df.shape[1]) #number the column starting from 0
df = df[[0,2]] #selecting the columns country and GDP
df=df.iloc[1:11,:] #selecting the indices from 0 to 10
df.columns=['Country','GDP (Million USD)'] # naming the columns
df['GDP (Million USD)'] = df['GDP (Million USD)'].astype(int) #changing the data type as int
df[['GDP (Million USD)']] = df[['GDP (Million USD)']]/1000 #converting to billion USD by dividing 1000
df[['GDP (Million USD)']] = np.round(df[['GDP (Million USD)']], 2) #getting only two number by rounding after decimal point
df.rename(columns = {'GDP (Million USD)' : 'GDP (Billion USD)'}, inplace=True) #rename the column
df.to_csv(r'C:\Users\susindra\OneDrive\Desktop\Largest_economies.csv', index=False) #load into csv file