import sys
import time 
import tkinter as tk
import os
import builtins
def CreateSequence(a):
    for x in range(a):
        yield x ** 2
terms = CreateSequence(100)
for y in terms:
    print(y)

print()
sys._debugmallocstats()


def progtressbar(n):
    z = "me"
    sys.stdout.write("[")
    for i in range (n):
        time.sleep(0.05)
        sys.stdout.write("|")
        sys.stdout.flush()
    sys.stdout.write("]")
    sys.stdout.write(f"Thanks for playing {z} ")

print(progtressbar(30))

print(time.ctime())
print(time.time())


z = ["apple","bannana"]
del(z[0])
print(z)


# root = tk.Tk()
# Height = 400
# Width = 500
# screen = tk.Canvas(height=1000,width=1500)
# screen.pack()
# root.title("Raul|TK")
# root.configure(background="blue")
# b1 = tk.Button(screen,height=10,width=40,background="red",text="push me",padx=500,pady=750)
# b1.pack()
# loop = tk.mainloop()

with open("name.txt","a") as file:
    
    file.writelines("hello")
    file.writelines("James")
    file.close()

def displayhook(value):
    if value is None:
        return
    # Set '_' to None to avoid recursion
    builtins = None
    text = repr(value)
    try:
        sys.stdout.write(text)
    except UnicodeEncodeError:
        bytes = text.encode(sys.stdout.encoding, 'backslashreplace')
        if hasattr(sys.stdout, 'buffer'):
            sys.stdout.buffer.write(bytes)
        else:
            text = bytes.decode(sys.stdout.encoding, 'strict')
            sys.stdout.write(text)
    sys.stdout.write("\n")
    builtins = value

displayhook(progtressbar)