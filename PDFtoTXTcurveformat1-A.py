# 1, Download visual studio code at https://code.visualstudio.com/  and then insall
# 2, Install extension  python whose authon is microsoft
# 3, Download python at https://www.python.org/downloads/ Python 3.8.1 and then install
# 4, test if python is install sucessfully by typing python3 -m tkinter, you will see a small windows if installed sucessfully
# 5, install pillow      by typing        pip3 install pillow
# 6, install pytesseract by typing        pip3 install pytesseract 
# 7, install tesseract   by typing        brew install tesseract
# 8, if has not install brew, install it by typing 
#/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# image to string 
import pytesseract

# Tkinter is Python's de-facto standard GUI (Graphical User Interface) Package
# It is a thin object-oriented layer on top of Tcl/Tk. 
import tkinter as tk
import os

# Regular expression 
import re
from tkinter import messagebox
#PIL Python image libarary 
from PIL import ImageTk, ImageGrab, Image

dirDict = {'left': 'L', 'right': 'R','north': 'N', 'south': 'S', 'west': 'W', 'east': 'E'}
mainWindow = tk.Tk()
# mainWindow.geometry('500x500')

imageLabel = tk.Label(mainWindow, width = 50, height = 50)  # , width=82
imageLabel.grid(row=0, column=0, sticky='nsew')

textOcr = tk.Text(mainWindow)
textOcr.grid(row=0, column=1, sticky="nsew")

textResult = tk.Text(mainWindow)
textResult.grid(row=0, column=2, sticky="nsew")


# searchcurve function is for curve 

def searchcurve(text, regex, description, resultdict):
    # declared a variable, store the result later
    result = ""
    
    for matches in re.finditer(regex, text, re.IGNORECASE):
        
        # convert current match to dictionary 
        gd = matches.groupdict() 
        
        #messagebox.showinfo(message = str(gd))

        if matches.group('radius') is None :
            messagebox.showinfo(message = 'radius is none')

        radiusfeet = ''
        if matches.group('radiusfeet') is None :
            messagebox.showinfo(message = 'radiusfeet is none')
        else:
            radiusfeet = matches.group('radiusfeet')

        curvedir = ''
        if matches.group("curvedir") is None:
            messagebox.showinfo(message = 'curvedir')
        else: 
            curvedir = dirDict[matches.group('curvedir').lower()]

        dir1 = ''
        # it will show a messagebox from tkinter 
        if matches.group('dir1') is None :
            messagebox.showinfo(message='dir1 is none')
        else:
            #messagebox.showinfo(message =matches.group("dir1"))
            dir1 = dirDict[matches.group('dir1').lower()]
            
        degrees = ''
        if matches.group('degrees') is None :
            messagebox.showinfo(message='degrees is none')
        else:
            #messagebox.showinfo(message =matches.group("degrees"))
            degrees = matches.group('degrees')
        
        minutes = ''
        if "minutes" in gd:
            #messagebox.showinfo(message= matches.group("minutes"))
            minutes = matches.group('minutes')
            if minutes is None:
                minutes = "00"
        else:
            #messagebox.showinfo(message ="doesn't have minutes")
            minutes = "00"

        seconds = ''
        if "seconds" in gd:
            #messagebox.showinfo(message= matches.group("seconds"))
            seconds = matches.group('seconds')
            if seconds is None:
                seconds = "00"
        else:
            messagebox.showinfo(message ="doesn't have seconds")
            seconds = "00"
        
        dir2 = ''
        if matches.group('dir2') is None :
            messagebox.showinfo(message='dir2 is none')
        else:
            dir2 = dirDict[matches.group('dir2').lower()]
            #messagebox.showinfo(message = dir2)
            

        feet = ''
        if matches.group('feet') is None :
            messagebox.showinfo(message='feet is none')
        else:
            feet = matches.group('feet')
            #messagebox.showinfo(message = "feet is: " + feet)



        resultdict[matches.start()] =  "NC " + "R " + radiusfeet + " C " + feet + " C " + dir1 + degrees + "-" + minutes + "-" + seconds + dir2 + " " + curvedir + '\n'
        resultdict[-matches.start()] = matches.end()-matches.start()
        #result = result +  "NC " + "R " + radiusfeet + " C " + feet + " C " + dir1 + degrees + "-" + minutes + "-" + seconds + dir2 + " " + curvedir + '\n'
        #messagebox.showinfo(message= "result is: " + result)

    # delete to avoid duplication prints 
    
    # insert the result to the text box
    # result = description + '\n' + "*******"+ "\n"+ result+"\n"
    # textResult.insert(tk.END, result)


