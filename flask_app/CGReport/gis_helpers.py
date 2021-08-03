## imports for gis

from arcgis.gis import GIS,Layer
from arcgis.features import FeatureLayer,FeatureCollection,FeatureSet,FeatureLayerCollection
import pandas as pd



def _GIS():
    url="https://tj4z3jkq44fcm9vl.maps.arcgis.com/home/organization.html"
    user="Tjstets"
    pswd="ppq2nDTYt1dt8UlX"
    gis = GIS(url,user,pswd)
    return gis


def get_data_feature_layer(layer_needed = 'facilities'):
    '''Takes a string of econ to specify the Economic_Development_Opportunities
       Layer or no string for the Facilities layer. Returns specified layer'''
# create gis object
    gis = _GIS()
    itemid="28b39d8a0fbb492883476cdfbf8343da"
    item = gis.content.get(itemid)

    edevLyer = item.layers[2]
    facLyer = item.layers[0]

    if layer_needed == 'econ':
        return edevLyer
    elif layer_needed == 'facilities':
        return facLyer

# def query_data(layer,form):
#     '''
#         Takes a specified layer string : 'econ' or 'facilities' and a dictionary
#         The layer string gets the necessary layer for query processing. The
#         dictionary is used to form the where clause used in the query method to
#         return features from the gis layer.
#     '''
#     data_table = get_data_feature_layer(layer)
    
#     where_clause = f"""ACREAGE BETWEEN {float(filter["amin"])} AND {float(filter["amax"])} 
#                     AND NMTC = '{filter["nmtc"]}' 
#                     AND FTZ = '{filter["ftz"]}' 
#                     AND OZ = '{filter["oz"]}' """

#     df = data_table.query(where=where_clause,as_df=True)
   
#     return df


