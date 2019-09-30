import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model  # download with "pip install -U scikit-learn"

"""
DO A LOT OF RESEARCH INTO THIS STUFF
"""

"""
finish later it is getting late and experiment with documentation
get the data from:
life satisfaction - https://homl.info/4
gdp per capita - https://homl.info/5
"""

# load the data
"""
just getting files (maybe pandas works with them in a way), csv is comma separated values
panda gets the file that is data separated by commas already and adds commas to thousands
{stuff I haven't really worked with}
"""
life = pd.read_csv("life_satis_exercise_LS.csv", thousands=',')
"""
panda gets a tab separated file but debilitates it by each tab to be a comma
it then encodes it and sets not available values
works same way as other csv, but the data ins't as pure as csv so some work needs to be done
need to use deliminator of ',' to separate each by commas
{stuff I haven't really worked with}
"""
gdp = pd.read_csv("life_satis_exercise_GDP.csv", thousands=',',
                  delimiter=',', encoding='latin1', na_values='n/a')

# prepare data
"""
long function that combines the the two data-sets together
not sure if this is gone over so may need to do some research with
(dont know any of this or how to work with it)
(maybe look up documentation)
"""


def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index('Country', inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]


"""
combines both data-sets
x axis is gdp
y is life satisfaction
"""
country_stats = prepare_country_stats(life, gdp)
"""
x axis is the GDP per capita of the combine data
(dont know any of this or how to work with it)
(maybe look up documentation)
"""
x = np.c_[country_stats["GDP per capita"]]
"""
y axis is the life satisfaction of the combine data
(dont know any of this or how to work with it)
(maybe look up documentation)
"""
y = np.c_[country_stats["Life satisfaction"]]

# Visualize the data
"""
creates the plot off the combined data
sets the x and y axises
(dont know any of this or how to work with it)
(maybe look up documentation)
"""
country_stats.plot(kind="scatter", x="GDP per capita", y="Life satisfaction")
"""
displays the plot
"""
plt.show()

# select a linear model
"""
get linear regression model function from sklearn
(maybe look up documentation)
"""
model = sklearn.linear_model.LinearRegression()

# Train model
"""
train the model with both axises
(dont know this or how to work with it)
(maybe look up documentation)
"""
model.fit(x, y)

# make a prediction for cyprus
"""
prediction is off, though data has not been updated, not sure why
(dont know this or how to work with it)
(maybe look up documentation)
"""
x_new = [[20732]]  # Cyprus' GDP per capita
print(model.predict(x_new))  # output [[5.96242338]]





