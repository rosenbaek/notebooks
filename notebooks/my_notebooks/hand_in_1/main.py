from turtle import color
import pandas as pd 
import numpy as np
import matplotlib as mpl
# reset defaults because we change them further down this notebook
mpl.rcParams.update(mpl.rcParamsDefault)
import matplotlib.pyplot as plt

df = pd.read_csv("owid-covid-data.csv", parse_dates=["date"])

df["month"] = df["date"].dt.month


no_2 = df.pivot(index="date", columns="location", values="new_cases")
monthly_max = no_2.resample("M").sum()
no_3 = monthly_max.transpose()
no_3['max_month'] = no_3.idxmax(axis=1)
no_3['max_value'] = no_3.max(axis=1)
print(no_3[["max_month","max_value"]])


europe = df.loc[df['continent'] == "Europe"].sort_values(by=['total_tests_per_thousand'],ascending=False)
print(europe[["location", "total_tests_per_thousand"]])

no_4 = df.pivot(index="date", columns="location", values="total_deaths")
maxDeath = no_4.resample("M").max()
no_4 = maxDeath.transpose()
no_4['max_death'] = no_4.max(axis=1)
no_4 = no_4.sort_values(by=['max_death'],ascending=False)[9:19]
x = no_4.index
y = no_4["max_death"]
mpl.use("pdf")
plt.bar(no_4.index, no_4["max_death"], width=0.5, align='center')
plt.axis([None, None, 0, no_4["max_death"].max() + 80000])
plt.xlabel("Countries", fontsize=10)
plt.ylabel("Amount", fontsize=10)
plt.savefig('barchart.png',bbox_inches='tight')
plt.close()
print(no_4.index)

df["death_vs_infected"] = df.new_deaths.div(df.new_cases)*100

denmark = df.loc[df['location'] == "Denmark"]
usa = df.loc[df['location'] == "United States"]
germany = df.loc[df['location'] == "Germany"]


usa = usa[(usa['date'] > '2021-04-1')]
denmark = denmark[(denmark['date'] > '2021-04-1')]
germany = germany[(germany['date'] > '2021-04-1')]
denmark.date = pd.to_datetime(denmark.date)
print(denmark.info())
dk = plt.plot(denmark['date'], denmark['death_vs_infected'],linewidth=1, label='Denmark')
ger = plt.plot(germany['date'], germany['death_vs_infected'],linewidth=1, label='Germany')
us = plt.plot(usa['date'], usa['death_vs_infected'],linewidth=1, color="red",label='United States')
plt.ylabel('% deaths of infected') 
plt.legend()
plt.savefig('linechart.png',bbox_inches='tight')
#
print(denmark['death_vs_infected'])



