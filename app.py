import streamlit as st
import json
from util import bg_image
import config

# setup background image
st.set_page_config(page_title="Inventory Locator App", page_icon=":guardsman:", layout="wide",
                  initial_sidebar_state="auto",
                  )

# Create a dictionary to store the inventory
inventory = json.load(open('./data/inventory.json'))

def search_item(item_name):
    if item_name in inventory:
        item = inventory[item_name]
        location = list(zip(item['zone'], item['shelf']))
        cols = st.columns(2)
        cols[0].success(f"Item found: {item_name}")
        for l in location:
            cols[0].write(f"Location: Zone {l[0]}, Shelf {l[1]}")
    else:
        cols[0].error(f"Item not found: {item_name}")

def main():
    st.title("Inventory Locator App")
    st.write("Search for an item in the inventory:")
    cols = st.columns(2)
    item_name = cols[0].text_input("Item name:")
    if st.button("Search"):
        search_item(item_name)

# Load background image
bg_image.set_png_as_page_bg(
    f"{config.PATH_TO_IMAGES}/armani-exchange.png"
)
if __name__ == "__main__":
    main()