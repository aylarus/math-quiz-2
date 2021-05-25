from tkinter import *
from PIL import ImageTk, Image
import random 
names = []
global questions_answers 
asked=[]
score=0

questions_answers = {
1: ["QUESTION:\n SOLVE: 2x+90=120, what is x?",
'20',
'18',
'15', 
'10',15],
2: ["QUESTION:\n SOLVE: 5x=10, what is x?",
'2',
'8',
'4', 
'0',2],
3: ["QUESTION:\n SOLVE: 2x=10, what is x?",
'2',
'5',
'4', 
'0',5],
4: ["QUESTION:\n SOLVE: 5x+40=50, what is x?",
'2',
'8',
'5', 
'0',2],
5: ["QUESTION:\n SOLVE: 99x+1=100, what is x?",
'88',
'1',
'78', 
'0',1],

}

def randomiser():
  global qnum 
  qnum = random.randint(1,5)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()




class Quiz:
    def __init__(self, parent):  

        self.bg_image = Image.open("math2.jpg")  
        self.bg_image = self.bg_image.resize((450, 350), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
     

        self.quiz_frame = Frame(parent, bg="white")
 
        self.quiz_frame.grid()  
        self.image_label = Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.heading_label = Label(self.quiz_frame,text="Welcome to the Maths Quiz Program ", font=("Comic Sans MS", "11"), bg="lightcyan")
        self.heading_label.grid(row=1, padx=85, pady=35)


        self.user_label = Label(self.quiz_frame, text="Enter your Name: ", font=("Comic Sans MS", "13"), bg="#A8F0E4")
        self.user_label.grid(row=2, padx=90, pady=25)
 

        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=3, padx=90, pady=25)


        self.continue_button = Button(self.quiz_frame,text="Continue",font=("Comic Sans MS", "13", "bold"), command=self.name_collection)
        self.continue_button.grid(row=4, padx=90, pady=35)

    def name_collection(self):
        name = self.entry_box.get()
        names.append(name) 
        self.continue_button.destroy()
        self.entry_box.destroy() 
        self.heading_label.destroy()
        self.user_label.destroy()
        Quiz(root)

class Quiz:
    def __init__(self, parent):  
   
        self.quiz_frame = Frame(parent, bg="white")
        self.quiz_frame.grid(pady=0, padx=0)  
        randomiser()

  
        self.question_label = Label(self.quiz_frame,text= questions_answers[qnum][0], font=("Comic Sans MS", "11"), bg="lightcyan")
        self.question_label.grid(row=1, padx=85, pady=35)
        self.var1=IntVar()

        self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font=("Comic Sans MS", "11"), bg="#62E4CF", value=1, variable=self.var1, indicator=0, pady=5, padx=100)
        self.rb1.grid(row=2)

        self.rb2 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][2], font=("Comic Sans MS", "11"), bg="#62E4CF", value=2, variable=self.var1, indicator=0, pady=10, padx=100)
        self.rb2.grid(row=3)

        self.rb3 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][3], font=("Comic Sans MS", "11"), bg="#62E4CF", value=3, variable=self.var1, indicator=0,  pady=10, padx=100)
        self.rb3.grid(row=4)
                
        self.rb4 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][4], font=("Comic Sans MS", "11"), bg="#62E4CF", value=4, variable=self.var1, indicator=0,  pady=10, padx=100)
        self.rb4.grid(row=5)

        self.confirm_button= Button(self.quiz_frame, text="Confirm",bg="#A8F0E4", command=self.test_process)
        self.confirm_button.grid(row=6, pady=10, padx=150)
        
        
        def question.setup(self):
          randomiser()
          self.var1.set(0)
          self.question_label.config(text=questions_answer[qnum][0])
          self.rb1.config(text=questions_answer[qnum][1])
          self.rb2.config(text=questions_answer[qnum][2])
          self.rb3.config(text=questions_answer[qnum][3])
          self.rb4.config(text=questions_answer[qnum][4])




          def test_process(self):
            global score






if __name__ == "__main__":
    root = Tk()
    root.title("Maths Quiz Program")
    quiz_instance = Quiz(root)
    root.mainloop() 
 