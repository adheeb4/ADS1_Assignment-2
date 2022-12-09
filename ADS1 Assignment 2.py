# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:43:51 2022

@author: adheeb
"""

import pandas as pd
import matplotlib.pyplot as plt


def read_data(filename):
    data = pd.read_csv(filename, skiprows=4)
    data_transposed = data.set_index("Country Name").transpose()
    return data, data_transposed


def lineplot(dat, label, label1):
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


CO2_data, CO2_data_transposed = read_data("CO2.csv")
CO2_data_transposed = CO2_data_transposed.drop(index=["Country Code", "Indicator Name", "Indicator Code"])
CO2_data_transposed = CO2_data_transposed[30:51]

Urban_data, Urban_data_transposed = read_data("Urban Population.csv")
Urban_data_transposed = Urban_data_transposed.drop(index=["Country Code", "Indicator Name", "Indicator Code"])
Urban_data_transposed = Urban_data_transposed[30:51]

con = ["Australia", "Brazil", "China", "United Kingdom", "India", "United States"]


lineplot(CO2_data_transposed, "CO2 Emission(kt)", "CO2")
lineplot(Urban_data_transposed, "Urban Population", "UP")
