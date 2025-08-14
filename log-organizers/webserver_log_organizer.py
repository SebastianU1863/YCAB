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

def organize_log(log_path):
    start_time = time.time()
    header = ["IP Address", "Domain", "Timestamp", "Timezone", "Method Path Protocol", "Status", "Size", "Referrer"]
    try:
        data_frame = pd.read_csv(log_path, sep = " ",usecols=[0,1,3,4,5,6,7,8], names = header, header = None)
        data_frame[['Method', 'Path', 'Protocol']] = data_frame['Method Path Protocol'].str.split(expand=True)

    except:
        popup("Unable to read file. This program can only accept .org or .txt files.")
        sys.exit()   
    data_frame['Timestamp'] = data_frame['Timestamp'] + data_frame['Timezone']
    data_frame.drop('Timezone', axis=1, inplace=True) 
    data_frame = data_frame[["IP Address", "Domain", "Timestamp", "Method", "Path", "Protocol", "Status", "Size", "Referrer"]]
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

output_file = "organized_log_printout_webserver.csv"
to_csv(open_file_dialog(), output_file)
