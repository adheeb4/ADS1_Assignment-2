# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:43:51 2022

@author: adheeb
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def read_data(filename):
    """This function takes filename as argument, 
    reads the csv file and returns one normal 
    dataframe and one date frame with countries as columns"""
    data = pd.read_csv(filename, skiprows=4)
    data_transposed = data.set_index("Country Name").transpose()
    data_transposed = data_transposed.drop(index=["Country Code", "Indicator Name", "Indicator Code"])
    return data, data_transposed


def lineplot(dat, con, label, label1):
    """This function produces a lineplot with the data given in argument 
    and saves the image as a png file"""
    plt.figure()
    for i in range(len(con)):
        plt.plot(dat.index, dat[con[i]], label=con[i])
    plt.title(label, size=18)
    plt.xlabel("Year", size=12)
    plt.ylabel(label, size=12)
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig(label1+"_lineplot.png", dpi=300, bbox_inches="tight")
    plt.show()


def barplot(dat, label, label1):
    """This function produces a barplot with the data given in argument 
    and saves the image as a png file"""
    dat.plot(kind="bar")
    plt.title(label, size=18)
    plt.xlabel("Year", size=12)
    plt.ylabel(label, size=12)
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig(label1+"_barplot.png", dpi=300, bbox_inches="tight")
    plt.show()



def pieplot(dat, label1, label2):
    """This function produces a pieplot with the data given in argument 
    and saves the image as a png file"""
    plt.figure()
    plt.pie(dat, autopct="%1.1f%%")
    plt.title(label1, size=15)
    plt.legend(bbox_to_anchor=(1,1) , labels=Countries_list)
    plt.savefig(label2+"_pieplot.png", dpi=300, bbox_inches = "tight")
    plt.show()
   
def heatmap(dat):
    """This function produces a correlation heatmap with the data given in argument 
    and saves the image as a png file"""
    dat = dat.apply(pd.to_numeric)
    dat = dat[indicators]
    corr = dat.corr()
    plt.title("Different Indicators of China", size=20)
    sns.heatmap(corr, annot = True, linewidths=0, square=True, cmap='Blues')
    plt.savefig("heatmap.png", dpi=300, bbox_inches = "tight")
    plt.show()
    



Countries_list = ["Australia", "Brazil", "China",
                  "United Kingdom", "India", "United States"]

CO2_data, CO2_data_transposed = read_data("CO2.csv")
CO2_data_transposed = CO2_data_transposed[30:51]

Urban_data, Urban_data_transposed = read_data("Urban Population.csv")
Urban_data_transposed = Urban_data_transposed[30:51]


indicators = ["Urban population", "Population, total", "CO2 emissions (kt)","CO2 emissions from solid fuel consumption (kt)", 
              "Electricity production from coal sources (% of total)"]

All_data, All_data_transposed = read_data("All Data.csv")
All_data_china = All_data[(All_data["Country Name"] == "China")]
All_data_china = All_data_china.set_index("Indicator Name")
All_data_china_transposed = All_data_china.transpose()
All_data_china_transposed = All_data_china_transposed.drop(index=["Country Name", "Country Code", "Indicator Code"])
All_data_china_transposed = All_data_china_transposed[30:51]

Urban_data_transposed_mean = np.mean(Urban_data_transposed[Countries_list])



C = CO2_data_transposed[0:5]
C = C[["India", "Canada"]]



lineplot(CO2_data_transposed, Countries_list,
         "CO\N{SUBSCRIPT TWO} Emission(kt)", "CO\N{SUBSCRIPT TWO}")

lineplot(Urban_data_transposed, Countries_list, "Urban Population", "UP")

barplot(C, "CO2", "CO2222")

heatmap(All_data_china_transposed)

pieplot(Urban_data_transposed_mean, "Urban Population of Different Countries", "Urban population")






print(All_data_china_transposed.columns)









