# import tkinter as tk
# from tkinter import ttk
# import subprocess

# def compile_code():
#     code = text_area.get("1.0", tk.END)
    
#     # Save the code to a temporary file
#     with open("temp.lime", "w") as f:  # Assuming .lime is your language's extension
#         f.write(code)

#     # Run the main compiler file (update the command if needed)
#     result = subprocess.run(["python", "main.py", "temp.lime"], capture_output=True, text=True)
    
#     # Display output
#     output_area.config(state=tk.NORMAL)
#     output_area.delete("1.0", tk.END)
#     output_area.insert(tk.END, result.stdout if result.stdout else result.stderr)
#     output_area.config(state=tk.DISABLED)

# # Create main window
# root = tk.Tk()
# root.title("Custom Compiler UI")

# # Create a Notebook (Tab container)
# notebook = ttk.Notebook(root)
# notebook.pack(expand=True, fill="both")

# # --- Compiler Tab ---
# compiler_frame = ttk.Frame(notebook)
# notebook.add(compiler_frame, text="Compiler")

# text_area = tk.Text(compiler_frame, height=10)
# text_area.pack(pady=5, padx=5, fill="both", expand=True)

# run_button = tk.Button(compiler_frame, text="Run Code", command=compile_code)
# run_button.pack(pady=5)

# output_area = tk.Text(compiler_frame, height=10, state=tk.DISABLED, bg="lightgray")
# output_area.pack(pady=5, padx=5, fill="both", expand=True)

# # --- Manual Tab ---
# manual_frame = ttk.Frame(notebook)
# notebook.add(manual_frame, text="Manual")

# manual_text = tk.Label(manual_frame, text=(
#     "Welcome to the Custom Compiler!\n\n"
#     "1. Enter your code in the text editor.\n"
#     "2. Click 'Run Code' to execute using your compiler.\n"
#     "3. The output will appear below.\n\n"
#     "Supports your custom language."
# ), justify="left", padx=10, pady=10)
# manual_text.pack()

# # Run the main loop
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk, filedialog, messagebox
# import subprocess

# # Function to compile code
# def compile_code():
#     code = text_area.get("1.0", tk.END).strip()
#     if not code:
#         messagebox.showwarning("Warning", "Code editor is empty!")
#         return

#     # Save the code to a temporary file
#     with open("temp.lime", "w") as f:  # Assuming .lime is your language's extension
#         f.write(code)

#     # Run the compiler (Modify this as per your compiler setup)
#     result = subprocess.run(["python", "main.py", "temp.lime"], capture_output=True, text=True)

#     # Display output
#     output_area.config(state=tk.NORMAL)
#     output_area.delete("1.0", tk.END)
#     output_area.insert(tk.END, result.stdout if result.stdout else result.stderr)
#     output_area.config(state=tk.DISABLED)

# # Function to open a file
# def open_file():
#     file_path = filedialog.askopenfilename(filetypes=[("Lime Files", "*.lime"), ("All Files", "*.*")])
#     if file_path:
#         with open(file_path, "r") as file:
#             text_area.delete("1.0", tk.END)
#             text_area.insert(tk.END, file.read())

# # Function to save a file
# def save_file():
#     file_path = filedialog.asksaveasfilename(defaultextension=".lime", filetypes=[("Lime Files", "*.lime"), ("All Files", "*.*")])
#     if file_path:
#         with open(file_path, "w") as file:
#             file.write(text_area.get("1.0", tk.END))

# # Create main window
# root = tk.Tk()
# root.title("Custom Compiler UI")
# root.geometry("800x600")
# root.configure(bg="#2e3b4e")

# # Styling
# style = ttk.Style()
# style.theme_use("clam")
# style.configure("TNotebook.Tab", font=("Arial", 12), padding=[10, 5])
# style.configure("TButton", font=("Arial", 11), background="#4CAF50", foreground="white")

# # Create Notebook (Tab container)
# notebook = ttk.Notebook(root)
# notebook.pack(expand=True, fill="both", padx=10, pady=10)

# # --- Compiler Tab ---
# compiler_frame = ttk.Frame(notebook)
# notebook.add(compiler_frame, text="🖥 Compiler")

# # Toolbar (Open & Save)
# toolbar = ttk.Frame(compiler_frame)
# toolbar.pack(fill="x", padx=5, pady=5)

# open_btn = ttk.Button(toolbar, text="📂 Open", command=open_file)
# open_btn.pack(side="left", padx=5)

