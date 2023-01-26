import streamlit as st
import json
import numpy as np
from util import bg_image
import matplotlib.image as mpimg
import config

# setup background image
st.set_page_config(page_title="Inventory Locator App", page_icon=":guardsman:", layout="wide",
                  initial_sidebar_state="auto",
                  )

# Create a dictionary to store the inventory
inventory = json.load(open('./data/inventory.json'))

def search_item(item_name):
    cols = st.columns(2)
    if item_name in inventory:
        item = inventory[item_name]
        locations = list(zip(item['zone'], item['shelf']))
        maps = preprocess_map(locations)
        cols[0].success(f"Item found: {item_name}")
        for l in locations:
            cols[0].write(f"Location: Zone {l[0]}, Shelf {l[1]}")
        display_map(maps)
    else:
        cols[0].error(f"Item not found: {item_name}")


def preprocess_map(locations):
    # plot image based on zone for code
    maps = []
    zones = []
    for l in locations:
        if l[0] not in zones:
            zones.append(l[0])
            im = mpimg.imread(f'./images/zone{l[0]}.png')
            maps.append(im)
        else:
            continue
    return maps

def display_map(maps):
    map_final = np.sum(maps, axis=0)
    st.image(map_final, caption='Your items are in the highlighted zones.', clamp=True)

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