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

    # Semaphore
    semaphore_out = " ".join(SEMAPHORE_ENCODE.get(c.upper(), "?") for c in text_to_encode)
    output.append(f"Semaphore: {semaphore_out}")

    # Barcode Numbers
    barcode_out = "-".join(BARCODE_NUM_ENCODE.get(c.upper(), "??") for c in text_to_encode)
    output.append(f"Barcode: {barcode_out}")

    # Clock Code
    clock_out = " ".join(CLOCK_ENCODE.get(c.upper(), "?") for c in text_to_encode)
    output.append(f"Clock: {clock_out}")

    # DTMF
    dtmf_out = " ".join(DTMF_ENCODE.get(c.upper(), "?") for c in text_to_encode)
    output.append(f"DTMF: {dtmf_out}")

    elapsed = time.time() - start_time
    output.append("----------------")
    output.append(f"Took {elapsed:.8f} seconds")
    output.append("----------------")
    return "\n".join(output)

# Semaphore: flag positions as clock directions (1=up, 2=upper-right, 3=right, 4=lower-right,
#            5=down, 6=lower-left, 7=left, 8=upper-left). Each letter = two positions e.g. "1-2"
SEMAPHORE_ENCODE = {
    'A': '1-2', 'B': '1-3', 'C': '1-4', 'D': '1-5', 'E': '1-6',
    'F': '1-7', 'G': '1-8', 'H': '2-3', 'I': '2-4', 'J': '2-6',
    'K': '2-7', 'L': '2-8', 'M': '3-4', 'N': '3-5', 'O': '3-6',
    'P': '3-7', 'Q': '3-8', 'R': '4-5', 'S': '4-6', 'T': '4-7',
    'U': '4-8', 'V': '5-6', 'W': '6-7', 'X': '6-8', 'Y': '5-7',
    'Z': '7-8',
    '1': '1-2', '2': '1-3', '3': '1-4', '4': '1-5', '5': '1-6',
    '6': '1-7', '7': '1-8', '8': '2-3', '9': '2-4', '0': '5-5',
    ' ': '/'
}
SEMAPHORE_DECODE = {v: k for k, v in SEMAPHORE_ENCODE.items() if k.isalpha() or k == ' '}
SEMAPHORE_DECODE['/'] = ' '

MORSE_DECODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '-..-.': '/', '/': ' '
}

# -------------------------
# Barcode Numbers — each letter = its alphabet position as 2-digit number (A=01 … Z=26)
# digits 0-9 stay as their value (00-09), space = 00
# tokens separated by - when encoded e.g. "HELLO" -> "08-05-12-12-15"
# -------------------------
BARCODE_NUM_ENCODE = {}
BARCODE_NUM_DECODE = {}
for _i, _ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1):
    _tok = f"{_i:02d}"
    BARCODE_NUM_ENCODE[_ch] = _tok
    BARCODE_NUM_DECODE[_tok] = _ch
for _d in range(10):
    BARCODE_NUM_ENCODE[str(_d)] = f"{_d:02d}"
    # digits decoded back only if not already claimed by a letter (01-09 clash with A-I)
    # so digits share tokens with letters; decode will prefer letters for 01-09
BARCODE_NUM_ENCODE[' '] = '00'
BARCODE_NUM_DECODE['00'] = ' '

# -------------------------
# Clock Code — hour hand points to letter (A=1o'clock … Z=26, mapped mod 12)
# Letters are shown as H:MM style clock face positions
# A-L  → 1–12 o'clock,  M-X → 1–12 o'clock (second pass, marked with *)
# We use simple numeric notation: A=1, B=2 … L=12, M=1*, N=2* … Z=12* (Z only 12 letters so Z=26→2**)
# Simplified: A-Z → 1..26, output as "H:00" where H = position, second pass gets "'"
# -------------------------
CLOCK_ENCODE = {}
CLOCK_DECODE = {}
for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1):
    hour = i if i <= 12 else i - 12
    mark = "" if i <= 12 else "'"
    token = f"{hour}{mark}"
    CLOCK_ENCODE[ch] = token
    CLOCK_DECODE[token] = ch