# search 1 function is for DD 
def search1(text, regex, description, resultdict):
    # declared a variable, store the result later
    result = ""
    # regular expression
    # The 'r' in front tells Python the expression is a raw string. 
    # search the text using regex 
    # Two ways 

    # to comment out in VS use command+? 
    # loop from the result text, using the pattern of the regex, the third independent varaible is for non-case sensititve
    # m = re.search(regex, text, re.IGNORECASE)
    # if m is None:
    #     messagebox.showinfo(message='can not find any result')
    # else:
    #     messagebox.showinfo(message='find result')

 
    for matches in re.finditer(regex, text, re.IGNORECASE):
        
        # convert current match to dictionary 
        gd = matches.groupdict() 
        isduplicated = False
        for pos, text in resultdict.items(): 
            if pos > 0 and -pos in resultdict.keys(): 
                if matches.start() >=  pos and matches.end() <= pos + resultdict[-pos]:
                    isduplicated = True 
                

        if isduplicated:
            continue  
        #messagebox.showinfo(message = str(gd))

        dir1 = ''
        # it will show a messagebox from tkinter 
        if matches.group('dir1') is None :
            messagebox.showinfo(message='dir1 is none')
        else:
            #messagebox.showinfo(message =matches.group("dir1"))
            dir1 = dirDict[matches.group('dir1').lower()]
            
        degrees = ''
        if matches.group('degrees') is None :
            messagebox.showinfo(message='degrees is none')
        else:
            #messagebox.showinfo(message =matches.group("degrees"))
            degrees = matches.group('degrees')
  
        # minutes = ''
        # if matches.group('minutes') is None :
        #     messagebox.showinfo(message='minutes is none')
        # else:
        #     #messagebox.showinfo(message =matches.group("minutes"))
        #     minutes = matches.group('minutes')
        # debug 
        
        minutes = ''
        if "minutes" in gd:
            #messagebox.showinfo(message= matches.group("minutes"))
            minutes = matches.group('minutes')
            if minutes is None:
                minutes = "00"
        else:
            #messagebox.showinfo(message ="doesn't have minutes")
            minutes = "00"

        seconds = ''
        if "seconds" in gd:
            #messagebox.showinfo(message= matches.group("seconds"))
            seconds = matches.group('seconds')
            if seconds is None:
                seconds = "00"
        else:
            messagebox.showinfo(message ="doesn't have seconds")
            seconds = "00"
        
        dir2 = ''
        if matches.group('dir2') is None :
            messagebox.showinfo(message='dir2 is none')
        else:
            dir2 = dirDict[matches.group('dir2').lower()]
            #messagebox.showinfo(message = dir2)
            

        feet = ''
        if matches.group('feet') is None :
            messagebox.showinfo(message='feet is none')
        else:
            feet = matches.group('feet')
            #messagebox.showinfo(message = "feet is: " + feet)

        resultdict[matches.start()] = "DD " + dir1 + degrees + "-" + minutes + "-" + seconds + dir2 + " " + feet + '\n'
        
        #result = result +  "DD " + dir1 + degrees + "-" + minutes + "-" + seconds + dir2 + " " + feet + '\n'
        #messagebox.showinfo(message= "result is: " + result)

    # delete to avoid duplication prints 
    
    # insert the result to the text box
    #result = description + '\n' + "*******"+ "\n"+ result+"\n"
    #textResult.insert(tk.END, result)

