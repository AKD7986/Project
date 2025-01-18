from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from analysis import analysisclass
from newfetch import soldrecords
import pymysql as pymysql
from PIL import ImageTk, Image
import detailspage as dp
import joblib
import sklearn
from sklearn.ensemble import RandomForestRegressor
model = joblib.load('price_prediction2.joblib')



class FormPage:
    def __init__(self):
        self.window = Tk()
        self.window.minsize(1400, 800)
        self.window.title("Predictor_App")
        #self.window.configure(bg='#A1BE95')  # Change 'light blue' to your desired color
        self.window.state('zoomed')

        carsize_w = 1400
        carsize_h = 800
        self.carimg1 = ImageTk.PhotoImage(Image.open("mypic//one.jpg").resize((carsize_w, carsize_h)))
        self.carimglbl = Label(self.window, image=self.carimg1)
        self.carimglbl.place(x=0, y=0)

        # Set window size to fit the screen
        self.heading = Label(self.window, text="House Price Prediction", font=('Aerial', 24, 'bold'), bg=dp.btcolor,fg='white')
        self.heading.pack(pady=20)

        self.head = Label(self.window, text="Fill a Form")
        self.title = Label(self.window, text="House Details Form")

        #-----------------------------Labels--------------------------------------------------

        bold_font = ('Arial', 12, 'bold')
        ariel_font = ('Times New Roman', 12, 'bold')
        self.L1 = Label(self.window, text="No of Bedrooms", font=bold_font, bg='white', fg='#000000')  # Black text
        self.L2 = Label(self.window, text="No of Bathrooms", font=bold_font, bg='white', fg='#000000')
        self.L3 = Label(self.window, text="Living Area", font=bold_font, bg='white', fg='#000000')
        self.L4 = Label(self.window, text="Lot Area", font=bold_font, bg='white', fg='#000000')
        self.L5 = Label(self.window, text="No of Floors", font=bold_font, bg='white', fg='#000000')
        self.L6 = Label(self.window, text="Waterfront Present", font=bold_font, bg='white', fg='#000000')
        self.L7 = Label(self.window, text="House Condition", font=bold_font, bg='white', fg='#000000')
        self.L8 = Label(self.window, text="House Grade (Between 4 to 13)", font=bold_font, bg='white', fg='#000000')
        self.L9 = Label(self.window, text="House Area (Excluding Basement)", font=bold_font, bg='white', fg='#000000')
        self.L10 = Label(self.window, text="Area of the Basement", font=bold_font, bg='white', fg='#000000')
        self.L11 = Label(self.window, text="Built Year", font=bold_font, bg='white', fg='#000000')
        self.L12 = Label(self.window, text="Renovation Year", font=bold_font, bg='white', fg='#000000')
        self.L13 = Label(self.window, text="Postal Code", font=bold_font, bg='white', fg='#000000')
        self.L14 = Label(self.window, text="Living Area (Renovation)", font=bold_font, bg='white', fg='#000000')
        self.L15 = Label(self.window, text="Lot Area (Renovation)", font=bold_font, bg='white', fg='#000000')
        self.L16 = Label(self.window, text="No of Schools Nearby", font=bold_font, bg='white', fg='#000000')
        self.L17 = Label(self.window, text=" - - - - - -",bg='white', font=('Times New Roman', 15, 'bold'))

        #------------------------Entry fields-------------------------------------------
        self.t1 = Entry(self.window,font=ariel_font)
        self.t2 = Entry(self.window,font=ariel_font)
        self.t3 = Entry(self.window,font=ariel_font)
        self.t4 = Entry(self.window,font=ariel_font)
        self.t5 = Entry(self.window,font=ariel_font)
        # self.t6 = Entry(self.window)
        # self.t7 = Entry(self.window)
        self.t8 = Entry(self.window,font=ariel_font)
        self.t9 = Entry(self.window,font=ariel_font)
        self.t10 = Entry(self.window,font=ariel_font)
        self.t11 = Entry(self.window,font=ariel_font)
        self.t12 = Entry(self.window,font=ariel_font)
        self.t13 = Entry(self.window,font=ariel_font)
        self.t14 = Entry(self.window,font=ariel_font)
        self.t15 = Entry(self.window,font=ariel_font)
        self.t16 = Entry(self.window,font=ariel_font)

        # Comboboxes for Waterfront present and House condition
        self.v6 = StringVar()
        self.com6 = Combobox(self.window,font=ariel_font, values=[ "No","Yes"], textvariable=self.v6)
        self.v7 = StringVar()
        self.com7 = Combobox(self.window,font=ariel_font, values=["Poor", "Fair", "Good", "Very Good", "Excellent"], textvariable=self.v7)

        #  Buttons
        self.b1 = Button(self.window, text="Predict Price", bg=dp.btcolor,fg='white', font=('Aerial', 15, 'bold'),command=self.prediction)
        self.b2 = Button(self.window, text="Reset", bg=dp.btcolor,fg='white', font=('Aerial', 15, 'bold'),command=self.clearPage)
        self.b3 = Button(self.window, text="Sale", bg=dp.btcolor,fg='white', font=('Aerial', 15, 'bold'),command=self.datasaved)
        self.b4 = Button(self.window, text="Analysis", bg=dp.btcolor,fg='white', font=('Aerial', 15, 'bold'),command=lambda :analysisclass(self.window))
        self.b5 = Button(self.window, text="Report", bg=dp.btcolor,fg='white', font=('Aerial', 15, 'bold'),command=lambda :soldrecords(self.window))
        self.b6 = Button(self.window, text="Exit", bg=dp.btcolor,fg='white', font=('Aerial', 15, 'bold'),command=self.Exit)


        #self.b1 = Button(self.window, text="Predict Price",bg='orange', command=self.show)

        self.ressize_w = 200
        self.ressize_h = 200
        self.pic = Label(self.window)


        #----------------------Placement-------------------------------------------------------------
        x1 = 20
        y1 = 10
        x_diff = 300
        y_diff = 40
        input_w = 150
        input_h = 25

        self.L1.place(x=x1, y=y1)
        self.t1.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L2.place(x=x1, y=y1)
        self.t2.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L3.place(x=x1, y=y1)
        self.t3.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L4.place(x=x1, y=y1)
        self.t4.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L5.place(x=x1, y=y1)
        self.t5.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L6.place(x=x1, y=y1)
        self.com6.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L7.place(x=x1, y=y1)
        self.com7.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L8.place(x=x1, y=y1)
        self.t8.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L9.place(x=x1, y=y1)
        self.t9.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L10.place(x=x1, y=y1)
        self.t10.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L11.place(x=x1, y=y1)
        self.t11.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L12.place(x=x1, y=y1)
        self.t12.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L13.place(x=x1, y=y1)
        self.t13.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L14.place(x=x1, y=y1)
        self.t14.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L15.place(x=x1, y=y1)
        self.t15.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L16.place(x=x1, y=y1)
        self.t16.place(x=x1 + x_diff, y=y1,width=input_w,height=input_h)
        y1 += y_diff
        self.L17.place(x=x1 + x_diff + 200, y=y1 - y_diff - 40, width=500, height=40)
        #--------------------------Buttons Placements--------------------------
        self.b1.place(x=x1, y=y1, width=200, height=40)
        self.b2.place(x=x1 + 220,y=y1, width=200, height=40)
        self.b3.place(x=x1+ 440,y=y1,width=200,height=40)
        self.b4.place(x=x1 + 660,y=y1, width=200, height=40)
        self.b5.place(x=x1 + 880, y=y1, width=200, height=40)
        self.b6.place(x=x1 + 1100, y=y1, width=200, height=40)
        #self.pic.place(x=900,y=400,width=150,height=150)

        #----------------------Functions--------------------------------------------------
        self.clearPage()
        self.setDefaultValue()
        self.dbconnection()

        self.window.mainloop()
    #------------Default values----------------------------------------------------------------------
    def setDefaultValue(self):
        self.t1.insert(0, "3")
        self.t2.insert(0, "2")
        self.t3.insert(0, "1680")
        self.t4.insert(0, "7000")
        self.t5.insert(0, "1")
        self.com6.current(0)
        self.com7.current(4)
        # self.t7.insert(0, "Good")
        self.t8.insert(0, "7")
        self.t9.insert(0, "1680")
        self.t10.insert(0, "0")
        self.t11.insert(0, "1968")
        self.t12.insert(0, "0")
        self.t13.insert(0, "122072")
        self.t14.insert(0, "1540")
        self.t15.insert(0, "7480")
        self.t16.insert(0, "3")

