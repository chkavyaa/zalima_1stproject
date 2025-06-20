import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import re
from PyPDF2 import PdfReader
import pandas as pd


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    return text


def extract_key_value_pairs(text):
    pairs = {}
    lines = [line.strip() for line in text.split("\n") if ":" in line]

    for line in lines:
        if re.match(r".+?:\s?.+", line):
            key, value = line.split(":", 1)
            key_clean = re.sub(r"[^A-Za-z0-9 ]+", "", key).strip()
            value_clean = value.strip()
            if key_clean:
                pairs[key_clean] = value_clean

    return pairs


class PDFInvoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📄 PDF Invoice Viewer")

        # Upload Button
        tk.Button(root, text="📂 Upload PDF", command=self.upload_pdf).pack(pady=10)

        # Treeview for displaying extracted data
        self.tree = ttk.Treeview(root)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def upload_pdf(self):
        file_path = filedialog.askopenfilename(
            title="Select PDF File",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not file_path:
            return

        try:
            text = extract_text_from_pdf(file_path)
            kv_pairs = extract_key_value_pairs(text)

            if not kv_pairs:
                messagebox.showwarning("⚠️ No Data", "No valid key-value pairs found.")
                return

            # Display in Treeview
            self.display_data(kv_pairs)

        except Exception as e:
            messagebox.showerror("❌ Error", str(e))

    def display_data(self, data):
        # Clear previous content
        for col in self.tree["columns"]:
            self.tree.heading(col, text="")
        self.tree.delete(*self.tree.get_children())

        # Set new columns and values
        self.tree["columns"] = list(data.keys())
        self.tree["show"] = "headings"

        for col in data.keys():
            self.tree.heading(col, text=col)

        self.tree.insert("", "end", values=list(data.values()))


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("900x300")
    app = PDFInvoiceApp(root)
    root.mainloop()