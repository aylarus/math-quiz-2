from tkinter import *
from PIL import ImageTk, Image
import random 
global questions_answers 


class Start:
  
  def __init__(self, parent):  # this function is called every time the class is being used to create a new object

        self.bg_image = Image.open("math2.jpg")#adding a background image to the quiz program for the first screen 
        self.bg_image = self.bg_image.resize((450, 350), Image.ANTIALIAS)#the sizing for the image 
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
     

        self.quiz_frame = Frame(parent, bg="white", padx=1)
 
        self.quiz_frame.grid()  
        self.image_label = Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        #heading label for welcoming the end user
        self.heading_label = Label(self.quiz_frame,text="Welcome to the Algebra Quiz Program", font=("Comic Sans MS", "11"), bg="#DCF9F4")
        self.heading_label.grid(row=1, padx=87, pady=35)#placing of the text

        #second label telling info 
        self.user_label = Label(self.quiz_frame, text= "Click start quiz to begin the quiz\n OR Click exit quiz to exit the quiz", font=("Comic Sans MS", "11"), bg="#A8F0E4")
        self.user_label.grid(row=2, padx=90, pady=5)#placing of the text
 
        #button 1 (start)
        self.start_button = Button(self.quiz_frame,text="Start Quiz",font=("Comic Sans MS", "13", "bold"), bg="#62E4CF", command=self.name_collection, pady=10)
        self.start_button.grid(row=4, padx=30, pady=78, sticky=W)#placing of the text

        #button 2 (exit)
        self.exit_button = Button(self.quiz_frame,text="Exit Quiz", font=("Comic Sans MS", "13", "bold"), bg="#62E4CF", command=root.destroy, pady=10, padx=18)
        self.exit_button.grid(row=4, padx=30, pady=78, sticky=E)
        #placing of the text
 



       
  def name_collection(self):
        self.quiz_frame.destroy()#destroying the 1st screen/ 1st component 
        Starter(root)#after detroying the 1st component this will continue the program to go to the next component 

class Starter:
  
  def __init__(self, parent): # this function is called every time the class is being used to create a new object

        self.bg_image = Image.open("math2.jpg") #same image for the 2nd component  
        self.bg_image = self.bg_image.resize((450, 350), Image.ANTIALIAS) #sizing of the background image 
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
     

        self.quiz_frame = Frame(parent, bg="black")
 
        self.quiz_frame.grid()  
        self.image_label = Label(self.quiz_frame, image=self.bg_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)
        #exit button 
        self.exit_button = Button(self.quiz_frame,text="Exit Quiz", font=("Comic Sans MS", "8"), command=root.destroy)
        self.exit_button.grid(row=4, sticky=E, padx=10, pady=0)#sizing of the exit button

        #another label 
        self.heading_label = Label(self.quiz_frame,text="Welcome to the Algebra Quiz Program ", font=("Comic Sans MS", "11"), bg="lightcyan")
        self.heading_label.grid(row=1, padx=85, pady=35)#placing of the text/label

        #username label
        self.user_label = Label(self.quiz_frame, text="Enter a UserName: ", font=("Comic Sans MS", "13"), bg="#A8F0E4")
        self.user_label.grid(row=2, padx=90, pady=25)#placing of the username label
                #continue button to continue on to the next component where the questions are asked 
        self.continue_button = Button(self.quiz_frame,text="Continue",font=("Comic Sans MS", "13", "bold"),bg="#62E4CF",  command=self.contbutton)
        self.continue_button.grid(row=4, padx=0, pady=35)#plaing of the continue button
 
        #entry box to enter the username 
        self.entry_box = Entry(self.quiz_frame)
        self.entry_box.grid(row=3, padx=90, pady=25)


  #trial and error for the continue button so it the user left the box empty then 
  def name_collection(self):
     name= self.entry_box.get()
     if name.strip() != "" and len(name) <= 15:
       name.append(name)
       self.quiz_frame.destroy()#destroying the second component
       Quiz(root)#after destroying second compnent moving on to the next componet (the quiz questions)
     elif len (name) ==  0:
        self.continue_button.config(text="Please enter a Username", font=("Comic Sans MS", "10"))
        
      elif len(name) <= 2:#the user can only have 10 values this will stop the user from contuining
        self.continue_button.config(text="username has to be \n more than 2 values", font=("Comic Sans MS", "10"))
            
       else:
         self.name_collection()#coninuation from the continue button to the next compnent(the questions)
    
  