# save_btn = ttk.Button(toolbar, text="💾 Save", command=save_file)
# save_btn.pack(side="left", padx=5)

# run_button = ttk.Button(toolbar, text="▶ Run Code", command=compile_code)
# run_button.pack(side="right", padx=5)

# # Split Pane for Editor and Output
# split_pane = ttk.PanedWindow(compiler_frame, orient=tk.VERTICAL)
# split_pane.pack(expand=True, fill="both")

# # --- Code Editor with Scrollbar ---
# text_frame = ttk.Frame(split_pane)
# text_scroll = ttk.Scrollbar(text_frame, orient="vertical")
# text_area = tk.Text(text_frame, wrap="word", yscrollcommand=text_scroll.set, font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
# text_scroll.config(command=text_area.yview)

# text_scroll.pack(side="right", fill="y")
# text_area.pack(expand=True, fill="both")
# split_pane.add(text_frame, weight=3)  # Editor takes 3/4 of space

# # --- Output Area with Scrollbar ---
# output_frame = ttk.Frame(split_pane)
# output_scroll = ttk.Scrollbar(output_frame, orient="vertical")
# output_area = tk.Text(output_frame, wrap="word", yscrollcommand=output_scroll.set, font=("Consolas", 12), bg="#262626", fg="#00FF00", state=tk.DISABLED)
# output_scroll.config(command=output_area.yview)

# output_scroll.pack(side="right", fill="y")
# output_area.pack(expand=True, fill="both")
# split_pane.add(output_frame, weight=1)  # Output takes 1/4 of space

# # --- Manual Tab ---
# manual_frame = ttk.Frame(notebook)
# notebook.add(manual_frame, text="📖 Manual")

# manual_text = tk.Text(manual_frame, wrap="word", font=("Arial", 12), bg="#2e3b4e", fg="white", padx=20, pady=20)
# manual_text.insert(tk.END, """📌 Welcome to the Custom Compiler!

# 🖊 Enter your code in the text editor.
# ▶ Click 'Run Code' to execute your script using the compiler.
# 💾 Use 'Open' and 'Save' to manage your .lime files.
# 🔍 Output appears in the console below.

# 🛠 Supports your custom programming language.

# 🔹 How to Use:
# 1️⃣ Write your code in the editor.
# 2️⃣ Save your work before running (recommended).
# 3️⃣ Click ▶ Run Code to compile and execute.
# 4️⃣ View the output in the console area.
# 5️⃣ If there are errors, they will be displayed.

# 🔹 File Support:
# - Open and edit `.lime` files.
# - Save your work with `.lime` extension.
# - "define" can be written for LET,
# - "be"can be written for EQ,
# - "end"can be written for SEMICOLON,
# - "fun"can be written for FN,
# - "give"can be written for RETURN,
# - "set"can be written for ARROW,
# - "crack"can be written for BREAK,
# - "go"can be written for CONTINUE,
# - "import"can be written for IMPORT,
# - "take"can be written for IMPORT.

# Enjoy coding! 🚀""")
# manual_text.config(state=tk.DISABLED)  # Make it read-only
# manual_text.pack(expand=True, fill="both")

# # Run the main loop
# root.mainloop()



import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess
import time

# Function to compile code
def compile_code():
    code = text_area.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Warning", "Code editor is empty!")
        return

    # Save the code to a temporary file
    with open("temp.lime", "w") as f:  # Assuming .lime is your language's extension
        f.write(code)

    # Start time tracking
    start_time = time.time()

    # Run the compiler (Modify this as per your compiler setup)
    result = subprocess.run(["python", "main.py", "temp.lime"], capture_output=True, text=True)
    
    # Calculate execution time
    execution_time = time.time() - start_time
    
    # Prepare output
    output_text = result.stdout if result.stdout else result.stderr
    output_text += f"\nExecution Time: {execution_time:.4f} seconds"
    
    # Display output
    output_area.config(state=tk.NORMAL)
    output_area.delete("1.0", tk.END)
    output_area.insert(tk.END, output_text)
    output_area.config(state=tk.DISABLED)

# Function to open a file
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Lime Files", "*.lime"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete("1.0", tk.END)
            text_area.insert(tk.END, file.read())

