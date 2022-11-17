# LIBRARIES
import streamlit
import pandas as pd
import requests


# DATASETS
# List of fruits
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list.set_index('Fruit', inplace=True)



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
selection = list(my_fruit_list.index) if len(selection)==0 else selection
streamlit.dataframe(my_fruit_list.loc[selection])

# Section 3
streamlit.header('Fruityvice Fruit Advice')
fruit_selection = streamlit.multiselect("Choose your fruits", list(my_fruit_list.index), ['Watermelon', 'Banana'])

# Information about the fruit
fruityvice_response = [requests.get("https://fruityvice.com/api/fruit/"+fruit.lower()).json() for fruit in fruit_selection]
fruityvice_advice = pd.DataFrame.from_records(fruityvice_response)
streamlit.dataframe(fruityvice_advice)

