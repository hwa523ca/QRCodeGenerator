import customtkinter as custtk
import qrcode

custtk.set_appearance_mode("dark")
custtk.set_default_color_theme("blue")
class CQRGUI():
    def __init__(self):
        self.root = custtk.CTk()
        self.root.geometry("600x300")

        self.root.title("QR Code Generator")

        self.label = custtk.CTkLabel(master=self.root, text="Enter in the link here", font=('Arial', 18))
        self.label.pack(padx=10, pady=0)

        self.link_entry = custtk.CTkEntry(master=self.root, font=('Arial', 16))
        self.link_entry.pack(padx=0, pady=0)

        self.label2 = custtk.CTkLabel(master=self.root, text="Enter in the file name here", font=('Arial', 18))
        self.label2.pack(padx=10, pady=0)

        self.file_entry = custtk.CTkEntry(master=self.root, font=('Arial', 16))
        self.file_entry.pack(padx=0, pady=0)

        self.button = custtk.CTkButton(master=self.root, text="Generate QR Code", font=('Arial', 18), command=self.make_qr_code)
        self.button.pack(padx=10, pady=10)

        self.label3 = custtk.CTkLabel(master=self.root, text="", font=('Arial', 18))
        self.label3.pack(padx=10, pady=0)

        self.root.mainloop()

    def make_qr_code(self):
        try:
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

            #print(f"{link}\n{file_name}") #For debugging purposes.

            if ".png" not in file_name:
                file_name += ".png"

            if file_name == ".png" or link == None:
                self.label3.config(text="Error in creating QR Code.")
            else:
                img.save(file_name)
                self.label3.configure(text="QR Code successfully created.")
        except:
            self.label3.configure(text="Error in creating QR Code.")

CQRGUI()