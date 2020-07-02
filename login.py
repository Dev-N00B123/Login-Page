#! usr/bin/python3

from tkinter import *
import os

def usr():
	username_info = username.get()
	password_info = password.get()

	f=open(username_info, 'w')
	f.write(username_info+'\n')
	f.write(password_info)
	f.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(screen1, text = 'Sign-up complete', fg = 'green', font = ('Calibri', 11)).pack()

def sign_up():
	global screen1
	screen1 = Toplevel(screen)
	screen1.title('Sign-up page')
	screen1.geometry('300x250')
	global username
	global password
	global username_entry
	global password_entry
	username = StringVar() 
	password = StringVar()

	Label(screen1, text = 'Please enter details below').pack()
	Label(screen1, text = '').pack()

	Label(screen1, text = 'Username * ').pack()
	username_entry = Entry(screen1, textvariable = username)
	username_entry.pack()
	Label(screen1, text = 'Password * ').pack()
	password_entry = Entry(screen1, textvariable = password)
	password_entry.pack()
	Label(screen1, text = '').pack()
	Button(screen1, text = 'sign_up', width = 10, height = 1, command = usr).pack()

def login_true():
	screen3 = Toplevel(screen2)
	screen3.title('success')
	screen3.geometry('300x250')
	Label(screen3, text = 'Login was a success', fg = 'green', font = ("Calibri", 15)).pack()

def pass_false():
	screen4 = Toplevel(screen2)
	screen4.title('password not found')
	screen4.geometry('300x250')
	Label(screen4, text = 'password not found', fg = 'red', font = ("Calibri", 15)).pack()

def usr_false():
	screen5 = Toplevel(screen2)
	screen5.title('user not found')
	screen5.geometry('300x250')
	Label(screen5, text = 'User not found', fg = 'red', font = ("Calibri", 15)).pack()

def login_verify():
	usr1 = usr_verify.get()
	passwd1 = pass_verify.get()

	username1.delete(0, END)
	pass1.delete(0, END)

	files = os.listdir()
	if usr1 in files:
		file1 = open(usr1, 'r')
		verify  = file1.read().splitlines()
		if passwd1 in verify:
			login_true()
		else:
			pass_false()
	else:
		usr_false()

def Login():
	global screen2
	screen2 = Toplevel(screen)
	screen2.title('login')
	screen2.geometry('300x250')
	Label(screen2, text = 'Please enter details below to login').pack()
	Label(screen2, text = '').pack()
	global username1
	global pass1
	global usr_verify
	global pass_verify

	usr_verify = StringVar()
	pass_verify = StringVar()
	Label(screen2, text = 'Username * ').pack()
	username1 = Entry(screen2, textvariable = usr_verify)
	username1.pack()
	Label(screen2, text = '').pack()
	Label(screen2, text = 'Password * ').pack()
	pass1 = Entry(screen2, textvariable = pass_verify)
	pass1.pack()
	Label(screen2, text = '').pack()
	Button(screen2, text = 'Login', width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry('300x250')
    screen.title('main page')
    Label(text = 'Main Page', bg = 'grey', width = '300', height = '2', font = ('Calibri', 13)).pack()
    Button(text = 'Login', height = '2', width = '13', command = Login).pack()
    Label(text = '').pack()
    Button(text = 'Sign-Up', height = '2', width = '13', command = sign_up).pack()

    screen.mainloop()

main_screen()