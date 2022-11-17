# LIBRARIES
import streamlit
import pandas as pd
import requests
import snowflake.connector


# DATASETS
# List of fruits
my_fruit_list = pd.read_csv("fruit_macros.txt")
my_fruit_list.set_index('Fruit', inplace=True)

# Add fruit "PEACH"
peach = """{
    "genus": "Prunus",
    "name": "Peach",
    "family": "Rosaceae",
    "order": "Rosales",
    "nutritions": {
        "carbohydrates": 15,
        "protein": 1,
        "fat": 0.5,
        "calories": 50,
        "sugar": 13
    }
}
"""
response_adding = requests.put("https://fruityvice.com/api/fruit/", data=peach)

# STREAMLIT STRUCTURE
# Section 1
streamlit.text(response_adding.content)
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
fruit_selection = list(my_fruit_list.index) if len(fruit_selection)==0 else selection

# Information about the fruit
fruityvice_response = [requests.get("https://fruityvice.com/api/fruit/"+fruit.lower()).json() for fruit in fruit_selection]
fruityvice_advice = pd.json_normalize(fruityvice_response)
streamlit.dataframe(fruityvice_advice)


