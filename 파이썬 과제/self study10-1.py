from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "C:\\Users\\cjwon\\OneDrive\\바탕 화면\\대학교 파일\\엔트리 팀플 자료\\책뭉이.webp")
photo2 = PhotoImage(file = "C:\\Users\\cjwon\\OneDrive\\바탕 화면\\대학교 파일\\엔트리 팀플 자료\\책뭉이.webp")

label1 = Label(window, image = photo1)
label2 = Label(window, image = photo1)

label1.pack(side=LEFT)
label2.pack(side=LEFT)

window.mainloop()