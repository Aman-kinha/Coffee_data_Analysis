import pandas as pd
coffee_data=pd.read_csv("index.csv")
weather_data=pd.read_csv("delhi.csv")
# coffee_data.info()
datac=coffee_data["date"].str.split("-")                 #Spliting  the date column into day, month and year

# print(datac.str[0])                 
coffee_data["year"]=datac.str[0]                         #Extracting  year from date 
coffee_data["month"]=datac.str[1]                        #Extracting  Month from date 
coffee_data.loc[:,"card"]=coffee_data["card"].fillna("No Card")                         #Removing Null Values 
# print(coffee_data)
coffee_data["date"]=pd.to_datetime(coffee_data["date"],dayfirst=True)  #Converting Date column to datetime format
# print(coffee_data.head(15))
# print(coffee_data.duplicated().sum())                  #Checkng for duplicate rows
# coffee_data.to_csv("coffee.csv")

# coffee_data.info()
dataw=weather_data["date_time"].str.split(" ")
weather_data["Dates"]=dataw.str[0]

start_date='2009-01-01'
end_date='2019-02-28'
drop_date='2020-01-01'
mask=(weather_data["Dates"]>=start_date)&(weather_data["Dates"]<=end_date)
weather_data=weather_data[weather_data["Dates"]!=drop_date]
weather_data=weather_data.loc[~mask]
weather_data["Dates"]=weather_data["Dates"].str.replace("19","24") 
# print(weather_data)


weather_data["date_time"]=pd.to_datetime(weather_data["date_time"])  #Converting Date_time column to datetime format
# weather_data.info()
# print(weather_data.isnull().sum())                 

weather_data["average_temp"] = (weather_data["maxtempC"] + weather_data["mintempC"]) / 2
weather_data.loc[(weather_data["average_temp"]>=25) & (weather_data["average_temp"]<=29), "weather"] = "Normal"
weather_data.loc[(weather_data["average_temp"]>29), "weather"] = "Summer"
weather_data.loc[(weather_data["average_temp"]<25), "weather"] = "Winter"
# print(weather_data.head(364))

# print(weather_data.loc[3627:3680])       
weather_data.drop_duplicates(subset=["Dates"], inplace=True)
# print(weather_data)                       
weather_data.shape
print(weather_data["Dates"].isnull().sum())                      #Checking For Nul values 
weather_data.to_csv("weather.csv")