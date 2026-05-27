import pandas as pd
import sqlite3


df = pd.read_csv("students_file.csv")

print(df.head())


conn = sqlite3.connect("college.db")

df.to_sql("students",conn,if_exists="replace",index=False)

conn.close()

print("Upload successful!")