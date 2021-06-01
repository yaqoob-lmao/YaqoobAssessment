from tkinter import *
from PIL import ImageTk, Image



class Quiz:
    def __init__(self, parent):#constructor, The __init__() function is called automatically every time the class is being used to create a new object.
 
        background_color="orange"# to set it as background color for all the label widget

        #open image
        self.comp_image= Image.open("computer.jpg")
        self.comp_image=self.comp_image.resize((250,250), Image.ANTIALIAS)
        self.comp_image=ImageTk.PhotoImage(self.comp_image)


        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx, pady How many pixels to pad widget, horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#This geometry manager organizes widgets in a table-like structure in the parent widget.
               
        #widgets goes below
        self.heading_label=Label(self.quiz_frame, text="Coding quiz", font=("Tw Cen MT","18","bold"),bg=background_color)
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
        self.continue_button.destroy()
        self.entry_box.destroy() #Destroy name frame then open the quiz runner




      
if __name__ == "__main__":
    root = Tk()
    root.title("Coding quiz") 
    quiz_instance = Quiz(root) #instantiation, making an instance of the class Quiz
    root.mainloop()#so the frame doesnt dissapear


