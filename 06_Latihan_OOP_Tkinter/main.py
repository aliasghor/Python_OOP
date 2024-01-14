import tkinter

main_window = tkinter.Tk()

label1 = tkinter.Label(main_window,text="Ini adalah Label 1")
label2 = tkinter.Label(main_window,text="Ini adalah label 2")

tombol1 = tkinter.Button(main_window,text="Ini adalah tombol 1")
tombol2 = tkinter.Button(main_window,text="Ini adalah tombol 2")

label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# Method menampilkan GUI
main_window.mainloop()