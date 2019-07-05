from tkinter import *
from tkinter import filedialog
import cv2
import pytesseract
from PIL import Image

root = Tk()
root.geometry("720x420")

root.title('Optical Character Recognization')
root.config(bg = '#ff2300' )
def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hp\AppData\Local\Tesseract-OCR\tesseract.exe"
    path = filedialog.askopenfilename()
    image = cv2.imread(path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    
    filename = "{}.png".format("temp")
    B.destroy()
    cv2.imwrite(filename, gray)
    text1 = pytesseract.image_to_string(Image.open(filename))
    print(text1)
    file = open("text.txt","w")
    file.write(text1)
    file.close()
    S = Scrollbar(root)
    T = Text(root,width=420)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=LEFT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    T.insert(END, text1)  

try:
    B = Button(root, text = "Select", command=main,width = 20, height = 2,font =('Verdana',10,'bold'),border=5
            )
    B.pack(padx = 30, pady=60 )

except Exception as e:
    print(e.args) 
    print(e.__cause__)

