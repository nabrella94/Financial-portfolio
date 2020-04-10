#!/usr/bin/env python
# coding: utf-8

# his a basic stock market analysis project to understand some of the basics of Python programming in financial markets.
# : Import the necessary modules

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd


# Overview of American Airlines and benchmarking their stocks performance together. Get the data from yahoo finance on the  weekly closing prices of Delta, United Airlines , South West and American Airlines for 2 month . I will grabbing the data from Yahoo Finance using download method. In this section, I am comparing Delta(DAL), South West( LUV), United(UAL) and AAL(American Arilines). I am setting interval of 1 week for the last 2 months to show the trend of stock price.Fetching data for multiple tickers

# In[5]:


data = yf.download("DAL LUV UAL AAL", interval = "1wk", start="2020-02-01", end="2020-04-06",
                   group_by="ticker")


# The COVID-19 Pandemic Slams Into Airlines. The airlines have been severely disrupted by the pandemic, with the global industry expected to lose more than $100 billion in revenue in 2020 due to travel bans and plummeting demand. Airlines cancel flights and lay off workers as their shares plummet.

# In this section I am going to organize the datfarme and remove uninecessary coloumns to plot close stock market price for those airlines. Create a new column for each dataframe called “df1” which is the close stock price.

# In[7]:


#creating data frame
df = pd.DataFrame(data) 
  
 #Remove two columns name is 'Open' and 'High' , 'low' , 'adjust close' and 'volum'  
df.drop(df.columns[[0,1,2,4,5,6,7,8,10,12,11,13,14,16,17,18,19,20,22,23]], axis = 1, inplace = True)
#remove nan values
df.dropna(inplace=True)
#table for 
df.head()


#  Visualise the data, and visually inspect interesting events. In this section, we also create a candlestick chart from scratch.

# In[9]:


df.plot(figsize=(10,4))
plt.legend()

plt.title(" Close Stock Price for Airline Companies", fontsize=16)

plt.ylabel('Stock Closing Price', fontsize=14)

