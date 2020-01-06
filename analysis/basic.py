# Education analysis
#
# Author : Rohit Suratekar
# Year: 2020
#
# This analysis is performed on Barro-Lee Educational Attainment Data (Barro
# and Lee 2010) http://www.barrolee.com/
#
# Main data file : data/LeeLee_v1.dta
# Data is obtained from http://www.barrolee.com/data/full1.htm on 6 Jan 2020

import matplotlib.pyplot as plt
from SecretColors import Palette

from helpers.constants import *
from helpers.utils import get_data

p = Palette()


def data_stats():
    data = get_data()
    print(f"Number of entries : {len(data)}")
    print(f"Number of countries : {len(data[COL_COUNTRY].unique())}")
    print(f"Number of years : {len(data[COL_YEAR].unique())}")

    print(data[[COL_POPULATION, COL_YEAR]])


def run():
    data_stats()
