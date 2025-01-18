from tkinter import *
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk,Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import detailspage as dp

class analysisclass:
    def __init__(self,home_window):
        self.window = Toplevel(home_window)
        self.window.title("House Price Predictor")
        self.w = self.window.winfo_screenwidth()
        self.h = self.window.winfo_screenheight()
        w1=self.w
        h1=self.h
        self.window.minsize(w1,h1)
        #self.window.geometry("%dx%d+%d+%d"%(w1,h1,w1/2,h1/2))
        self.window.state('zoomed')

        carsize_w=w1
        carsize_h=h1
        self.carimg1 = ImageTk.PhotoImage(Image.open("mypic//one.jpg").resize((carsize_w,carsize_h)))
        self.carimglbl = Label(self.window,image=self.carimg1)
        self.carimglbl.place(x=0,y=0)

        self.b1 = Button(self.window, text="Exit", bg=dp.btcolor, fg='white', font=('Aerial', 15, 'bold'),command=self.Exit)
        self.b1.place(x=1150, y=650, width=200, height=40)

        # ----------------- widgets -----------------------------------------------------
        self.window.config(background='black')
        self.headlbl = Label(self.window, text="Analysis",bg='#1c96c5',foreground='white',font=('Aerial',22,'bold'))
        self.headlbl.place(x=500, y=20,width=250,height=50)

        self.l1 = Label(self.window, text="Analys Data with Price",bg='#1c96c5',foreground='white',font=('Aerial',15,'bold'))
        self.l1.place(x=40,y=100)
        x1=5
        y1=200
        x_dif=460

        car_data = pd.read_csv('house_price.csv')


        figure1 = plt.Figure(figsize=(5, 5), dpi=90)
        ax1 = figure1.add_subplot(111)
    #     #------------ background ------------------------------
        figure1.patch.set_facecolor('#ADD8E6')
        ax1.set_facecolor(dp.headbkcolor)
        ax1.xaxis.label.set_color(dp.textcolor)
        ax1.yaxis.label.set_color(dp.textcolor)
        ax1.tick_params(axis='x', colors=dp.textcolor)
        ax1.tick_params(axis='y', colors=dp.textcolor)
        diagram = FigureCanvasTkAgg(figure1, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*0,y=y1)
        ax1.set_title('Built Years v/s Price', color=dp.textcolor)
        car_data.plot(kind='scatter',x='Built Year', y='Price',color=dp.diagram_color, legend=True, ax=ax1)

        figure2 = plt.Figure(figsize=(5,5), dpi=90)
        ax2 = figure2.add_subplot(111)
    #
    #     #------------ background ------------------------------
        figure2.patch.set_facecolor('#ADD8E6')
        ax2.set_facecolor(dp.headbkcolor)
        ax2.xaxis.label.set_color(dp.textcolor)
        ax2.yaxis.label.set_color(dp.textcolor)
        ax2.tick_params(axis='x', colors=dp.textcolor)
        ax2.tick_params(axis='y', colors=dp.textcolor)
        diagram = FigureCanvasTkAgg(figure2, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*1,y=y1)
        ax2.set_title('No of Bedrooms v/s Price', color=dp.textcolor)
        car_data.plot(kind='scatter',x='No of bedrooms', y='Price',color=dp.diagram_color, legend=True, ax=ax2)

        figure3 = plt.Figure(figsize=(5,5), dpi=90)
        ax3= figure3.add_subplot(111)

    #     #------------ background ------------------------------
        figure3.patch.set_facecolor('#ADD8E6')
        ax3.set_facecolor(dp.headbkcolor)
        ax3.xaxis.label.set_color(dp.textcolor)
        ax3.yaxis.label.set_color(dp.textcolor)
        ax3.tick_params(axis='x', colors=dp.textcolor)
        ax3.tick_params(axis='y', colors=dp.textcolor)
        diagram = FigureCanvasTkAgg(figure3, self.window)
        diagram.get_tk_widget().place(x=x1+x_dif*2,y=y1)
        ax3.set_title('House Grade v/s Price', color=dp.textcolor)
        car_data.plot(kind='scatter',x='house grade', y='Price',color=dp.diagram_color, legend=True, ax=ax3)


        self.window.mainloop()


    def Exit(self):
        ans = messagebox.askquestion("Confirmation", "Are you sure to Close ? ", parent=self.window)
        if ans == 'yes':
            self.window.destroy()


if __name__ == '__main__':
    dummy=Tk()
    obj = analysisclass(dummy)
    dummy.mainloop()
