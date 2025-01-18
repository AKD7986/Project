from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk ,Label
import pymysql as pymysql
import pandas as pd
from PIL import ImageTk,Image
import detailspage as dp

class soldrecords:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("House Solds Records")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        self.window.state('zoomed')
        self.columns = (
            "no_of_bedrooms", "no_of_bathrooms", "living_area", "lot_area", "no_of_floors", "waterfront",
            "house_condition",
            "house_grade", "house_basement", "basement_area", "built_year", "renew_year", "postal_code", "living_renew",
            "lot_renew", "no_of_schools", "price", "date"
        )
        self.display_data(home_window)


    def connect_to_database(self):
        try:
            self.connection = mysql.connector.connect(host='localhost', db='modeldata', user='root', password="")
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error while connecting to MySQL: {e}")
            return False
        return False

    def fetch_data_from_db(self):
        if self.connect_to_database():
            cursor = self.connection.cursor()
            try:
                cursor.execute("""
                    SELECT 
                        bedrooms,
                        bathrooms,
                        lvarea,
                        loarea,
                        floors,
                        waterfront,
                        house_condition,
                        grade,
                        house_area_base,
                        base_area,
                        built_year,
                        renew_year,
                        code,
                        lvrenew,
                        lorenew,
                        schools,
                        price,
                        date
                    FROM form_column
                """)
                records = cursor.fetchall()
                return records
            except Error as e:
                print(f"Error fetching data: {e}")
                return []
            finally:
                if self.connection.is_connected():
                    cursor.close()
                    self.connection.close()
        return []


    def display_data(self,home_window):

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)



        tree = ttk.Treeview(frame, columns=self.columns, show="headings")

        for col in self.columns:
            tree.heading(col, text=col, anchor=tk.CENTER)
            tree.column(col, anchor=tk.CENTER, width=90, stretch=tk.NO)

        h_scrollbar = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=h_scrollbar.set)

        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        tree.pack(fill=tk.BOTH, expand=True)

        records = self.fetch_data_from_db()
        for row in records:
            tree.insert("", tk.END, values=row)

        self.window.mainloop()


if __name__ == '__main__':
    dummy=Tk()
    obj = soldrecords(dummy)
    dummy.mainloop()
