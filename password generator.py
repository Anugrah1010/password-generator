import random
import string
import tkinter as tk
from tkinter import messagebox

def open_password_generator():
    root.destroy()
    password_generator()

def password_generator():
    def generate_password():
        length = length_entry.get()
        try:
            length = int(length)
            if length > 10:
                messagebox.showerror("Error", "Panjang password maksimal adalah 10!")
            else:
                characters = string.ascii_letters + string.digits + string.punctuation
                password = ''.join(random.choice(characters) for _ in range(length))
                password_label.config(text="Password: " + password)
        except ValueError:
            messagebox.showerror("Error", "Silahkan masukkan angka sebagai panjang password!")

    root = tk.Tk()
    root.title("UAS PBO KELOMPOK 14 - Password Generator")

    # Background color
    root.configure(bg="black")

    # Header
    header_label = tk.Label(root, text="Welcome to Random Password Generator", font=("Times New Roman", 20), bg="black", fg="white")
    header_label.pack(pady=20)

    # Password Length
    length_frame = tk.Frame(root, bg="black")
    length_frame.pack()

    length_label = tk.Label(length_frame, text="Silahkan masukkan angka panjang password! : ", font=("Times New Roman", 10), bg="black", fg="white")
    length_label.pack(side=tk.LEFT, padx=10)

    length_entry = tk.Entry(length_frame, font=("Times New Roman", 10))
    length_entry.pack(side=tk.LEFT, padx=10)

    # Generate Button
    generate_button = tk.Button(root, text="Generate", font=("Times New Roman", 10), bg="gray", command=generate_password)
    generate_button.pack(pady=10)

    # Password Display
    password_label = tk.Label(root, text="Password:", font=("Times New Roman", 14), bg="black", fg="white")
    password_label.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("UAS PBO KELOMPOK 14")

    # Background color
    root.configure(bg="black")

    # Header
    header_label = tk.Label(root, text="Cara Pemakaian Aplikasi", font=("Times New Roman", 20), bg="black", fg="white")
    header_label.pack(pady=20)

    # Instructions
    instructions = [
        "1. Jalankan aplikasi dengan menjalankan script ini.",
        "2. Aplikasi akan membuka jendela utama yang berisi instruksi penggunaan.",
        "3. Pada jendela utama, masukkan panjang password yang diinginkan.",
        "4. Tekan tombol 'Generate' untuk membuat password.",
        "5. Password yang dihasilkan akan ditampilkan pada jendela utama.",
        "6. Jika ingin membuat password baru, ulangi langkah 3-5.",
        "7. Tutup aplikasi dengan menutup jendela."
    ]

    for instruction in instructions:
        label = tk.Label(root, text=instruction, font=("Times New Roman", 12), bg="black", fg="white")
        label.pack()

    # Open Password Generator Button
    open_button = tk.Button(root, text="Buka Aplikasi", font=("Times New Roman", 12), bg="gray", command=open_password_generator)
    open_button.pack(pady=20)

    root.mainloop()
