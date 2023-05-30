import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.title("Appearance mode")
root.geometry("600x350")

#fuctions
def darkmode():
    customtkinter.set_appearance_mode("dark")
def lightmode():
    customtkinter.set_appearance_mode("light")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=10, pady=10, fill="both", expand=True)

#the buttons
btn1 = customtkinter.CTkButton(frame, text="Dark", command=darkmode)
btn1.pack(padx=20, pady=20)

btn2 = customtkinter.CTkButton(frame, text="light", command=lightmode)
btn2.pack(padx=20, pady=20)


root.mainloop()
