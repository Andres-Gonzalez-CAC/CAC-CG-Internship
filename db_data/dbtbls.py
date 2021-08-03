# Import sqlite 3 and pandas to create db from excel file
import sqlite3
import pandas as pd
from pathlib import Path

def main():
    path = "C:/Users/stets/Desktop/2021_GIS_Internship/CAC-CG-Internship/flask_app/CGReport/Building_Information.sqlite3"
    dbpath = path + "/Building_Information"
    conn = sqlite3.connect(path)
    cursor = conn.cursor()


#create dataframe from excel file
    file = Path("C:/Users/stets/Desktop/2021_GIS_Internship/CAC-CG-Internship/db_data/supplementary_info.csv")
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(" ","_")
    df.columns = df.columns.str.replace(".","")
    df.columns = df.columns.str.replace("?","")
    df.columns = df.columns.str.replace("/","")
    df.columns = df.columns.str.replace("\r","")
    df.columns = df.columns.str.replace("\n","")
    df.columns = df.columns.str.replace("(","")
    df.columns = df.columns.str.replace(")","")
    df.columns = df.columns.str.replace("•","")
    df.columns = df.columns.str.replace(',','')
    df.columns = df.columns.str.replace('$','')
    df.columns = df.columns.str.replace('#','Num')
    df.columns = df.columns.str.replace('-','_')
    df.columns = df.columns.str.replace(':','')


   



    # create_table_sql = pd.io.sql.get_schema(df.reset_index(), table_name)
    
   
    df.to_sql(name="Supplementary_Site_Info", con = conn, if_exists='replace',index=False)
    # cursor.close()
    # conn.close()
if __name__ == "__main__":
    main()
