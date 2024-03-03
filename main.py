import PyPDF2
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

def select_files():
    file_paths = filedialog.askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])
    files_listbox.delete(0, tk.END)  # Clear previous entries
    for file_path in file_paths:
        files_listbox.insert(tk.END, file_path)

def merge_files():
    merged_pdf = PyPDF2.PdfFileMerger()
    for file_path in files_listbox.get(0, tk.END):
        merged_pdf.append(file_path)

    desktop_path = str(Path.home() / "Desktop")
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf",filetypes=[("PDF files", "*.pdf")],initialdir=desktop_path,title="Save Merged PDF As")

    if output_path:
        with open(output_path, "wb") as output_file:
            merged_pdf.write(output_file)

        tk.messagebox.showinfo("Success", "PDF files merged successfully!")

# GUI Setup
root = tk.Tk()
root.title("PDF Merger")

select_button = tk.Button(root, text="Select Files", command=select_files)
select_button.pack(pady=10)

files_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, width=50, height=10)
files_listbox.pack()

merge_button = tk.Button(root, text="Merge Files", command=merge_files)
merge_button.pack(pady=10)

root.mainloop()