#-----------Clear values--------------------------------------------------------------

    def clearPage(self):
        self.t1.delete(0, END)
        self.t2.delete(0, END)
        self.t5.delete(0, END)
        self.t8.delete(0, END)
        self.t11.delete(0, END)
        self.t16.delete(0, END)
        self.L17.config(text=" - - - - - -", font=('Times New Roman', 15, 'bold'))
        # self.responseimg1 = ImageTk.PhotoImage(Image.open("myapp_images//question-mark.png").resize((self.ressize_w, self.ressize_h)))
        self.pic.config(image="")
        self.pic.place(x=900, y=400, width=0, height=0)
        self.b3['state'] = 'disabled'



    #-----------------------Print the values-------------------------------------------------
    # def show(self):
    #     # Printing the collected data
    #     print("No of bedrooms                =", self.t1.get())
    #     print("No of bathrooms               =", self.t2.get())
    #     print("Living area                   =", self.t3.get())
    #     print("Lot area                      =", self.t4.get())
    #     print("No of floors                  =", self.t5.get())
    #     print("Waterfront present            =", self.v6.get())
    #     print("House condition               =", self.v7.get())

#----------------------------Prediction Function--------------------------------------------

    def prediction(self):
        if self.nullvalidate() == False:
            return False
        if self.formvalidate() == False:
            return
        a1 = int(self.t1.get())
        a2 = float(self.t2.get())
        a3 = int(self.t3.get())
        a4 = int(self.t4.get())
        a5 = float(self.t5.get())
        a8 = int(self.t8.get())
        a9 = int(self.t9.get())
        a10 = int(self.t10.get())
        a11 = int(self.t11.get())
        a12 = int(self.t12.get())
        a13 = int(self.t13.get())
        a14 = int(self.t14.get())
        a15 = int(self.t15.get())
        a16 = int(self.t16.get())

        water = self.v6.get()
        if water == 'Yes':
            a6 = 1
        else:
            a6 = 0
        com = self.v7.get()
        if com == 'Poor':
            a7 = 0
        elif com == 'Fair':
            a7 = 1
        elif com == 'Good':
            a7 = 2
        elif com == 'Very Good':
            a7 = 3
        elif com == 'Excellent':
            a7 = 4
       # print(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16)