def searchall(text):
    textResult.delete(1.0, tk.END)

    resultdict = dict()

    # search curve 
    searchcurve(text, r"(?P<radius>radius)(?:.|\n)*?(?P<radiusfeet>\d+.?\d+?.?\d+?)\W+feet(?:.|\n)*?(?P<curvedir>left|right)(?:.|\n)*?(?P<dir1>South|North|West|East)\W+(?P<degrees>\d+)\W+degrees?\W+((?P<minutes>\d+)\W+minutes?\W+)?((?P<seconds>\d+)\W+seconds?\W+)?(?P<dir2>South|North|West|East)(?P<omit>(?:.|\n)*?\((?:.|\n)*?\))?(?:.|\n)*?(?P<feet>\d+.?\d+?.?\d+?)\W+feet", 
    """Curve direction: Format 1 : # it will tell you if it turns to the left or to the right """, resultdict)

    # search DD 
    search1(text, r"\W+(?P<dir1>South|North|West|East)\W+(?P<degrees>\d+)\W+degrees?\W+((?P<minutes>\d+)\W+minutes?\W+)?((?P<seconds>\d+)\W+seconds?\W+)?(?P<dir2>South|North|West|East)(?P<omit>(?:.|\n)*?\((?:.|\n)*?\))?(?:.|\n)*?(?P<feet>\d+.?\d+?.?\d+?)\W+feet", 
    "Format1-A: North/East/South/West 00 Degrees 00 Minutes 00 Seconds North/East/South/West  00.00 feet", resultdict)
    search1(text, r"\W+(?P<dir1>South|North|West|East)\W+(?P<degrees>\d+)\W+degrees?\W+((?P<minutes>\d+)\W+minutes?\W+)?((?P<seconds>\d+)\W+seconds?\W+)?(?P<dir2>South|North|West|East)(?:.|\n)*?(?P<feet>\d+.?\d+)\W+feet",
     "Format1-A does not deal with ()", resultdict)
    search1(text, r"\W+(?P<dir1>North|South|West|East)\W+(?:.|\n)*?\((?P<degrees>\d+.?\d+?)?\)\W+?degrees?(?:.|\n)*?\((?P<minutes>\d+.?\d+?)?\)\W+?minutes?((?:.|\n){1,16}\((?P<seconds>\d+.?\d+?)?\)\W+seconds)?\W+(?P<dir2>North|South|West|East)\W+(?:(?:.|\n)*?\((?P<feet>\d+.?\d+.?\d+?)?\))\W+feet",
     "Format1-B North/East/South/West (00) degrees (00)  minutes (00) seconds North/East/South/West  Two Hundred Forty-two and Twenty-three Hundredths (242.23) feet", resultdict)
    search1(text, r"\W+(?P<dir1>South|North|West|East)\W+(?P<degrees>\d+)\W+deg?\W+((?P<minutes>\d+)\W+min?\W+)?((?P<seconds>\d+)\W+sec?\W+)?(?P<dir2>South|North|West|East)(?P<omit>(?:.|\n)*?\((?:.|\n)*?\))?(?:.|\n)*?(?P<feet>\d+.?\d+)\W+feet",
     "Format1-C: North/East/South/West 00 deg 00 min 00 sec North/East/South/West", resultdict)
    search1(text, r"\W+(?P<dir1>South|North|West|East)\W+(?P<degrees>[0-9]?[0-9])\W+?(?P<minutes>[0-9]?[0-9])\W+?(?P<seconds>[0-9]?[0-9])\W+?(?P<dir2>South|North|West|East)(?:.|\n)*?(?P<feet>\d+(?:\.|\,)?\d+?(?:\.|\,)?(\d+)?).*?\W+feet",
     """Format 2 North/East/South/West 00°00’00’’ North/East/South/West""", resultdict)
    search1(text, r"\W+(?P<dir1>South|North|West|East)\W+(?P<degrees>[0-9]?[0-9])\W+?(?P<minutes>[0-9]?[0-9])\W+?(?P<seconds>[?0-9]?[?0-9])?\W+?(?P<dir2>South|North|West|East)(?:.|\n)*?(?P<feet>\d+\d+\W?\d+).*?(feet|ft)", 
     "Format 2 does not deal with ()", resultdict)
    search1(text, r"\W+(?P<dir1>S|N|W|E)\W+(?P<degrees>[0-9]?[0-9])\W+?(?P<minutes>[0-9]?[0-9])\W+?(?P<seconds>[?0-9]?[?0-9])?\W+?(?P<dir2>S|N|W|E)(?P<omit>(?:.|\n)*?\((?:.|\n)*?\))?(?:.|\n)*?(?P<feet>\d+.?\d+)\W+feet",
     """Format 3-A  N/E/S/W 00°00’00’’ N/E/S/W feet """, resultdict)
    search1(text, r"\W+(?P<dir1>S|N|W|E)\W+(?P<degrees>[0-9]?[0-9])\W+?(?P<minutes>[0-9]?[0-9])\W+?(?P<seconds>[?0-9]?[?0-9])?\W+?(?P<dir2>S|N|W|E)(?P<omit>(?:.|\n)*?\((?:.|\n)*?\))?(?:.|\n)*?(?P<feet>\d+.?\d+)\W+feet",
     """Format 3-B  N/E/S/W 00°00’00’’ N/E/S/W feet """, resultdict)
    search1(text, r"\W+(?P<dir1>South|North|West|East)\W+(?P<degrees>\d+)\W+degrees?\W(?P<minutes>[0-9]?[0-9])?\W+?(?P<seconds>[0-9]?[0-9])?\W+?(?P<dir2>South|North|West|East)(?:.|\n)*?(?P<feet>\d+.?(\d+)?\.?(\d+)?)",
     """Format 4-A North/East/South/West 00 degrees 00’00’’ North/East/South/West""", resultdict)
    search1(text, r"\W+(?P<dir1>S|N|W|E)\W+(?P<degrees>\d+)\W+degrees?\W(?P<Minutes>[0-9]?[0-9])?\W+?(?P<seconds>[0-9]?[0-9])?\W+?(?P<dir2>S|N|W|E)(?:.|\n)*?(?P<feet>\d+\W?\d+\W+\d+)",
     """Format 4-B N/E/S/W 00 degrees 00’00’’ N/E/S/W""", resultdict)
    
    newdict = sorted(resultdict.keys()) 
    for position in newdict: 
        if position >=  0:

            # result = str(position) + ": " + resultdict[position] 
            result = resultdict[position] 
            textResult.insert(tk.END, result)

