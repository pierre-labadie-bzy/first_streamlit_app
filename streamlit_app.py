import streamlit
import pandas as pd
import requests
import snowflake.connector

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favourites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# Let's put a pick list here so they can pick the fruit they want to include 
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Strawberries','Apple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/' + 'kiwi')
# Normalise data from fruityvice
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# Put data from fruityvice into a df
streamlit.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List contains:")
df = streamlit.dataframe(my_data_rows)

fruit_add = streamlit.text_input('What fruit would you like to add?')
streamlit.text(f'Thanks for adding {fruit_add}')
insert into pc_rivery_db.public.fruit_load_list values ('lychee');

