import osmnx as ox
from unidecode import unidecode


def get_streets(relation_id):
    # Definir las coordenadas del polígono a través de relation_id
    polygon = ox.geocoder.geocode_to_gdf(relation_id, which_result=None, by_osmid=True, buffer_dist=None)

    # Acceder al polígono geométrico
    polygon_geom = polygon['geometry'].iloc[0]

    # Obtener el grafo de la red de OpenStreetMap dentro del polígono
    G = ox.graph.graph_from_polygon(polygon_geom, network_type="drive")

    # Extraer los nombres de las calles del grafo
    street_names = []
    for u, v, k, data in G.edges(keys=True, data=True):
        if 'name' in data:
            names = data['name']
            if isinstance(names, str):
                street_names.append(names)
            else:
                street_names.extend(names)

    # Eliminar los nombres de calles duplicados
    unique_names = list(set(street_names))

    # Eliminar los acentos de los nombres de las calles
    normalized_street_names = [unidecode(name) for name in unique_names]

    # Ordenar la lista de calles alfabéticamente
    sorted_street_names = sorted(normalized_street_names)

    # Renderizar la plantilla con los nombres de las calles
    return sorted_street_names