CLOCK_ENCODE[' '] = '|'
CLOCK_DECODE['|'] = ' '

# -------------------------
# DTMF — telephone keypad tones, digits/symbols only; letters mapped via T9
# Format: each character → tone label e.g. "1" "2" "3" … "*" "#"
# Letters use T9: A=2a B=2b C=2c D=3a … spaces = 0
# -------------------------
DTMF_ENCODE = {
    '1': '1',   '2': '2',   '3': '3',   '4': '4',   '5': '5',
    '6': '6',   '7': '7',   '8': '8',   '9': '9',   '0': '0',
    '*': '*',   '#': '#',
    'A': '2a',  'B': '2b',  'C': '2c',
    'D': '3a',  'E': '3b',  'F': '3c',
    'G': '4a',  'H': '4b',  'I': '4c',
    'J': '5a',  'K': '5b',  'L': '5c',
    'M': '6a',  'N': '6b',  'O': '6c',
    'P': '7a',  'Q': '7b',  'R': '7c',  'S': '7d',
    'T': '8a',  'U': '8b',  'V': '8c',
    'W': '9a',  'X': '9b',  'Y': '9c',  'Z': '9d',
    ' ': '0',
}
DTMF_DECODE = {v: k for k, v in DTMF_ENCODE.items() if k.isalpha() or k.isdigit() or k in ('*', '#', ' ')}

def decode(text_to_decode):
    output = []
    output.append("----------------")
    output.append("Decode input:")
    output.append(text_to_decode)
    output.append("----------------")

    start_time = time.time()

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

    # Binary (space-separated 8-bit groups)
    try:
        parts = text_to_decode.strip().split()
        decoded_binary = "".join(chr(int(b, 2)) for b in parts)
        output.append(f"Binary decoded: {decoded_binary}")
    except Exception:
        output.append("Binary: ERROR")

    # ASCII (space-separated decimal values)
    try:
        parts = text_to_decode.strip().split()
        decoded_ascii = "".join(chr(int(v)) for v in parts)
        output.append(f"ASCII decoded: {decoded_ascii}")
    except Exception:
        output.append("ASCII: ERROR")

    # Hex
    try:
        decoded_hex = bytes.fromhex(text_to_decode.strip()).decode("utf-8")
        output.append(f"Hex decoded: {decoded_hex}")
    except Exception:
        output.append("Hex: ERROR")

    # Morse
    try:
        decoded_morse = "".join(MORSE_DECODE.get(token, "?") for token in text_to_decode.strip().split(" "))
        output.append(f"Morse decoded: {decoded_morse}")
    except Exception:
        output.append("Morse: ERROR")

    # Semaphore
    try:
        decoded_semaphore = "".join(SEMAPHORE_DECODE.get(token, "?") for token in text_to_decode.strip().split(" "))
        output.append(f"Semaphore decoded: {decoded_semaphore}")
    except Exception:
        output.append("Semaphore: ERROR")

    # Barcode Numbers — tokens separated by "-"
    try:
        tokens = text_to_decode.strip().split("-")
        decoded_barcode = "".join(BARCODE_NUM_DECODE.get(t, "?") for t in tokens)
        output.append(f"Barcode decoded: {decoded_barcode}")
    except Exception:
        output.append("Barcode: ERROR")

    # Clock Code — space-separated tokens like "1" "2'" "|"
    try:
        tokens = text_to_decode.strip().split(" ")
        decoded_clock = "".join(CLOCK_DECODE.get(t, "?") for t in tokens)
        output.append(f"Clock decoded: {decoded_clock}")
    except Exception:
        output.append("Clock: ERROR")

    # DTMF — space-separated tokens like "2a" "3b" "0"
    try:
        tokens = text_to_decode.strip().split(" ")
        decoded_dtmf = "".join(DTMF_DECODE.get(t, "?") for t in tokens)
        output.append(f"DTMF decoded: {decoded_dtmf}")
    except Exception:
        output.append("DTMF: ERROR")

    elapsed = time.time() - start_time
    output.append("----------------")
    output.append(f"Took {elapsed:.8f} seconds")
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