# Function to save a file
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".lime", filetypes=[("Lime Files", "*.lime"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get("1.0", tk.END))

# Create main window
root = tk.Tk()
root.title("Custom Compiler UI")
root.geometry("800x600")
root.configure(bg="#2e3b4e")

# Styling
style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook.Tab", font=("Arial", 12), padding=[10, 5])
style.configure("TButton", font=("Arial", 11), background="#4CAF50", foreground="white")

# Create Notebook (Tab container)
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

# --- Compiler Tab ---
compiler_frame = ttk.Frame(notebook)
notebook.add(compiler_frame, text="🖥 Compiler")

# Toolbar (Open & Save)
toolbar = ttk.Frame(compiler_frame)
toolbar.pack(fill="x", padx=5, pady=5)

open_btn = ttk.Button(toolbar, text="📂 Open", command=open_file)
open_btn.pack(side="left", padx=5)

save_btn = ttk.Button(toolbar, text="💾 Save", command=save_file)
save_btn.pack(side="left", padx=5)

run_button = ttk.Button(toolbar, text="▶ Run Code", command=compile_code)
run_button.pack(side="right", padx=5)

# Split Pane for Editor and Output
split_pane = ttk.PanedWindow(compiler_frame, orient=tk.VERTICAL)
split_pane.pack(expand=True, fill="both")

# --- Code Editor with Scrollbar ---
text_frame = ttk.Frame(split_pane)
text_scroll = ttk.Scrollbar(text_frame, orient="vertical")
text_area = tk.Text(text_frame, wrap="word", yscrollcommand=text_scroll.set, font=("Consolas", 12), bg="#1e1e1e", fg="white", insertbackground="white")
text_scroll.config(command=text_area.yview)

text_scroll.pack(side="right", fill="y")
text_area.pack(expand=True, fill="both")
split_pane.add(text_frame, weight=3)  # Editor takes 3/4 of space

# --- Output Area with Scrollbar ---
output_frame = ttk.Frame(split_pane)
output_scroll = ttk.Scrollbar(output_frame, orient="vertical")
output_area = tk.Text(output_frame, wrap="word", yscrollcommand=output_scroll.set, font=("Consolas", 12), bg="#262626", fg="#00FF00", state=tk.DISABLED)
output_scroll.config(command=output_area.yview)

output_scroll.pack(side="right", fill="y")
output_area.pack(expand=True, fill="both")
split_pane.add(output_frame, weight=1)  # Output takes 1/4 of space

# --- Manual Tab ---
manual_frame = ttk.Frame(notebook)
notebook.add(manual_frame, text="📖 Manual")

manual_text = tk.Text(manual_frame, wrap="word", font=("Arial", 12), bg="#2e3b4e", fg="white", padx=20, pady=20)
manual_text.insert(tk.END, """📌 🔹 Introduction
Welcome to the Custom Compiler! This tool allows you to write, compile, and execute code written in the Lime language.

👨‍💻 Features:

🖊 Enter your code in the text editor.
▶ Click 'Run Code' to execute your script using the compiler.
💾 Use 'Open' and 'Save' to manage your .lime files.
🔍 Output appears in the console below.

🛠 Supports your custom programming language.

🔹 How to Use:
1️⃣ Write your code in the editor.
2️⃣ Save your work before running (recommended).
3️⃣ Click ▶ Run Code to compile and execute.
4️⃣ View the output in the console area.
5️⃣ If there are errors, they will be displayed.

🔹 Supported Syntax & Keywords
Keyword	        Equivalent in Other Languages
define	        Variable Declaration (let)
be	            Assignment (=)
end	            Statement Terminator (;)
fun	            Function Declaration (fn)
give	        Return Statement (return)
set	            Function Type (->)
crack	        Break (break)
go	            Continue (continue)
import	        Import Module (import)
take	        Include File (#include)
                   
🔹 Code Structure & Examples
✅ Example 1: Variable Declaration & Assignment

define a: int be 10 end
define b: float be 5.5 end
                   

✅ Example 2: Function Definition

fun add(x: int, y: int) set int {
    give x + y end
}
                   

✅ Example 3: Conditional Statements

define x: int be 10 end
if x > 5 {
    printf "X is greater than 5" end
} else {
    printf "X is less than or equal to 5" end
}
                   

✅ Example 4: Loops

define i: int be 0 end
while i < 5 {
    printf i end
    i = i + 1 end
}
                   

✅ Example 5: Importing Modules

import "math.lime" end


                   
Enjoy coding! 🚀""")
manual_text.config(state=tk.DISABLED)  # Make it read-only
manual_text.pack(expand=True, fill="both")

# Run the main loop
root.mainloop()