


import streamlit 
streamlit.title ('my parents new healthy dinner')


import streamlit 
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:" , list((my_fruit_list.index)))
streamlit.dataframe(my_fruit_list)                
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:" , list((my_fruit_list.index)))
streamlit.dataframe(my_fruit_list)


streamlit.multiselect("Pick some fruit fruits:",list(my_fruit_list.index),['Lemon' , 'Grapes'])
streamlit.dataframe(my_fruit_list)

fruits_selected =streamlit.multiselect("Pick some fruit fruits:",list(my_fruit_list.index),['Avocado' , 'Grapes'])
fruits_to_show =my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)


streamlit.header('Fruityvice Fruit Advice ! ') 
Fruityvice_respose = requests.get("https://www.fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


