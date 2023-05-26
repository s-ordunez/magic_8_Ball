from tkinter import *
from PIL import ImageTk, Image
import random

file_path = ###enter file path as a string here to connect images###
answers = {'1':'It is certain.', '2':'It is decidedly so.', 
'3':'Without a doubt.', '4':'Yes, Definitely', '5':'You may rely on it.',
'6':'As I see it, yes.','7': 'Most Likely.', '8':'Outlook good.',
'9':'Signs point to yes.','10':'Yes.','11':'Reply hazy, Try again.',
'12':'Ask again later.','13':'Better not tell you now',
'14':'Cannot predict now.','15':'Concentrate and ask again.',
'16':"Don't count on it.",'17':'My reply is no.',
'18':'My sources say no.','19':'Outlook not so good.','20':'Very doubtful.'}


# --- functions ---

def make_a_wish():
    ### This function allows the user to continue ###
    ### asking questions deleting the initial frame ###
    ### then recreating the frame and add an answer ###
    reset_all()

    text = answers[str(random.randint(1,20))]
    answer = Label(text=text)
    answer.place(x= 350, y=350, anchor=CENTER)

def create_frame(master):
   
    frame = Frame(master)
    
    master.geometry('700x700')
    master.title('Ask the Magic 8 Ball!')
    master.iconbitmap(file_path + '/eightball.ico')
    
    
    bg_image = Label(frame, image = magic8Ball)
    bg_image.pack()
    
    button_1 = Button(frame, text="Ask the Magic 8-Ball!",
        padx = 40, pady = 20, command = make_a_wish)
    button_1.place(x= 250, y = 575)

    return frame

def reset_all():
    global frame

    frame.destroy()
    frame = create_frame(master)
    frame.pack()

### Main ###

master = Tk()

magic8Ball = ImageTk.PhotoImage(Image.open(file_path +
                                            '/Magic8BallMain.png'))

frame = create_frame(master)
frame.pack()

mainloop()
