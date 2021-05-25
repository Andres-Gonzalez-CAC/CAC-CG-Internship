# Import sqlite 3 and pandas to create db from excel file
import sqlite3
import pandas as pd
from pathlib import Path

def main():
    dbname = "Building_Information"
    conn = sqlite3.connect(dbname + '.sqlite3')

#create dataframe from excel file

    df = pd.read_csv('sites.csv')
    df.to_sql(name="Sites", con = conn, if_exists='append',index=False)

if __name__ == "__main__":
    main()
