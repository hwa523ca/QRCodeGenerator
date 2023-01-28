import tkinter as tk
import qrcode

class QRGUI:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("QR Code Generator")

        self.label = tk.Label(self.root, text="Enter in the link here", font=('Arial', 18))
        self.label.pack(padx=10, pady=0)

        self.link_entry = tk.Entry(self.root, font=('Arial', 16))
        self.link_entry.pack(padx=0, pady=0)

        self.label2 = tk.Label(self.root, text="Enter in the file name here", font=('Arial', 18))
        self.label2.pack(padx=10, pady=0)

        self.file_entry = tk.Entry(self.root, font=('Arial', 16))
        self.file_entry.pack(padx=0, pady=0)

        self.button = tk.Button(self.root, text="Generate QR Code", font=('Arial', 18), command=self.make_qr_code)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def make_qr_code(self):
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4
        )
        
        link = self.link_entry.get()
        qr.add_data(link)
        qr.make(fit = True)
        img = qr.make_image(fill_color = "black", back_color = "white")

        file_name = str(self.file_entry.get())

        #print(f"{link}\n{file_name}")

        if ".png" not in file_name:
            file_name += ".png"

        img.save(file_name)

QRGUI()