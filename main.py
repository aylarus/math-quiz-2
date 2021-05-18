from tkinter import *
from PIL import ImageTK, image


names = []

class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="white"# to set it as background color for all the label widgets

        self.bg_images= Images .open("mpic.jpg")#need to use image if need to resize
        self.bg_image = self.bg_images.resize((450, 350), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        #self.bg_image = PhotoImage(file="mpic.jpg")

        #frame set up
        self.quiz_frame=Frame(parent, bg = "white", padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Welcome to the Maths Quiz program ",  font=("Comic Sans MS","11"), bg="lightcyan")
        self.heading_label.grid(row=0, padx=20) 
        self.var1=IntVar() #holds value of radio buttons

        self.image_label= Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        #label for username
        self.user_label=Label(self.quiz_frame,text="Enter your Name: ",font=("Comic Sans MS","13"), bg="#A8F0E4")
        self.user_label.grid(row=1, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)

        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="blue", command=self.name_collection)
        self.continue_button.grid(row=3,  padx=20, pady=20)        
         
       

    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner

    
        

if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz program") 

    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear
 