names = []
asked = []
score = 0
#10 questions for the quiz with the 4 different choices and the answer  
questions_answers = {
1: ["QUESTION:\n SOLVE: 2x+90=120, what is x?  ",
' 20',
' 28',
' 15', 
' 10',
' 15', 3],
2: ["QUESTION:\n SOLVE: 5x=10, what is x?      ",
' 2 ',
' 8 ',
' 4 ', 
' 0 ',
' 2 ', 1],
3: ["QUESTION:\n SOLVE: 2x=10, what is x?      ",
' 2 ',
' 5 ',
' 4 ', 
' 0 ',
' 5 ', 2],
4: ["QUESTION:\n SOLVE: 5x+40=50, what is x?   ",
' 2 ',
' 8 ',
' 5 ', 
' 0 ',
' 2 ', 1],
5: ["QUESTION:\n SOLVE: 99x+1=100, what is x?  ",
' 8 ',
' 0 ',
' 7 ', 
' 1 ',
' 1 ', 4],
6: ["QUESTION:\n SOLVE: 2x+0=12, what is x?    ",
' 2 ',
' 4 ',
' 6 ', 
' 8 ',
' 6 ', 3],
7: ["QUESTION:\n SOLVE: 5x=25, what is x?      ",
' 1 ',
' 3 ',
' 8 ', 
' 5 ',
' 5 ', 4],
8: ["QUESTION:\n SOLVE: 50x+23=173, what is x? ",
' 1 ',
' 5 ',
' 3 ', 
' 0 ',
' 3 ', 3],
9: ["QUESTION:\n SOLVE: 5x+69=129, what is x?  ",
' 12',
' 16',
' 18', 
' 14',
' 12', 1],
10: ["QUESTION:\n SOLVE: 2(6)-492=x, what is x?",
'450 ',
'-460',
'420 ', 
'-480',
'-480', 4],

}

def randomiser():#this will make the quiz pick the questions at random so if the user wants to do the quiz again it will be the same questions but in a different order now
  global qnum 
  qnum = random.randint(1,10)
  if qnum not in asked:
    asked.append(qnum)
  elif qnum in asked:
    randomiser()



class Quiz:
  def __init__(self, parent): # this function is called every time the class is being used to create a new object
   
        self.quiz_frame = Frame(parent, bg="black", pady=25, padx=60)
        self.quiz_frame.grid(padx=0, pady=0)

        randomiser()

        #the label of the quiz questions so it can show up on the screen on the 3rd component (named Quiz)
        self.question_label = Label(self.quiz_frame,text= questions_answers[qnum][0], font=("Comic Sans MS", "11"), bg="#DCF9F4")
        self.question_label.grid(row=1, padx=60, pady=4)
        self.var1=IntVar()#holds the radio buttons 

        #radio button 1 so the first choices will appear
        self.rb1 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][1], font=("Comic Sans MS", "11"), bg="#73E7D4", value=1, variable=self.var1, indicator=0, pady=10, padx=120)
        self.rb1.grid(row=2, pady=1, padx=40)#

        #radio button 2 so the second choices will appear
        self.rb2 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][2], font=("Comic Sans MS", "11"), bg="#73E7D4", value=2, variable=self.var1, indicator=0, pady=10, padx=120)
        self.rb2.grid(row=3, pady=1, padx=40)

        #radio button 3 so the third choices will appear
        self.rb3 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][3], font=("Comic Sans MS", "11"), bg="#73E7D4", value=3, variable=self.var1, indicator=0, pady=10, padx=120)
        self.rb3.grid(row=4, pady=1, padx=40)
                
        #radio button 4 so the forth choices will appear
        self.rb4 = Radiobutton(self.quiz_frame, text = questions_answers[qnum][4], font=("Comic Sans MS", "11"), bg="#73E7D4", value=4, indicator=0,  pady=10, padx=120,variable=self.var1)
        self.rb4.grid(row=5, pady=1, padx=0)

        #exit button is used so the user can exit anytime while doing the quiz if they dont want to do it anymore
        self.exit_button = Button(self.quiz_frame,text="Exit Quiz", font=("Comic Sans MS", "8"), command=root.destroy)
        self.exit_button.grid(row=7, sticky=E, padx=36)

        #score label is used to show how much the end user has scored and if they are loosing any points 
        self.score_label = Label(self.quiz_frame, text="SCORE", font=("Comic Sans MS", "11"),bg="#DCF9F4")
        self.score_label.grid(row=7, pady=1, padx=4,  sticky=W)

        #after the user has pick there choice the confirm button will  go to the next question 
        self.confirm_button = Button(self.quiz_frame, text="CONFIRM", bg="#63E4CF", command=self.test_progress, padx=30)
        self.confirm_button.grid(row=6, pady=5, padx=22)

  #the question label to new questions and possible answers as new radio button choices
  def questions_setup(self):
          randomiser()
          self.var1.set(0)
          self.question_label.config(text=questions_answers[qnum][0])
          self.rb1.config(text=questions_answers[qnum][1])
          self.rb2.config(text=questions_answers[qnum][2])
          self.rb3.config(text=questions_answers[qnum][3])
          self.rb4.config(text=questions_answers[qnum][4])


