#from _typeshed import WriteableBuffer
from tkinter import *
from time import sleep
import threading
from typing import ClassVar

from pandas.core.frame import DataFrame #import the library
import Web
import tkinter.font as tkFont
import numpy as np
import pandas as pd

url = "https://vnexpress.net/thu-tuong-neu-6-muc-tieu-chong-covid-19-4325397.html"
#url = 'https://vnexpress.net/chung-khoan-mat-gan-25-diem-4329462.html'

def get_text():
    return Web.GetPage(url)

text = get_text()
words = Web.GetWords(url,0,False)

import os
def save_words(words):
    print(words)
    
    #pd.read_excel('Data/Words.xlsx')
    np = []
    
    PATH = './Data/Words.xlsx'
    for word in words:
        if(len(word)>=1):
            np.append([word])        
    
    #df.reset_index(drop=True)
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        print("File exists and is readable")
        _df = pd.read_excel(PATH)
        _words = _df['Word']
        for _word in _words:
        #_df.reset_index(drop=True)
            np.append([_word])
        # #df.to_excel('Data/Words.xlsx')
        # _newDf = DataFrame(np, columns=['Word'])
        # _newDf.drop_duplicates()
        # _newDf.to_excel(PATH)
    else:
        print("Either the file is missing or not readable")
    df = DataFrame(np, columns=['Word'])
    df.to_excel(PATH)
    data = pd.read_excel('Data/Words.xlsx')
    df = data['Word']
    df = df.drop_duplicates()
    os.remove(PATH)
    df.to_excel(PATH)
#save_words(words)

def get_words(_c):
    data = pd.read_excel('Data/Words.xlsx')
    df = data['Word']
    _words = df.values
    _rs = []
    i = 0
    n = len(_words)
    if(len(_c)>=2):
        for word in _words:
            if _c in word and len(_c) < len(word):            
                _rs.append(word)                
    return _rs

#print(get_words('ao'))


root = Tk()    
fontStyle = tkFont.Font(family="Lucida Grande", size=80)

l = Label(root, text="", font=fontStyle, borderwidth=5,width=100)
#l.grid(column=10, row=10)
l.pack()

l1 = Label(root, text="", font=fontStyle, borderwidth=5,width=100)
#l1.grid(column=10, row=14)
l1.pack()

#root.geometry('350x450+700+200')
root.geometry('800x600')

def get_all_words():
    data = pd.read_excel('Data/Words.xlsx')
    df = data['Word']
    _words = df.values
    return _words

def get_words_by_length(n):
    _words = get_all_words()
    _rs = []
    for _word in _words:
        if(len(_word) == n):
           _rs.append(_word) 
    return _rs

#print(get_words_by_length(2))

    

# threading.Thread(target=call).start() #create a separate thread to not freeze the GUI
# root.mainloop()


class Lavie:
    # @classmethod
    # def update(self):
    #     _words = get_new_words()
    #     save_words(_words)
    
    time_update : float
    
    def __init__(self, seconds) -> None:
        self.time_update = seconds
    
    
    @classmethod
    def updateUI(self):
        _words = []
        for j in range(2,4):
            _x = get_words_by_length(j)
            for k in _x:
                _words.append(k)
        #get_all_words()
        i = 0
        n = len(_words)

        for _word in _words:
            i = i + 1
            l1.config(text = _word + '\n' + str(i) + ' : ' + str(n))
            sleep(10)
    
    @classmethod
    def run(self,seconds):
        threading.Thread(target=self.updateUI).start()
        root.mainloop()
    
lavie = Lavie(1)
lavie.run(0.5)
