#%%
import gmaps
import googlemaps
import pandas as pd
import numpy as np
import compile_layer
import config

gmaps.configure(api_key= config.API_KEY)
fig = gmaps.figure(center=(25.127559567787795, 121.73770164184408), zoom_level=12)
layer_list = compile_layer.compile_layer('keelung')
# fig.add_layer(layer_list[i] for i in range(len(layer_list)))
fig.add_layer(layer_list[0])
fig
