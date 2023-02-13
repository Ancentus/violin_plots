import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Read the data set onto a pandas dataframe
data = pd.read_csv("gapminder_with_codes.csv")

# Extract the data for the year 2007
data_2007 = data[data["year"] == 2007]

# Create a figure with three subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

# Create a violin plot for life expectancy
sns.violinplot(x="lifeExp", data=data_2007, ax=axs[0])
axs[0].set_title("Life Expectancy in 2007")

# Create a violin plot for population
sns.violinplot(x="pop", data=data_2007, ax=axs[1])
axs[1].set_title("Population in 2007")

# Create a violin plot for GDP per capita
sns.violinplot(x="gdpPercap", data=data_2007, ax=axs[2])
axs[2].set_title("GDP Per Capita in 2007")

# Use streamlit to display the data and the figure
st.title("Data and Violin Plots for the Year 2007")
st.dataframe(data_2007)
st.pyplot(fig)