def imgps():
    #try:
        temp_path = os.getcwd() + "/temp.png" # Current folder path

        im = ImageGrab.grabclipboard() # Get image from clipboard
        im.save(temp_path, format='PNG') # save image to temp folder
        
        
        loadedImage = ImageTk.PhotoImage(im) # load image from temp folder
        imageLabel.config(image=loadedImage) # set image to label
        imageLabel.image = loadedImage # save reference to image in memory
        # imageLabel.clipboard_clear() # clear clipboard

        text = pytesseract.image_to_string(Image.open(temp_path))
        
        #messagebox.showinfo(message="so far so good")
        textOcr.delete(1.0, tk.END)
        textOcr.insert(tk.END, text)

        searchall(text)
 
        # messagebox.showinfo(message=text)

        # os.remove(temp_path) # delete temp file

    #except:
        #messagebox.showinfo(message="Clipboard is Empty Or Some Exception Occured.")


def traverse_file(): # when you convert to text 
    # get the text from the text box, 
    # set the value to input value 
    # extract information from the input value 
    # https://tkdocs.com/tutorial/text.html
    inputValue = textOcr.get("1.0","end-1c")
    #messagebox.showinfo(message=inputValue)
    searchall(inputValue)

button = tk.Button(mainWindow, text="Recognize", command=imgps)
button.grid(row=1, column=0, sticky='nsew')

buttonconvert = tk.Button(mainWindow, text="Convert to Traverse", command=traverse_file)
buttonconvert.grid(row=1, column=1, sticky='nsew')

mainWindow.mainloop()