from tkinter import *
from PIL import ImageTk, Image

names =[]
qnum = 1
score=0
#questions bank dictionary
questions_bank = {
  1: ["question1", "first and right answer", "second answer", "third answer", "forth answer", 1] ,
  2: ["question2", "first answer", "second answer", "third answer", "forth answer is right", 4] ,
  3: ["question3", "first answer", "second answer", "third answer is right", "forth answer", 3] ,
  4: ["question4", "first ", "second ansewr right", "third answer", "forth answer", 2] ,
  5: ["question5", "first ", "second answer right", "third answer", "forth answer", 2] ,
}


class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="orange"# to set it as background color for all the label widget

        #open image
        self.comp_image = Image.open("computer.jpg")
        self.comp_image = self.comp_image.resize((250,250), Image.ANTIALIAS)
        self.comp_image = ImageTk.PhotoImage(self.comp_image)


        #frame set up
        self.quiz_frame = Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label = Label(self.quiz_frame, text="Coding quiz", font=("Tw Cen MT","18","bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20) 
     
        #label image
        self.image_label= Label(self.quiz_frame, image=self.comp_image)
        #self.image_label.grid(row=0, column=1) #on left side
        self.image_label.grid(row=1)
        #label for username
        self.user_label=Label(self.quiz_frame, text="Please enter your username below: ", font=("Tw Cen MT","16"),bg=background_color)
        self.user_label.grid(row=2, padx=20, pady=20) 
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=3,padx=20, pady=20)
        
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="orange", command=self.name_collection)
        self.continue_button.grid(row=4,  padx=20, pady=20)        
        


    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning
        self.quiz_frame.destroy()
        Questions(root)
       
class Questions:
      def __init__(self, parent):
        background_color="orange"# to set it as background color for all the label widget

        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        self.quiz_frame.grid()
        #Question Label
        self.question_label = Label(self.quiz_frame, text= questions_bank[1][0], font=("Tw Cen MT","18","bold"),bg=background_color)
        self.question_label.grid(row=0, padx=20) 

        #varible to store value of choice
        self.var1=IntVar()
        #Radio button 1 for first answer
        self.radio_buton1 = Radiobutton (self.quiz_frame, text= questions_bank[1][1], variable=self.var1, value=1 )
        self.radio_buton1.grid(row=1)
        #Radio button 2 for first answer
        self.radio_buton2 = Radiobutton (self.quiz_frame, text= questions_bank[1][2], variable=self.var1, value=2 )
        self.radio_buton2.grid(row=2)
        #Radio button 3 for first answer
        self.radio_buton3 = Radiobutton (self.quiz_frame, text= questions_bank[1][3], variable=self.var1, value=3 )
        self.radio_buton3.grid(row=3)
        #Radio button 4 for first answer
        self.radio_buton4 = Radiobutton (self.quiz_frame, text= questions_bank[1][4], variable=self.var1, value=4 )
        self.radio_buton4.grid(row=4)

        self.score_label = Label(self.quiz_frame, text="score")
        self.score_label.grid(row=5)

        self.submit = Button ( self.quiz_frame, text="submit", font=("Helvetica", "13", "bold"), bg="orange", command=self.test_progress)
        self.submit.grid(row=6,  padx=20, pady=20) 

      def question_setup(self):
        global qnum
        self.var1.set(0)
        self.question_label.config(text=questions_bank[qnum][0])
        self.radio_buton1.config(text=questions_bank[qnum][1])
        self.radio_buton2.config(text=questions_bank[qnum][2])
        self.radio_buton3.config(text=questions_bank[qnum][3])
        self.radio_buton4.config(text=questions_bank[qnum][4])


      def test_progress(self):
            global score, qnum #this score needs to be accissible to all the questions
            scr_label=self.score_label
            choice = self.var1.get() 
            if choice == 0:
              self.submit.config(text="Try Again, You didn't select an option")
            else:
              if choice == questions_bank[qnum][5]:#checking that the ky has the 
                score+=1
                scr_label.configure(text=score)
                self.submit.config(text="Confirm")
                scr_label.configure(text=score)
                #self.endscreen()
              else:
                self.submit.config(text="Confirm")
              qnum += 1         
              if qnum==  len(questions_bank):
                exit()   
              self.question_setup()
              



      
if __name__ == "__main__":
    root = Tk()
    root.title("Coding quiz") 
    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear


