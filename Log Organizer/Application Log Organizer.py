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
    c = ["Timestamp", "Level", "Event", "Actor", "Message"]
    try:
        f = open(path).read().splitlines()
    except:
        popup("Unable to read file. This program can only accept .org or .txt files.")
        sys.exit()
    df = pd.DataFrame(columns=c)
    for line in f:
        line = line.split()
        Timestamp = ' '.join(line[:2])
        Level = line[2]
        Event = line[3]
        Actor = line[4]
        Message = ' '.join(line[4:])
        df.loc[len(df)] = [Timestamp,Level,Event,Actor,Message]
    print(time.time()-x)
    return df

def to_csv(data_frame):
    try:
        data_frame.to_csv(r"C:\Users\SHU\Downloads\organized_log_printout_application.csv")
    except:
        popup("Please select a file.")
        sys.exit()

def popup(text: str):
    messagebox.showinfo("Error", text)

to_csv(open_file_dialog())
