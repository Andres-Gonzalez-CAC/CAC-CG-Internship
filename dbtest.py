import sqlite3
import pandas as pd

#function to read from database to dataframe
def db_to_df():
    db = 'Building_information.sqlite3'
    conn = sqlite3.connect(db)

    df = pd.read_sql('''SELECT * FROM Building_Site_Info 
                        WHERE SITE = "Site 1" ''',con=conn)
    print("Dataframe printing...")
    print(df)


#function to select from database
def dbread():
    db = 'Building_information.sqlite3'

    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute('''SELECT * FROM Building_Site_Info
                    Where Site = "Site 1"''')

    names = list(map(lambda x: x[0], cur.description))
    # print(names)
    count = 0
    for row in cur:
        count = count +1
        print(row)
    print(count)

# main function
def main():
    # dbread()
    db_to_df()

if __name__ == "__main__":
    main()