#-------------------------------Final Prediction-------------------------------------------------------

        self.answer = model.predict([[a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16]])

        print("------------",self.answer)
        self.output = round(self.answer[0])
        if self.output > 0:
            self.L17.config(text="You Can Sell this House at Rs. {}".format(self.output))
            ressize_w = 200
            ressize_h = 200

            self.pic.place(x=700, y=300, width=200, height=200)

            self.responseimg1 = ImageTk.PhotoImage(Image.open("mypic//up12.jpeg").resize((self.ressize_w, self.ressize_h)))
            self.pic.config(image=self.responseimg1)



            # carsize_w = 140
            # carsize_h = 80
            # self.carimg1 = ImageTk.PhotoImage(Image.open("up.jpeg").resize((carsize_w, carsize_h)))
            # self.carimglbl = Label(self.window, image=self.carimg1)
            # self.carimglbl.place(x=600, y=200)


            #self.b1['state'] = 'disabled'
            self.b3['state'] = 'normal'
            self.b2['state'] = 'normal'

        else:
            self.L17.config(text="Sorry you Cannot Sell this House ")
            #self.b1['state'] = 'normal'


    #---------------------------------------------------------------------------------------------------------------------



#---------------------------another's codes------------------------------------------

        # self.output = round(self.answer[0], 2)
        # if self.output < 0:
        #     self.L17.config(text="Sorry you cannot sell this car")
        #     self.responseimg1 = ImageTk.PhotoImage(
        #         Image.open("images.jpeg").resize((self.ressize_w, self.ressize_h)))
        #     self.responseimglbl.config(image=self.responseimg1)
        #     self.b1['state'] = 'disabled'
        # else:
        #     if presentPrice - 0.5 <= self.output <= presentPrice:
        #         self.output -= 0.5
        #     if presentPrice <= self.output:
        #         self.output = presentPrice - 0.2
        #     self.l17.config(text="You Can Sell The Car at Rs. {} Lakh(s)".format(self.output))
        #     self.responseimg1 = ImageTk.PhotoImage(
        #         Image.open("myapp_images//thumbs-up.png").resize((self.ressize_w, self.ressize_h)))
        #     self.responseimglbl.config(image=self.responseimg1)
        #     self.b1['state'] = 'normal'

    #----------------------------Database work---------------------------------------------------------------------------------------
    def dbconnection(self):
        try:
            self.conn = pymysql.connect(host='localhost', db='modeldata', user='root', password="")
            self.curr = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Database Error", "Error in Database Connection : \n" + str(e), parent=self.window)

    def datasaved(self):
        if self.nullvalidate() == False:
            return
        if self.formvalidate() == False:
            return
        try:
            from datetime import date
            today = date.today()
            todaydt = today.strftime("%Y-%m-%d")

            #bedrooms 	bathrooms 	lvarea 	loarea 	floors 	waterfront 	house_condition 	grade 	house_area_base
            # base_area 	built_year 	renew_year 	code 	lvrenew 	lorenew 	schools

            # srno	year	showroom_price	km_drived	previous_owner	fuel_type	seller_type	transmission	price	sold_on
            qry = " insert into  form_column (bedrooms, bathrooms, lvarea, loarea, floors, waterfront, house_condition, grade, house_area_base," \
                  " base_area, built_year, renew_year, code, lvrenew, lorenew, schools, price, date) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            rowcount = self.curr.execute(qry, (self.t1.get(),self.t2.get(),self.t3.get(),self.t4.get(),self.t5.get(),self.v6.get(),
                                               self.v7.get(),self.t8.get(),self.t9.get(),self.t10.get(),self.t11.get(),self.t12.get(),
                                               self.t13.get(),self.t14.get(),self.t15.get(),self.t16.get(),self.output,todaydt))
            self.conn.commit()
            if (rowcount == 1):
                messagebox.showinfo("Success", "House Sold Successfully", parent=self.window)
                self.b3['state'] = 'disabled'

        except Exception as e:
            messagebox.showerror("Query Error", "Error in Insertion : \n" + str(e), parent=self.window)

    def nullvalidate(self):
        if self.t1.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t2.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t3.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t4.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t5.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t8.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t9.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t10.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t11.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t12.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t13.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t14.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t15.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        elif self.t16.get() == "":
                messagebox.showwarning("Null Value Check", "First Fill the Form ", parent=self.window)
                return False
        return True

    #--------------Validation work---------------------------------------------------------------------------------------------------------------

    def formvalidate(self):
        if int(self.t1.get()) < 1 or int(self.t1.get()) > 12 or not(self.t1.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter no of Bedrooms between 1 to 12 ", parent=self.window)
            return False
        elif float(self.t2.get()) < 1 or float(self.t2.get()) > 8 or not(self.t2.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter no of Bathrooms between 1 to 8 ",
                                   parent=self.window)
            return False
        elif int(self.t3.get()) < 370 or int(self.t3.get()) > 13540 or not(self.t3.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter Living Area between 370 to 13540 ",
                                   parent=self.window)
            return False
        elif int(self.t4.get()) < 520 or int(self.t4.get()) > 1074218 or not(self.t4.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter Lot Area between 520 to 1074218 ",
                                   parent=self.window)
            return False
        elif float(self.t5.get()) < 1 or float(self.t5.get()) > 4 or not(self.t5.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter no of Floors between 1 to 4 ",
                                   parent=self.window)
            return False
        elif int(self.t9.get()) < 370 or int(self.t9.get()) > 9410 or not(self.t9.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter the Area between 370 to 9410 ",
                                   parent=self.window)
            return False
        elif int(self.t10.get()) < 0 or int(self.t10.get()) > 4820 or not(self.t10.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter the Basement between 0 to 4820 ",
                                   parent=self.window)
            return False
        elif int(self.t11.get()) < 1900 or not(self.t11.get().isdigit()):
            messagebox.showwarning("Validation Check", "Built Year should not be less then 1900 ",
                                   parent=self.window)
            return False
        # elif int(self.t11.get()) > int(self.t12.get()):
        #     messagebox.showwarning("Validation Check", "Built Year Should be Less than Renovation Year ",
        #                            parent=self.window)
        #     return False
        elif int(self.t13.get()) < 122003 or int(self.t13.get()) > 122072 or not(self.t13.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter the postal code between 122003 to 122072 ",
                                   parent=self.window)
            return False
        elif int(self.t14.get()) < 460 or int(self.t14.get()) > 6110 or not(self.t14.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter Living Area Renovation between 460 to 6110 ",
                                   parent=self.window)
            return False
        elif int(self.t15.get()) < 651 or int(self.t15.get()) > 560617 or not(self.t15.get().isdigit()):
            messagebox.showwarning("Validation Check", "Please Enter Lot Area Renovation between 651 to 560617 ",
                                   parent=self.window)
            return False
        # elif self.t16.get() < 1 or self.t16.get() > 3 or not(self.t16.get().isdigit()):
        #     messagebox.showwarning("Validation Check", "Please Enter Valid Range ",
        #                            parent=self.window)
        #     return False
        # elif len(self.t2.get()) < 1 or not (self.t2.get().isdigit()):
        #     messagebox.showwarning("Validation Check", "Please Enter Valid Showroom Price ", parent=self.window)
        #     return False
        # elif int(self.t2.get()) < 1:
        #     messagebox.showwarning("Validation Check", "Please Enter Showroom Price more than 1 lakh",
        #                            parent=self.window)
        #     return False
        # elif len(self.t3.get()) < 1 or not (self.t3.get().isdigit()):
        #     messagebox.showwarning("Validation Check", "Please Enter Valid Km Drived", parent=self.window)
        #     return False
        return True

    def Exit(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()



if __name__ == '__main__':
    FormPage()

