# Import sqlite 3 and pandas to create db from excel file
import sqlite3
import pandas as pd

def main():
    dbname = "Building_Information"
    conn = sqlite3.connect(dbname + '.sqlite3')

#create dataframe from excel file
    df = pd.read_excel('st_transposed.xlsx')
    df.to_sql(name="Building_Site_Info", con = conn)

if __name__ == "__main__":
    main()
