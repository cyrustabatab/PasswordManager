import tkinter
import pyperclip
import json
from tkinter import messagebox
from generate_password import generate_password
from PIL import Image,ImageTk
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    if password_entry.get():
        password_entry.delete(0,tkinter.END)
    password = generate_password()
    password_entry.insert(0,password)


def find_password():
    #TODO add better website searching by ignoring possible spaces?
    website = website_entry.get()
    if not website: 
        messagebox.showerror(title="Oops",message="Please type website you want the password of!")
    else:
        website = website.upper()
        try:
            with open('data.json','r') as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror(title="Oops",message="You have not saved any passwords yet!")
        else:
            try:
                email = data[website]['email']
                password = data[website]['password']
            except KeyError:
                messagebox.showerror(title="Oops",message="No password saved for this website")
            else:
                messagebox.showinfo(title=f"Info for {website}",message=f"Email: {email}\nPassword: {password}")








    
    '''
    finally:
        website_entry.delete(0,tkinter.END)
        password_entry.delete(0,tkinter.END)
    '''













# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    new_data = {website.upper(): {'email': email,'password': password}}
    if not website or not email or not password:
        messagebox.showerror(title="Oops",message="Please do not leave any fields blank")
    
    else:

        is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json','r') as f:
                    data = json.load(f)
                    data.update(new_data)
            except FileNotFoundError:
                f = open('data.json','w')
                f.close()
                data = new_data

            with open('data.json','w') as f:
                json.dump(data,f,indent=4)
            pyperclip.copy(password)
            messagebox.showinfo(title="Success",message="Password successfully saved!")

        
        website_entry.delete(0,tkinter.END)
        password_entry.delete(0,tkinter.END)




# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

# canvas
canvas = tkinter.Canvas(width=200,height=200)
image = Image.open('logo.png')
photo = ImageTk.PhotoImage(image)
canvas.create_image(100,100,image=photo)
canvas.grid(row=0,column=1)

# label
website_label = tkinter.Label(text='Website:')
website_label.grid(row=1,column=0,sticky=tkinter.E)


# website entry
website_entry = tkinter.Entry(width=35)
website_entry.focus_set()
website_entry.grid(row=1,column=1,sticky=tkinter.W + tkinter.E,padx=5)

search_button = tkinter.Button(text='Search',command=find_password)
search_button.grid(row=1,column=2,sticky=tkinter.W + tkinter.E)


# email/username label

email_label = tkinter.Label(text='Email/Username:')
email_label.grid(row=2,column=0,pady=5)


email_entry = tkinter.Entry(width=35)
email_entry.insert(0,'ctabatab@gmail.com')
email_entry.grid(row=2,column=1,columnspan=2,sticky=tkinter.W + tkinter.E,padx=5,pady=5)


# password label
password_label = tkinter.Label(text='Password:')
password_label.grid(row=3,column=0,sticky=tkinter.E,pady=5)


#password entry
password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3,column=1,sticky=tkinter.W + tkinter.E,padx=5,pady=5)


password_button = tkinter.Button(text='Generate Password',pady=5,command=password_generate)
password_button.grid(row=3,column=2)


# add button  

add_button = tkinter.Button(text='Add',width=36,command=save_password)
add_button.grid(row=4,column=1,columnspan=2,sticky=tkinter.W,pady=5)



window.mainloop()