#confirm button for the questions window to be better 
  def test_progress(self):#pass the users choice
    global score#this score us there to be acessed to everyone 
    scr_label = self.score_label#shhowing the score because it will be different each time a question is answered 
    choice = self.var1.get()#get the users choice
    if len(asked)>9:#to determine it its the last question to end the quiz after
      if choice == questions_answers[qnum][6]:#cheking the qnum has the correct answer that is stored in index 6
        score+=1#adding a point after each correct answer 
        scr_label.configure(text=score)#it will change the score to the new score each time 
        self.confirm_button.config(text="confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed 
      
      else:
        print(choice)
        score+=0#score will stay the same if the questions is answered inccorectly 
        scr_label.configure(text="Incorrect the answer was:  " + questions_answers[qnum][5])#sayin the incorrect answer the the question that the end user put wrong 
        self.confirm_button.config(text="Confirm")#will change the test on the button to confirm
        self.endScreen()#to open endScreen when quiz is completed 

    else:
      if choice == 0:#if the user doesnt select and option
        self.confirm_button.config(text="Pick an option")#then the confirm button will say plase try again until the questions is answered and an option is selected
        choice=self.var1.get()#still get the answer if they chose it
       
        
      else:#if choice is correct
        if choice == questions_answers[qnum][6]:#if the choice is correct
          score+=1
          scr_label.configure(text=score)
          self.confirm_button.config(text="Confirm")
          self.questions_setup()#to move on to the next question

        else:#if the choice was inccorect
          print(choice)
          score+=0
          scr_label.configure(text="Incorrect the answer was:" + questions_answers[qnum][5])#telling the correct answer 
          self.confirm_button.config(text="Confirm")
          self.questions_setup()#moving to the next question

  def endScreen(self):
    root.withdraw()
    name = names[0]
    file = open("leaderBoard.txt", "a")#opens highscores, text file in append mode
    if name == "admin_reset":#to wipe scores in the list, admin eneters with the name
      file = open("leaderBoard.txt", "w")
    
    else:
      file.write( str(score))#turns the sucess rate into a string 
      file.write(" - ")#writes into the text file
      file.write(name+"\n")#writes the names into the text files and goes to a new line (\n)
      file.close()#closes the file

    inputFile = open("leaderBoard.txt", 'r')#opens the highscore files in read mode 
    lineList = inputFile.readlines()#linelist equals the each lines in the lists
    lineList.sort()#sorts the line alpabetically
    top=[]#display top scores 
    top5=(lineList[-5:])#the last 10 values in the list for top 10
    for line in top5:
      point=line.split(" - ")
      top.append((int(point[0]), point[1]))
    file.close()#closes the files 
    top.sort()
    top.reverse()
    return_string = " Your final score is: "
    for i in range (len(top)):
      return_string += "{} - {}\n".format(top[i][0], top[i][1])
      print(return_string)#for testing to show on the console
      
    open_endscreen = End(root)
    open_endscreen.listLabel.config(text=return_string)#this will config the label in the end screen class which is displaying the names of the top 5

class End:
    def __init__(self, parent): # this function is called every time the class is being used to create a new object
      background ="#62E4CF"
      self.end_box = Toplevel(root)
      self.end_box.title("End Box")

      self.end_frame = Frame(self.end_box, pady=40, padx=45, bg=background)
      self.end_frame.grid()
      #end heading 
      end_heading = Label (self.end_frame, text='You have now Completed the quiz', font=("Comic Sans MS", "11"), bg=background, pady=15)
      end_heading.grid(row=0)
      #exit button to end the quiz 
      exit_button = Button (self.end_frame, text='Exit quiz>>', width=10, font=("Comic Sans MS", "11"), command=self.close_end, pady=10, padx=10)
      exit_button.grid(row=4, pady=20, padx=5, sticky=E)

      #if 1st place is available/ what they got 
      self.listLabel = Label(self.end_frame, text="You are in 1st place", font=("Comic Sans MS", "11"), width=40, bg=background, padx=10, pady=10)
      self.listLabel.grid(row=2)



    def close_end(self):
      self.end_frame.destroy()
      self.end_box.destroy()
      root.withdraw()



if __name__ == "__main__":
  root = Tk()
  root.title("Maths Algebra Quiz Program")#name of the quiz 
  quiz_instance = Start(root)#to creat the frame with its widgets and passing root as i
  root.mainloop()#used do the window doesnt disapper