from tkinter import*
from tkinter import ttk
import tkinter.messagebox
from PIL import Image,ImageTk
import tkinter
from student import Student
import os
from time import strftime
from datetime import datetime
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #image 1
        img=Image.open(r"images\stanford.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #image2
        img1=Image.open(r"images\face.webp")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)
        
        #image3
        img2=Image.open(r"images\ugo.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=550,height=130)

    
        # #backgrounf image
        img3=Image.open(r"images\bigimggg.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #==============time=====================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl=Label(title_lbl,font=('times new roman',14,'bold',),background='white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

        #student detail4
        img4=Image.open(r"images\students.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)



        #detect face butto5
        img5=Image.open(r"images\beta.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)


        #attendance button
        img6=Image.open(r"images\attendance.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)


        #help button
        img7=Image.open(r"images\uwu.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)


        #train data button
        img8=Image.open(r"images\train2.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)


        #Photos face button
        img9=Image.open(r"images\group.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)


        #Developer face button
        img10=Image.open(r"images\man.png")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)


        #Exit face button
        img11=Image.open(r"images\out.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")
        pass

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","You sure want to exit?",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return



    #=========functions buttons======

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)



    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)



    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

   







    




        



       





        
    

















if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
