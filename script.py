import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os.path

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn_open_image = tk.Button(self)
        self.btn_open_image["text"] = "Open Image"
        self.btn_open_image["command"] = self.open_image
        self.btn_open_image.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="black",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def white_to_transparency_gradient(self, img):
        x = np.asarray(img.convert('RGBA')).copy()

        x[:, :, 3] = (255 - x[:, :, :3].mean(axis=2)).astype(np.uint8)

        return Image.fromarray(x)

    def open_image(self):
        sourceFilepath = filedialog.askopenfilename(parent=root)  
        sourcePath, sourceFile = os.path.split(sourceFilepath)
        sourceFilename, sourceExt = os.path.splitext(sourceFile)
        outputFile = sourceFilename + "_transparent" + sourceExt
        outputFilepath = os.path.join(sourcePath, outputFile)
        img = Image.open(sourceFilepath)
        self.white_to_transparency_gradient(img).save(outputFilepath)
        print("Successfully converted " + outputFilepath)
        



root = tk.Tk()
app = Application(master=root)
app.mainloop()