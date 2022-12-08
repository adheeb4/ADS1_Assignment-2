# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:43:51 2022

@author: adheeb
"""

import pandas as pd


def read_data(filename):
    data = pd.read_csv(filename, skiprows=4)
    data_transposed = data.set_index("Country Name").transpose()
    return data, data_transposed


CO2_data, CO2_data_transposed = read_data("CO2.csv")
