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
    start_time = time.time()
    header = ["Timestamp", "Level", "Event", "Actor", "Message"]
    try:
        f = open(path).read().splitlines()
    except:
        popup("Unable to read file. This program can only accept .org or .txt files.")
        sys.exit()
    data_frame = pd.DataFrame(columns=header)
    for line in f:
        line = line.split()
        Timestamp = ' '.join(line[:2])
        Level = line[2]
        Event = line[3]
        Actor = line[4]
        Message = ' '.join(line[4:])
        data_frame.loc[len(data_frame)] = [Timestamp,Level,Event,Actor,Message]
    print(time.time()-start_time)
    return data_frame

def to_csv(data_frame, output_file):
    try:
        data_frame.to_csv(output_file)
    except:
        popup("Please select a file.")
        sys.exit()

def popup(text: str):
    messagebox.showinfo("Error", text)

output_file = r"C:\Users\SHU\Downloads\organized_log_printout_application.csv"
to_csv(open_file_dialog(), output_file)
