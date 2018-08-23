from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename

bcrypt = Tk()
bcrypt.resizable(width=FALSE, height=FALSE)
bcrypt.wm_title("Bcrypt")
filepath1 = Label(bcrypt, text="Click Encrypt or Decrypt and then select a file")
filepath1.grid( column = 0, row = 0)



def encrypt():
    filepath = askopenfilename()
    if filepath == "":
        tkMessageBox.showinfo( "Bcrypt", "Please Input File Name")
    else:
        f = open(filepath)
        enter = ""
        for line in f:
            enter = enter + line
        f.close()
        if enter == "":
            tkMessageBox.showinfo( "Bcrypt", "File is empty!")
        else:
            enter = enter.lower()
            length = len(enter)
            x = 0
            code = ""
            while (x < length):
                first = enter[x]
                if first == "a":
                    code = code + "bac"
                elif first == "b":
                    code = code + "cad"
                elif first == "c":
                    code = code + "cdb"
                elif first == "d":
                    code = code + "aaa"
                elif first == "e":
                    code = code + "ccc"
                elif first == "f":
                    code = code + "ddd"
                elif first == "g":
                    code = code + "bbb"
                elif first == "h":
                    code = code + "bba"
                elif first == "i":
                    code = code + "baa"
                elif first == "j":
                    code = code + "bdd"
                elif first == "k":
                    code = code + "ccd"
                elif first == "l":
                    code = code + "cbd"
                elif first == "m":
                    code = code + "dbc"
                elif first == "n":
                    code = code + "adc"
                elif first == "o":
                    code = code + "abc"
                elif first == "p":
                    code = code + "ddb"
                elif first == "q":
                    code = code + "acc"
                elif first == "r":
                    code = code + "cca"
                elif first == "s":
                    code = code + "dda"
                elif first == "t":
                    code = code + "ddc"
                elif first == "u":
                    code = code + "bbc"
                elif first == "v":
                    code = code + "bad"
                elif first == "w":
                    code = code + "dab"
                elif first == "x":
                    code = code + "aad"
                elif first == "y":
                    code = code + "aac"
                elif first == "z":
                    code = code + "cbb"
                elif first == " ":
                    code = code + "ada" 
                elif first == "1":
                    code = code + "bda" 
                elif first == "2":
                    code = code + "ccb" 
                elif first == "3":
                    code = code + "dcb" 
                elif first == "4":
                    code = code + "dad"
                elif first == "5":
                    code = code + "aab"
                elif first == "6":
                    code = code + "bbd"
                elif first == "7":
                    code = code + "daa"
                elif first == "8":
                    code = code + "dac"            
                elif first == "9":
                    code = code + "dba"
                elif first == "10":
                    code = code + "dca"   
                elif first == "\n":
                    code = code + "dcc"
                x = x + 1
            f = open(filepath, "w")
            f.writelines(code)
            f.close()
            import os
            base = os.path.splitext(filepath)[0]
            os.rename(filepath, base + ".bcrypt")
            tkMessageBox.showinfo( "Bcrypt", "Successfully encrypted %s" %  filepath)

def decrypt():
    filepath = askopenfilename()
    if filepath == "":
        tkMessageBox.showinfo( "Bcrypt", "Please Input File Name")
    else:
        f = open(filepath)
        enter = ""
        for line in f:
            enter = enter + line
        f.close()
        if enter == "":
            tkMessageBox.showinfo( "Bcrypt", "File is empty!")
        else:
            length = len(enter)
            x = 0
            code = ""
            while (x < length):
                b = x + 3
                first = enter[x:b]
                if first == "bac":
                    code = code + "a"
                elif first == "cad":
                    code = code + "b"
                elif first == "cdb":
                    code = code + "c"
                elif first == "aaa":
                    code = code + "d"
                elif first == "ccc":
                    code = code + "e"
                elif first == "ddd":
                    code = code + "f"
                elif first == "bbb":
                    code = code + "g"
                elif first == "bba":
                    code = code + "h"
                elif first == "baa":
                    code = code + "i"
                elif first == "bdd":
                    code = code + "j"
                elif first == "ccd":
                    code = code + "k"
                elif first == "cbd":
                    code = code + "l"
                elif first == "dbc":
                    code = code + "m"
                elif first == "adc":
                    code = code + "n"
                elif first == "abc":
                    code = code + "o"
                elif first == "ddb":
                    code = code + "p"
                elif first == "acc":
                    code = code + "q"
                elif first == "cca":
                    code = code + "r"
                elif first == "dda":
                    code = code + "s"
                elif first == "ddc":
                    code = code + "t"
                elif first == "bbc":
                    code = code + "u"
                elif first == "bad":
                    code = code + "v"
                elif first == "dab":
                    code = code + "w"
                elif first == "aad":
                    code = code + "x"
                elif first == "aac":
                    code = code + "y"
                elif first == "cbb":
                    code = code + "z"
                elif first == "ada":
                    code = code + " " 
                elif first == "bda":
                    code = code + "1" 
                elif first == "ccb":
                    code = code + "2" 
                elif first == "dcb":
                    code = code + "3" 
                elif first == "dad":
                    code = code + "4"
                elif first == "aab":
                    code = code + "5"
                elif first == "bbd":
                    code = code + "6"
                elif first == "daa":
                    code = code + "7"
                elif first == "dac":
                    code = code + "8"            
                elif first == "dba":
                    code = code + "9"
                elif first == "dca":
                    code = code + "10"  
                elif first == "dcc":
                    code = code + "\n"                    
                x = x + 3
            f = open(filepath, "w")
            f.writelines(code)
            f.close()
            import os
            base = os.path.splitext(filepath)[0]
            os.rename(filepath, base + ".txt")
            tkMessageBox.showinfo( "Bcrypt", "Successfully decrypted %s" %  filepath)

password1 = Label(bcrypt, text = "Password:")
password1.grid( column = 0, row = 1, columnspan = 3)            
password = Entry(bcrypt)
password.grid( column = 0, row = 2, columnspan = 3)
encrypt = Button(bcrypt, text ="Encrypt", command = encrypt)
encrypt.grid( column = 0, row = 3, columnspan = 3)
decrypt = Button(bcrypt, text ="Decrypt", command = decrypt)
decrypt.grid( column = 0, row = 4)








bcrypt.mainloop()