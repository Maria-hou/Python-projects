# Author: Maria Hou
#
# Purpose:  This program utilizes tkinter as a GUI in
#           order to allow the user to choose a folder to
#           search from. The files that have been modified
#           in the last day in this folder, will then be
#           moved to a folder that the user also specifies.




# import the tkinter, time and shutil module
from tkinter import filedialog
import tkinter
from tkinter import *
import os
import time
import shutil

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master = master

        # Create the size of the window
        self.master.minsize(500,300) #(Height, Width)
        self.master.maxsize(500,300)

        self.master.title('Folder Explorer')

        # Create variables where the paths of the folders will
        # be kept
        self.folder_path = StringVar()
        self.destination_path = StringVar()

        # Create a label to tell the user to browse for a folder
        self.lbl1 = Label(self.master, text="Search this folder")
        self.lbl1.grid(row=0,column=0)

        # The Entry widget that will hold the path to the source folder
        self.txt_source = Entry(self.master, width=40)
        self.txt_source.grid(row=0, column=1, padx=5)


        # Create a browse button that opens a folder explorer
        self.button1 = Button(self.master, text="Browse", command=\
                              lambda:browse_button(self))
        self.button1.grid(row=0, column=3)

        # The Entry widget that will hold the path to the destination folder
        self.txt_dest = Entry(self.master, width=40)
        self.txt_dest.grid(row=1, column=1, padx=5)

        # Create another label to tell the user to browse for a
        # destination folder
        self.lbl3 = Label(self.master, text="Destination folder")
        self.lbl3.grid(row=1,column=0, pady=10)


        # Create another browse button
        self.button2 = Button(self.master, text="Browse", command=\
                              lambda:browse_button2(self))
        self.button2.grid(row=1, column=3)

        # Create a submit button
        self.button3 = Button(self.master, text="Submit", command=\
                              lambda:submit(self))
        self.button3.grid(row=2, column=1, padx=10)


        # This function gets the folder path chosen by the user
        def browse_button(self):
            # The user chooses the source folder
            source = filedialog.askdirectory()

            # Deletes whatever is in the txt_source entry widget and inserts
            # the path to the folder into it
            self.txt_source.delete(0, END)
            self.txt_source.insert(0, source)


        # This is the second function that gets the folder path from
        # the user
        def browse_button2(self):
            # The user chooses the destination folder
            dest = filedialog.askdirectory()

            # Deletes whatever is in the txt_dest entry widget and inserets
            # the path to the folder into it
            self.txt_dest.delete(0, END)
            self.txt_dest.insert(0, dest)


        # This is the function that sends the files from the source
        # folder to the destination folder
        def submit(self):

            # Retrieve the folder locations from the text entry widgets
            source = self.txt_source.get()
            destination = self.txt_dest.get()
            
            files = os.listdir(source)

            for i in files:

                # use os.path.join to create the full file path of i
                file_path = os.path.join(source, i)

                #get the last modification time since epoch
                file_time = os.path.getmtime(file_path)

                #get the current time since epoch
                now = time.time()

                #there are 86400 seconds in one day
                seconds = 86400

                #subtract the file modification time by current time and then
                #divide by how many seconds in one day will return how many
                #days since modification
                days = (now - file_time)/seconds

                #if it has been less than 1 day since modification,
                #the file will be moved to the destinatin folder
                if days < 1:
                    shutil.move(file_path, destination)


            # Create a notification that pops up telling the user
            # that the process is now complete
            notification = "Your recent files have now been moved from {} to {}."\
                           .format(source, destination)
            self.t1 = Text(height=5, width=27)
            self.t1.insert(END, notification)
            self.t1.grid(row=3, column=1,columnspan=2)




    
if __name__ == "__main__":
    root = Tk()
    App = Application(root)
    root.mainloop()
