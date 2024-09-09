from tkinter import *
from random import choice

# List of texts for the typing test
textlist = [
    'quick brown fox jumps over the lazy dog\nthe dog saw the fox\nthe decided to become quick',
    'there was a hen that laid golden eggs\nthe owner got rich by selling those eggs\nthe owner got greedy\nhe decided to kill the hen\nhe lost the eggs '
]

seconds = 0
time_running = False 
def start_timer():
    global time_running, seconds
    
    time_running = True
    seconds = 0
    text.config(text=choice(textlist)) 
    user.delete(1.0, 'end') 
    update_clock() 

def update_clock():
    global seconds, time_running
    if time_running:
        seconds += 1
        time_label.config(text=f"Time: {seconds} seconds", fg='red', font=('Arial MTBold', 12))
        root.after(1000, update_clock)


def stop_timer():
    global seconds, time_running
    time_running = False
    
    
    user_input = user.get('1.0', 'end-1c').strip()
    words = len(user_input.split()) 
    
    # Calculate words per minute (WPM)
    if seconds > 0:
        wpm = (words * 60 / seconds)
    else:
        wpm = 0
    
    time_label.config(text=f"{int(wpm)} Words per minute", fg='blue', font=('Arial MTBold', 12))
    text.config(text='') 
    seconds = 0  

# Set up the main window
root = Tk()
root.geometry('700x500')
root.title('Typing Speed Test')  
root.configure(bg='#f7f7f7')  


title = Label(
    root, text='Typing Speed Test', fg='darkblue', bg='#f7f7f7',
    font=('Arial', 24, 'bold')
)
title.grid(row=0, column=0, columnspan=5, pady=20)


time_label = Label(root, text='Time: 0 seconds', bg='#f7f7f7', font=('Arial', 12))
time_label.grid(column=0, row=1, columnspan=5, pady=10)


text = Label(
    root, text='', wraplength=600, justify="left", bg='#fff', font=('Arial', 14),
    height=6, width=70, relief='solid', padx=10, pady=10
)
text.grid(row=2, column=0, columnspan=5, padx=10, pady=10)


user = Text(root, height=5, width=60, wrap='word', font=('Arial', 12), relief='solid')
user.grid(column=0, row=8, columnspan=5, padx=10, pady=10)


start_button = Button(
    root, text='Start', bg='#28a745', fg='white', font=('Arial', 12, 'bold'), 
    width=10, command=start_timer, relief='raised', bd=3
)
start_button.grid(row=9, column=1, pady=20)


stop_button = Button(
    root, text='Stop', bg='#dc3545', fg='white', font=('Arial', 12, 'bold'),
    width=10, command=stop_timer, relief='raised', bd=3
)
stop_button.grid(row=9, column=2, pady=20)



root.mainloop()
