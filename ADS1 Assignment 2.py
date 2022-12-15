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
    data_transposed = data_transposed.drop(index=["Country Code",
                                                  "Indicator Name",
                                                  "Indicator Code"])
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


def barplot(dat, label1, label2):
    """This function produces a barplot with the data given in argument
    and saves the image as a png file"""
    dat.plot(kind="bar")
    plt.title(label1, size=18)
    plt.xlabel("Year", size=12)
    plt.ylabel(label1, size=12)
    plt.xticks(rotation=90)
    plt.legend()
    plt.savefig(label2+"_barplot.png", dpi=300, bbox_inches="tight")
    plt.show()


def pieplot(dat, label1, label2):
    """This function produces a pieplot with the data given in argument
    and saves the image as a png file"""
    plt.figure()
    plt.pie(dat, autopct="%1.1f%%")
    plt.title(label1, size=15)
    plt.legend(bbox_to_anchor=(1, 1), labels=Countries_list)
    plt.savefig(label2+"_pieplot.png", dpi=300, bbox_inches="tight")
    plt.show()


def heatmap(dat, label):
    """This function produces a correlation heatmap with the data
    given in argument and saves the image as a png file"""
    dat = dat.apply(pd.to_numeric)
    dat = dat[indicators]
    corr = dat.corr()
    plt.title("Different Indicators of China", size=20)
    sns.heatmap(corr, annot=True, linewidths=0, square=True, cmap='Blues')
    plt.savefig(label+"_heatmap.png", dpi=300, bbox_inches="tight")
    plt.show()


Countries_list = ["Australia", "Brazil", "China",
                  "United Kingdom", "India", "United States"]

"""Reading CO2.csv file using read function and assigning
the returned valuse to two variables"""
CO2_data, CO2_data_transposed = read_data("CO2.csv")
# filtering the years of the CO2_data
CO2_data_transposed = CO2_data_transposed[30:51]

"""Reading Urban Population.csv file using read function and assigning
the returned valuse to two variables"""
Urban_data, Urban_data_transposed = read_data("Urban Population.csv")
# filtering the years of the Urban_data_transposed
Urban_data_transposed = Urban_data_transposed[30:51]

# Selecting the indicators to create a dataframe to plot heatmap
indicators = ["Population, total", "Urban population", "CO2 emissions (kt)",
              "CO2 emissions from solid fuel consumption (kt)",
              "Methane emissions (kt of CO2 equivalent)",
              "Electricity production from coal sources (% of total)"]

"""Reading All Data.csv file using read function and assigning
the returned valuse to two variables"""
All_data, All_data_transposed = read_data("All Data.csv")
All_data_china = All_data[(All_data["Country Name"] == "China")]
All_data_china = All_data_china.set_index("Indicator Name")
All_data_china_transposed = All_data_china.transpose()
All_data_china_transposed = All_data_china_transposed.drop(
    index=["Country Name", "Country Code", "Indicator Code"])
All_data_china_transposed = All_data_china_transposed[30:51]

# Finding the mean of the rows using numpy functio to plot the pieplot
Urban_data_transposed_mean = np.mean(Urban_data_transposed[Countries_list])

"""Reading Methane.csv file using read function and assigning
the returned valuse to two variables"""
Methane_data, Methane_data_transpose = read_data("Methane.csv")
Methane_data_transpose = Methane_data_transpose[30:51]
Methane_data_transpose = Methane_data_transpose[["China", "United States"]]

"""Reading Urban Population Growth file using read function and assigning
the returned valuse to two variables"""
Urb_popgr_data, Urb_popgr_data_transpose = read_data(
    "Urban Population Growth.csv")
Urb_popgr_data_transpose_mean = np.mean(
    Urb_popgr_data_transpose[Countries_list])

# calling lineplot function using CO2 Emission data
lineplot(CO2_data_transposed, Countries_list,
         "CO\N{SUBSCRIPT TWO} Emission(kt)", "CO\N{SUBSCRIPT TWO}")

# calling lineplot function using Urban Population data
lineplot(Urban_data_transposed, Countries_list, "Urban Population", "UP")

# calling barplot function using Methane Emission data
barplot(Methane_data_transpose, "Methane Emission (kt)", "Methane")

# calling correlation heatmap function using data of China
heatmap(All_data_china_transposed, "china")

# calling pieplot function using urban population growth data
pieplot(Urb_popgr_data_transpose_mean,
        "Urban Population Growth of Different Countries(1990-2010)",
        "Urban population Growth")
