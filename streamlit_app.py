# LIBRARIES
import streamlit
import pandas
import requests


# DATASETS
# List of fruits
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit', inplace=True)

# Information about the fruit
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon").json()


# STREAMLIT STRUCTURE
# Section 1
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

# Section 2
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
selection = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
streamlit.dataframe(my_fruit_list.loc[selection])

# Section 3
streamlit.header('Fruityvice Fruit Advice')
streamlit.dataframe(pd.read_json("https://fruityvice.com/api/fruit/watermelon"))
