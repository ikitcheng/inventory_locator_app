import streamlit as st
from util import bg_image
import config

# setup background image
st.set_page_config(page_title="Inventory Locator App", page_icon=":guardsman:", layout="wide",
                  initial_sidebar_state="auto",
                  )

# Create a dictionary to store the inventory
inventory = {
    "item1": {"quantity": 10, "location": "Aisle 1, Shelf 2"},
    "item2": {"quantity": 5, "location": "Aisle 2, Shelf 3"},
    "item3": {"quantity": 2, "location": "Aisle 3, Shelf 1"}
}

def search_item(item_name):
    if item_name in inventory:
        item = inventory[item_name]
        cols = st.columns(2)
        cols[0].success(f"Item found: {item_name}")
        cols[0].write(f"Quantity: {item['quantity']}")
        cols[0].write(f"Location: {item['location']}")
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