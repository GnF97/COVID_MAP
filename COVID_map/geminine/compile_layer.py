import pdfprcsd
import storage_unit
import layerrr
from os import walk

def compile_layer(CityName):
    layer_list = []
    photossspath = f"/home/timlovefixie1997/COVID_map/photosss/{CityName}/"
    filenames = next(walk(photossspath), ([], None, None))[2]
    path_list = [photossspath + fn for fn in filenames]
    for p in path_list:
        layer = layerrr.layers(storage_unit.storage_unit(pdfprcsd.address_query(p)))
        layer_list.append(layer)
    return layer_list

# print(compile_layer('keelung'))