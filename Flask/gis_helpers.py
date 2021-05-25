## imports for gis

from arcgis.gis import GIS
import pandas as pd

def get_gis_data():
# create gis object
    url="https://tj4z3jkq44fcm9vl.maps.arcgis.com/home/organization.html"
    user="Tjstets"
    pswd="ppq2nDTYt1dt8UlX"
    gis = GIS(url,user,pswd)
    itemid="6b42a62bb8d1422d8346fa4a924e5d9a"

    table_item = gis.content.get(itemid)
    data_table = table_item.tables[0]

    return data_table

def query_data(filter):
    data_table = get_gis_data()
    
    where_clause = f"""ACREAGE BETWEEN {float(filter["amin"])} AND {float(filter["amax"])} 
                    AND NMTC = '{filter["nmtc"]}' 
                    AND FTZ = '{filter["ftz"]}' 
                    AND OZ = '{filter["oz"]}' """

    df = data_table.query(where=where_clause,as_df=True)
   
    return df
