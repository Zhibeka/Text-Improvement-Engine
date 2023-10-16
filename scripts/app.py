import tkinter as tk
from tkinter import filedialog
import tkinterdnd2 as tkdnd
import pandas as pd
import text_analyzer


def open_standardized_phrases():
    file_path = filedialog.askopenfilename(filetypes=[('CSV/Text Files', '*.csv;*.txt')])
    if file_path:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
            phrases = df.values.flatten().tolist()
        else:
            with open(file_path, 'r') as file:
                phrases = file.read().splitlines()
        phrases_input.delete(1.0, tk.END)
        phrases_input.insert(tk.END, '\n'.join(phrases))

def drop_phrases(event):
    file_path = event.data
    if file_path.endswith(('.csv', '.txt')):
        open_file(file_path, phrases_input)

def open_text():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        with open(file_path, 'r') as file:
            text = file.read()
            text_input.delete(1.0, tk.END)
            text_input.insert(tk.END, text)

def drop_text(event):
    file_path = event.data
    if file_path.endswith('.txt'):
        open_file(file_path, text_input)

def open_file(file_path, widget):
    with open(file_path, 'r') as file:
        content = file.read()
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, content)

def find_similar_phrases():
    text = text_input.get(1.0, tk.END).strip()
    phrases = phrases_input.get(1.0, tk.END).strip().split('\n')
    similar_words = text_analyzer.phrase_finder(text, phrases)
    result_str = '\n'.join(f'{item[0]}: {item[1]}' for item in similar_words)
    result_input.delete(1.0, tk.END)
    result_input.insert(tk.END, result_str)

window = tkdnd.TkinterDnD.Tk()
window.title('Text Improvement Engine')

# Configure the rows with text widgets to have a weight of 1
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(5, weight=1)

# Configure the column to have a weight of 1
window.grid_columnconfigure(0, weight=1)

phrases_input = tk.Text(window, width=40, height=10)
phrases_input.grid(row=0, column=0, sticky='nsew')

phrases_button = tk.Button(window, text='Open Standardized Phrases', command=open_standardized_phrases)
phrases_button.grid(row=1, column=0, sticky='ew')

text_input = tk.Text(window, width=40, height=10)
text_input.grid(row=2, column=0, sticky='nsew')

text_button = tk.Button(window, text='Open Text', command=open_text)
text_button.grid(row=3, column=0, sticky='ew')

find_button = tk.Button(window, text='Find Similar Phrases', command=find_similar_phrases)
find_button.grid(row=4, column=0, sticky='ew')

result_input = tk.Text(window, width=40, height=10)
result_input.grid(row=5, column=0, sticky='nsew')

phrases_input.drop_target_register(tkdnd.DND_FILES)
phrases_input.dnd_bind('<<Drop>>', drop_phrases)

text_input.drop_target_register(tkdnd.DND_FILES)
text_input.dnd_bind('<<Drop>>', drop_text)

window.mainloop()