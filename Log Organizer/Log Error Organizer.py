import tkinter as tk
import sys
from tkinter import filedialog
from tkinter import messagebox
import re
import csv
import sys

def open_file_dialog():
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select a file",
    )
    if file_path:
        print(f"Selected file: {file_path}")
        return parse_laravel_log(file_path)

def popup(text: str):
    messagebox.showinfo("Error", text)

def parse_laravel_log(log_path):

    with open(log_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    entries = []
    current_block = []

    for line in lines:
        if line.startswith('[') and 'production.ERROR:' in line:
            if current_block:
                entries.append(''.join(current_block))
                current_block = []
        current_block.append(line)

    if current_block:
        entries.append(''.join(current_block))

    parsed_rows = []

    for block in entries:
        try:
            timestamp = re.search(r'\[(.*?)\]', block)
            message = re.search(r'production\.ERROR:\s+(.*?)\s+{', block)
            exception = re.search(r'\[object\]\s+\((\w+Exception)', block)
            code = re.search(r'\(code: ([^):]+)\):', block)
            file_line = re.search(r' at ([^:\s]+):(\d+)', block)

            parsed_rows.append({
                "timestamp": timestamp.group(1) if timestamp else "",
                "reason": exception.group(1) if exception else "UnknownException",
                "message": message.group(1).strip() if message else "",
                "code": code.group(1) if code else "0",
                "file": file_line.group(1) if file_line else "Unknown",
                "line": file_line.group(2) if file_line else "0"
            })
        except Exception:
            continue  

    return parsed_rows

def to_csv(parsed_rows):
    try:
        with open(r"C:\Users\SHU\Downloads\organized_log_printout_errors.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["timestamp", "reason", "message", "code", "file", "line"])
            writer.writeheader()
            writer.writerows(parsed_rows)
    except:
        popup("Please select a file.")
        sys.exit()

to_csv(open_file_dialog())