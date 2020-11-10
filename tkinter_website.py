# Author: Maria Hou
#
# Purpose:  This program utilizes tkinter as a GUI
#           to create a website in a new tab using
#           the text that the user entered.


# import webbrowser as well as tkinter
import webbrowser
import tkinter 
from tkinter import *

class Application(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        self.master = master

        # Create the size of the window and make it fixed
        self.master.geometry("600x400")
        self.master.resizable(width=False,height=False)
        
        self.master.title('Customize Your Web Page!')

        # Create a label to describe the widget's function
        self.label1 = Label(self.master, text = 'Enter your desired text to be \
displayed in a new web page',font=('Helvetica',12))
        self.label1.pack(pady=(30,15))

        # Create an entry for input
        self.data = StringVar()
        self.entry1 = Entry(self.master, textvariable = self.data, font=('Helvetica',\
                                                                10))
        self.entry1.pack(ipadx=150, ipady=30)

        # Create a submit button that connects to the function new_website
        self.button1 = Button(self.master,text='Create Website', command=lambda:new_website(self), \
                            bg='green', fg='white',font=('Helvetica',14))
        self.button1.pack(pady=(20,0))


        # this function gets the input from the entry box, and creates a website
        def new_website(self):
            text = self.data.get()

            # Create a new html file named website. Return error if exits
            f = open("website.html","x")

            # This is the text that will be written in the html file
            message = """
        <html>
                <body>
                    <h1>
                        {}
                    </h1>
                </body>
            </html>""".format(text)
            f.write(message)
            f.close()
            webbrowser.open_new_tab('website.html')

            # Create new label that tells the user that the task is complete
            self.label2 = Label(text='Your website is now created!',\
                              font=('Helvetica',12))
            self.label2.pack(pady=(20,0))
    

if __name__ == "__main__":
    root = Tk()
    App = Application(root)
    root.mainloop()
