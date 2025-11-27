#
#python multi encoder by tree43 and chatgpt lol
ver = " v1.1.2"
#

import tkinter as tk
from tkinter import scrolledtext
import base64
import time
import traceback

# -------------------------
# Encode / Decode logic
# -------------------------
def encode(text_to_encode):
    output = []
    output.append("----------------")
    output.append("Original text:")
    output.append(text_to_encode)
    output.append("----------------")

    start_time = time.time()

    # Base32
    try:
        encoded_base32 = base64.b32encode(text_to_encode.encode()).decode()
        output.append(f"Base32: {encoded_base32}")
    except Exception as e:
        output.append(f"Base32: ERROR ({e})")

    # Binary
    binary_values = " ".join(format(ord(c), "08b") for c in text_to_encode)
    output.append(f"Binary: {binary_values}")

    # ASCII
    ascii_values = [ord(c) for c in text_to_encode]
    output.append(f"ASCII values: {ascii_values}")

    # Base64
    try:
        encoded_base64 = base64.b64encode(text_to_encode.encode()).decode()
        output.append(f"Base64: {encoded_base64}")
    except Exception as e:
        output.append(f"Base64: ERROR ({e})")

    # Morse
    MORSE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.', ' ': '/'
    }
    morse = " ".join(MORSE.get(c.upper(), "?") for c in text_to_encode)
    output.append(f"Morse: {morse}")

    # Hex
    hex_output = text_to_encode.encode().hex()
    output.append(f"Hex: {hex_output}")

    elapsed = time.time() - start_time
    output.append("----------------")
    output.append(f"Took {elapsed:.8f} seconds")
    output.append("----------------")
    return "\n".join(output)

def decode(text_to_decode):
    output = []
    output.append("----------------")
    output.append("Decode input:")
    output.append(text_to_decode)
    output.append("----------------")

    # Base64
    try:
        decoded = base64.b64decode(text_to_decode.encode()).decode("utf-8")
        output.append(f"Base64 decoded: {decoded}")
    except Exception:
        output.append("Base64: ERROR")

    # Base32
    try:
        decoded32 = base64.b32decode(text_to_decode.encode()).decode("utf-8")
        output.append(f"Base32 decoded: {decoded32}")
    except Exception:
        output.append("Base32: ERROR")

    output.append("----------------")
    return "\n".join(output)

# -------------------------
# GUI
# -------------------------
mode = "encode"  # default

def toggle_mode():
    global mode
    mode = "decode" if mode == "encode" else "encode"
    mode_btn.config(text=f"Mode: {mode.capitalize()}")

def run_action(event=None):
    """
    Called by Run button and Enter key. Wrapped with try/except so exceptions
    are shown inside the terminal widget.
    """
    try:
        
        

        text = entry.get().strip()
        if not text:
            terminal.insert(tk.END, "No text entered. Type something in the entry.\n\n")
            terminal.see(tk.END)
            return

        if mode == "encode":
            out = encode(text)
        else:
            out = decode(text)

        terminal.insert(tk.END, out + "\n\n")
        terminal.see(tk.END)
        entry.delete(0, tk.END)

    except Exception:
        # print traceback into terminal so you can see errors
        terminal.insert(tk.END, "ERROR in run_action:\n")
        terminal.insert(tk.END, traceback.format_exc() + "\n")
        terminal.see(tk.END)

# Build window
root = tk.Tk()
root.title(f"python multi decoder/encoder{ver}")
root.geometry("900x480")
root.resizable(False,False)
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Left panel for buttons
left_frame = tk.Frame(main_frame, width=220, bg="#2b2b2b")
left_frame.pack(side="left", fill="y")
lable = tk.Label(left_frame,text="Enter text here",font=("Consolas", 12),bg="#2b2b2b",fg="lime",)
lable.place(x=10,y=420)

# Ensure left_frame keeps visible width
left_frame.pack_propagate(False)

# Buttons
mode_btn = tk.Button(left_frame, text="Mode: Encode", command=toggle_mode, font=("Consolas", 12),fg=("lime"),bg="grey")
mode_btn.pack(padx=12, pady=(20,10), fill="x")

run_btn = tk.Button(left_frame, text="Run", command=run_action, font=("Consolas", 12),fg=("lime"),bg="grey")
run_btn.pack(padx=12, pady=10, fill="x")

# Optional Clear button (handy)
def clear_terminal():
    terminal.delete("1.0", tk.END)
clear_btn = tk.Button(left_frame, text="Clear", command=clear_terminal, font=("Consolas", 12),fg=("lime"),bg="grey")
clear_btn.pack(padx=12, pady=10, fill="x")

# Right panel (terminal)
right_frame = tk.Frame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

terminal = scrolledtext.ScrolledText(
    right_frame, wrap=tk.WORD, font=("Consolas", 11),
    bg="black", fg="lime", insertbackground="white"
)
terminal.pack(fill="both", expand=True)

# Entry located at bottom-left area: put in root but aligned to bottom and full width
entry = tk.Entry(root, font=("Consolas", 12),bg="grey",fg="lime")
entry.pack(fill="x", side="bottom")
entry.focus_set()

# Bind Enter to run_action
entry.bind("<Return>", run_action)

# initial message
terminal.insert(tk.END, "Type text below and press RUN (or Enter).\nToggle Mode on the left.\n\n")
terminal.see(tk.END)

root.mainloop()
