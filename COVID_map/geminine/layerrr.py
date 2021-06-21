import gmaps
import googlemaps
import config

pdf = [5+i for i in range(101)]
color_list = [f"{'rgba'}{(0, 0, 0+i, 0.5)}" for i in range(len(pdf))]

gmaps_key = googlemaps.Client(key= config.API_KEY)

def best_Poly(coord_sets):
  Polygon_points = coord_sets.tolist()
  x_set = [coord_sets[i][0] for i in range(len(coord_sets))]
  y_set = [coord_sets[i][1] for i in range(len(coord_sets))]
  for i in range(len(coord_sets)):
    if min(x_set) < coord_sets[i][0] < max(x_set):
      if min(y_set) < coord_sets[i][1] < max(y_set):
        Polygon_points.remove(coord_sets[i])
  return Polygon_points

def layers(location):
    patient_polygon = gmaps.Polygon(
        best_Poly(location),
        fill_color= color_list[0],
        stroke_color= color_list[0]
    )
    patient_layer = gmaps.drawing_layer(
        features=[patient_polygon],
        show_controls=False
    )
    return patient_layer

