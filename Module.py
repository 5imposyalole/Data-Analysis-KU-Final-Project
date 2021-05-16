#!/usr/bin/python
# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('athlete_events.csv')
df_GDP = pd.read_csv('gdp.csv', encoding = "ISO-8859-1")
df_pop = pd.read_csv('populationdata.csv', encoding = "ISO-8859-1")

#for i in range(0, len(years)):
#    s
#    if years[i] == 1960 + x:
#        olympic_years.append(i)
#    x = 4
     
    



def population(country,year):
    
    pop = df_pop.loc[(df_pop['Series Code'] == 'SP.POP.TOTL') & (df_pop['Country Code'] == country)]
    #year = 1959
    #years = list(Country)

    pop1 = pop.values.tolist()
    pop2 = pop1[0]
    population = pop2[4:63]

    r = year - 1901
    years = []
    for i in range(r):
        
        years.append(year)
        year += 1

    #print(years)
    return population, years


def GDP(country,year):

    country1 = df_GDP.loc[(df_GDP['Country Code'] == country)]
    country_list1 = country1.values.tolist()
    country_list2 = country_list1[0]
    GDP = country_list2[4:63]
    
    r = year - 1901
    
    years = []

    for i in range(r):
        year += 1
        years.append(year)

    return GDP,years

def medal_count(country, year, season):
    years_summer = [1896,1900,1904,1908,1912,1916,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]
    years_winter = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]

    medal_count  = []
    gold_count   = []
    silver_count = []
    bronze_count = []

    s = len(years_summer)
    w = len(years_winter)

    if season == 's':
        for i in range(len(years_summer)):
            if year > years_summer[i]:
                x = years_summer[i + 1:s]
            else:
                for i in range(len(years_winter)):
                    if year > years_winter[i]:
                        x = years_winter[i + 1:s]

    for i in range(len(x)):
        df_1 = df.loc[(df['NOC'] == country) & (df['Year'] == x[i]) & (df['Season'] == 'Summer')]
        
        age = df_1['Age'].values.tolist()

        result_df = df_1.drop_duplicates(subset=['Event','Medal']) #drop repeated medals i.e baseball team receives more than 1 medal for each member (can't earn more than 1 type of medal for 1 event)
        
        medal = result_df['Medal'].values.tolist()
        #event = result_df['Event'].values.tolist()

        count_G = medal.count('Gold')
        count_S = medal.count('Silver')
        count_B = medal.count('Bronze')

        total_count = count_G + count_S + count_B
        medal_count.append(total_count)
        gold_count.append(count_G)
        silver_count.append(count_S)
        bronze_count.append(count_B)

        #bronze_count,silver_count,gold_count,medal_count,


    return bronze_count,silver_count,gold_count,medal_count #event, average_age, medal_count, median_age, mode_age, minimum_age,maximum_age,range_age, y1_age, y2_age, interquartile_age, sd_age

def regression(x,y):
    results = stats.linregress(x, y)
    p = results.pvalue
    return results, p

    
def age_calc(country, year, season):
    years_summer = [1896,1900,1904,1908,1912,1916,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]
    years_winter = [1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016]

### Central tendency section
    average_age = []
    median_age  = []
    mode_age = []
    age_f = []

    s = len(years_summer)
    w = len(years_winter)

    if season == 's':
        for i in range(len(years_summer)):
            if year > years_summer[i]:
                x = years_summer[i + 1:s]
            else:
                for i in range(len(years_winter)):
                    if year > years_winter[i]:
                        x = years_winter[i + 1:s]

    for i in range(len(x)):
        df_1 = df.loc[(df['NOC'] == country) & (df['Year'] == x[i]) & (df['Season'] == 'Summer')]
        
        #male = df_1.loc[(df_1['Sex'] == 'M')]
        age = df_1.drop_duplicates(['ID', 'Year'])['Age']
        age =  age[np.isfinite(age)]
        age_f.append(age)
     #   print(age)
       
       ## Central tendency section
        average_age_calc = np.mean(age)
        average_age.append(average_age_calc)
        median_age_calc = np.median(age)
        median_age.append(median_age_calc)
        mode_result = stats.mode(age)
        x2 = mode_result.mode
        mode_age.append(x2)
        
        #print(x)
        

        #print(x)


    return age_f,average_age,median_age, mode_age #minimum_age,maximum_age,range_age, y1_age, y2_age, interquartile_age, sd_age

    
