# LIBRARIES
import streamlit
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

# SNOWFLAKE CONNECTION SETTINGS
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()


def get_fruityvice_fruit(names):
    fruityvice_response = [requests.get("https://fruityvice.com/api/fruit/"+fruit.lower()).json() for fruit in names]
    fruityvice_advice = pd.json_normalize(fruityvice_response)
    return fruityvice_advice

def get_fruits_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("INSERT INTO FRUIT_LOAD_LIST VALUES ("+new_fruit+")")
        return "New fruit added."

# DATASETS
# List of fruits
my_fruit_list = pd.read_csv("fruit_macros.txt")
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
selection = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberry'])
selection = list(my_fruit_list.index) if len(selection)==0 else selection
streamlit.dataframe(my_fruit_list.loc[selection])

# Section 3
streamlit.header('Fruityvice Fruit Advice')
fruit_selection = streamlit.multiselect("Choose your fruits", list(my_fruit_list.index), ['Watermelon', 'Banana'])

# Information about the fruit
streamlit.dataframe(get_fruityvice_fruit(fruit_selection))

# SECTION 4
if streamlit.button('Get fruit load list'):
    data_rows = get_fruits_list()
    streamlit.dataframe(data_rows)

add_fruit = streamlit.text_input("Add fruit:")
if streamlit.button("Add fruit to the list"):
    streamlit.text(insert_row_snowflake(add_fruit))