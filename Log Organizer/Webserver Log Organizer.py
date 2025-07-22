import pandas as pd
import time
import tkinter as tk
import sys
from tkinter import filedialog
from tkinter import messagebox

def open_file_dialog():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select a file",
    )
    if file_path:
        print(f"Selected file: {file_path}")
        return organize_log(file_path)

def organize_log(path):
    x = time.time()
    c = ["IP Address", "Domain", "Timestamp", "Timezone", "Method Path Protocol", "Status", "Size", "Referrer"]
    try:
        df = pd.read_csv(path, sep = " ",usecols=[0,1,3,4,5,6,7,8], names = c, header = None)
        df[['Method', 'Path', 'Protocol']] = df['Method Path Protocol'].str.split(expand=True)

    except:
        popup("Unable to read file. This program can only accept .org or .txt files.")
        sys.exit()   
    df['Timestamp'] = df['Timestamp'] + df['Timezone']
    df.drop('Timezone', axis=1, inplace=True) 
    df = df[["IP Address", "Domain", "Timestamp", "Method", "Path", "Protocol", "Status", "Size", "Referrer"]]
    print(time.time()-x)
    return df

def to_csv(data_frame):
    try:
        data_frame.to_csv(r"C:\Users\SHU\Downloads\organized_log_printout_webserver.csv")
    except:
        popup("Please select a file.")
        sys.exit()

def popup(text: str):
    messagebox.showinfo("Error", text)

to_csv(open_file_dialog())