plt.xlabel('Week', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()


# As you see above, All for Airlines companies' stock drop harshly in the last 2 months . They experienced rapid decrease, United Airlines(UAL) saw highest drop by 72%, on the other hand South West(LUV) saw the lowest decrease with 50% . Those four stocks follow the same pattern in given time.

# Create a new column for each dataframe called “df11” which is   the Volume Traded.

# In[15]:


df11=pd.DataFrame(data)
  
 #Remove two columns name is 'Open' and 'High' , 'low' , 'adjust close' and 'close'  
df11.drop(df11.columns[[0,1,2,3,4,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22]], axis = 1, inplace = True)

df11.dropna(inplace=True)




# Data visulization Volume Traded.

# In[14]:


df11.plot(figsize=(10,4))

plt.legend()

plt.title("Number of Stock Traded Weekly for Airline Companies", fontsize=16)

plt.ylabel('Number of Stocked Tarded 100,000,000', fontsize=14)

plt.xlabel('Week', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()


# Overview of Hotel Chain Brands and benchmarking their stocks performance together
# Hotel stocks have lost roughly half their value over the past month as hotel companies face steep drops in demand due to COVID-19. As the hotel industry is impacted by the global outbreak, share prices have also realized a significant slump. In the U.S., an estimated $1.4B in revenue is vanishing each week.

# I would like to present the effect of this pandemic on Hotel chain. I selected these brands: Hyattt Hotel(H), Choice Hotel International(CHH), Huanzhu Group(HTHT), Marriott Hotel(MAR) and Hilton(HLT). I will download the stock data for the same time and interval for hotel industry.

# In[20]:


data2 = yf.download("H CHH HTHT HLT MAR",interval = "1wk", start="2020-02-01", end="2020-04-06",
                   group_by="ticker") 
df2 = pd.DataFrame(data2) 
 #Remove two columns name is 'Open' and 'High' , 'low' , 'adjust close' and 'volum'   
df2.drop(df2.columns[[0,1,2,4,5,6,7,8,10,12,11,13,14,16,17,18,19,20,22,23,24,25,26,28,29]], axis = 1, inplace = True) 

df2.dropna(inplace=True)
df2.head()



# In[21]:


df2.plot(figsize=(10,4))

plt.legend()

plt.title("Close Stock Price for Hotel Chains Brands", fontsize=16)

plt.ylabel('Stock Closing Price', fontsize=14)

plt.xlabel('Week', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()


# Data visulization 

# In[25]:


#ceating new data frame 
df13=pd.DataFrame(data2) 
 #Remove two columns name is 'Open' and 'High' , 'low' , 'adjust close' and 'close'  
df13.drop(df13.columns[[0,1,2,3,4,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28]], axis = 1, inplace = True)



df13.dropna(inplace=True)


df13.plot(figsize=(10,4))

plt.legend()

plt.title("Number of Stock Traded Weekly for Hotel Chains Brands", fontsize=16)

plt.ylabel('Number of Stocked Tarded 10,000,000', fontsize=14)

plt.xlabel('Week', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()


# One one hand, the stock prices follow the same trend and they lost 50% to 60% of their value. One the other hand, it is interesting that traders moved strongly to Marriott (MAR) and Hotel(HLT)'s stocks in compare to others. This means traders trust on health of Hilton Hotel(HLT) and Marriott (MAR) finance market.

# Analyzing stock prices of Successful STARTUPS founded during 2008 Great Recession
# American workers took a hard hit after the 2008 recession, but a wave of new startups emerged from the financial downturn. Most of them is based on E-Commerce , mobile application, Social media and digital marketing solutions. Behavioral changes after pandemic could mean more opportunities for entrepreneurs to provide meaningful services. We can learn lessons from 2008 recession how those business plans lead to real business outcomes, like revenue and profit. Some of those successful brands(Whats up, Instagram) required by big companies like Facebook and Google

# In[ ]:





# In[40]:


data3 = yf.download("GRPN ZEN PYPL WORK UBER", period = "ytd",interval = "1wk", start="2020-02-01", end="2020-04-06",
                   group_by="ticker")


# The same procees for start ups

# In[42]:


df3 = pd.DataFrame(data3) 
 #Remove two columns name is 'Open' and 'High' , 'low' , 'adjust close' and 'volum' 
df3.drop(df3.columns[[0,1,2,4,5,6,7,8,10,12,11,13,14,16,17,18,19,20,22,23,24,25,26,28,29]], axis = 1, inplace = True) 


#,24,25,26,28,29
df3.dropna(inplace=True)


df3.plot(figsize=(10,4))

plt.legend()

plt.title("Close Stock Price for Top startups founded during 2008 recession ", fontsize=16)

plt.ylabel('Stock Closing Price', fontsize=14)

plt.xlabel('Weeks', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()


# In[44]:


df12=pd.DataFrame(data3) 
 #Remove two columns name is 'Open' and 'High' , 'low' , 'adjust close' and 'close'
df12.drop(df12.columns[[0,1,2,3,4,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,24,25,26,27,28]], axis = 1, inplace = True)


df12.dropna(inplace=True)
#from yahoofinancials import YahooFinancials

df12.plot(figsize=(10,4))

plt.legend()

plt.title(" Weekly for Top start-ups founded in 08 recession ", fontsize=16)

plt.ylabel('Number of stocked tarded 100,000,000', fontsize=14)

plt.xlabel('Week', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)

plt.show()


# As demonstrated above, This group of companies are more stable and reliable in compare to the previous industries. The pandemic didn't hit the stocks price and the leveled off the prices. As rising markets on increasing volume on Uber(UBER ) are typically viewed as strong and healthy. Traders believe on the future of Uber(UBER) more than others.

# In[ ]:




