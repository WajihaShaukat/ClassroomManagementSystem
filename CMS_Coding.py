import mysql.connector as mysqlconnector
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image

def main():
    root = Tk()
    app = login(root)
    
      #========================================First Screen: Login =========================================
      #========================================First Screen: Login =========================================
      #========================================First Screen: Login =========================================
class login:
    def __init__(self, root):
      self.root =root
      self.root.title("Classroom Management System")
      self.root.geometry("1350x750+0+0")
      self.root.config(bg='white')
      self.frame = Frame(self.root,bg='white')
      self.frame.pack()
     # self.root.state('zoomed')
      self.Username = StringVar()
      self.Password = StringVar()

      self.bg_frame = Image.open('uitn.png')
      photo = ImageTk.PhotoImage(self.bg_frame)
      self.bg_panel = Label(self.root, image=photo)
      self.bg_panel.image = photo
      self.bg_panel.pack(fill='both')
      
        # ====== Login Frame =========================
      self.frame1 = LabelFrame(self.root, bg='navyblue', width=500, height=600 )
      self.frame1.place(x=700, y=70)
      
      #========================label and Entry===============================================
      self.login = Label(self.frame1, text ="Administrator",font=("yu gothic ui", 30, "bold"),bg="navyblue",fg="white")
      self.login.place(x = 140, y = 265)

     # self.loginn = Label(self.frame1, text ="WELCOME",font='bold 40',bg="black",fg="white")
     # self.loginn.place(x = 50, y = 30)

      self.lblfrstrow = Label(self.frame1, text ="Username ",font='bold 15',bg="navyblue" ,fg="white")
      self.lblfrstrow.place(x = 100, y = 350,width = 150, height = 50)

      self.lblsecrow = Label(self.frame1, text ="Password ",font='bold 15',bg="navyblue",fg="white")
      self.lblsecrow.place(x = 100, y = 400,width = 150, height = 50)

      self.Username = Entry(self.frame1)
      self.Username.place(x = 250, y = 350,width = 140, height = 45)

      self.password = Entry(self.frame1, width = 35,show="*")
      self.password.place(x = 250, y = 400,width = 140, height = 45)


      #==============================Importing Image===============================================
 
      self.img = ImageTk.PhotoImage(Image.open("login.png"))
      self.panel = Label(self.frame1, image = self.img,bg="navyblue")
      self.panel.place(x=200, y=180)

      #===============================Login, Reset and Exit Buttons================================================
      self.btnLogin = Button(self.frame1,text = 'LOG IN',width=17,bg="white",fg="black", command=self.fllooor)
      self.btnLogin.place(x = 200, y = 460,width = 110, height = 35)
      
      self.btnExit = Button(self.frame1,text = 'Exit',width=17,bg="black",fg="white", command=self.exittt)
      self.btnExit.place(x = 905, y = 505,width = 100, height = 30)
  #  def log(self):
   #     conn= mysqlconnector.connect(host="localhost", user="root", password="wajihasql123@", database="classroomdb",auth_plugin='mysql_native_password')
    #    my_cursor=conn.cursor()
     #   u=(self.username.get())
      #  p=(self.password.get())
       # sql="select *from login where username=%s and  password=%s"
        #my_cursor.execute(sql,[(u),(p)])
   #     result=my_cursor.fetchall()
  #      if result:
    #        messagebox.showinfo("Login Sccessfully")
     #       self.newWindow= Toplevel (self.window)
      #      self.app = fllooor(self.newWindow)
       #     self.username.set("")
        #    self.password.set("")
        #else:
         #   messagebox.showerror("Invalid Username or Password")
          #  self.username.set("")
           # self.password.set("")
                          
    #  self.btnReset = Button(self.frame1,text = 'Reset',width=17, command=self.new_window)
     # self.btnReset.place(x = 450, y = 400,width = 120, height = 40)
   
     #===============================Defining how new screen appears================================================
    def fllooor(self):
        self.flloor= Toplevel (self.root)
        self.app = floor(self.flloor)
    def exittt(self):
        self.exitt= Toplevel (self.root)
        self.app = exiit(self.exit)
        
     #===============================Defining Exit Button================================================

class exiit:
    def __init__(self, root):
          self.root =root
          self.root.title("Student Management Sytem")
          self.root.geometry('1350x750+0+0')
          self.root.config(bg='black')
          self.frame = Frame(self.root,bg='lightblue')
          self.frame.pack()

          self.img = ImageTk.PhotoImage(Image.open("ii.png"))
          self.panel = Label(self.root, image = self.img,bg="black")
          self.panel.place(x=880,y=80)          

          self.title_label= Label(self.root,text="Thank You!", font = ("arial",50,"bold"))
          self.title_label.place(x=350,y=340)

          self.title_label2= Label(self.root,text="Best Wishes for Future", font = ("arial",15,"bold"),bg="black",foreground="blue")
          self.title_label2.place(x=430,y=430)

          self.title_label3= Label(self.root,text="Wajiha Shaukat", font = ("arial",13,"bold"),bg="black",foreground="yellow")
          self.title_label3.place(x=480,y=460)
          
      #========================================Second Screen: Floor Selection =========================================
      #========================================Second Screen: Floor Selection =========================================
      #========================================Second Screen: Floor Selection =========================================

class floor:
    def __init__(self, root):
          self.root =root
          self.root.title("Classroom Management Sytem")
          self.root.geometry('1350x750+0+0')
          self.root.config(bg='white')
          self.frame = Frame(self.root,bg='lightblue')
          self.frame.pack()
          
          self.bg_frame1 = Image.open('ff.jpg')
          photo = ImageTk.PhotoImage(self.bg_frame1)
          self.bg_panel = Label(self.root, image=photo)
          self.bg_panel.image = photo
          self.bg_panel.pack(fill='both')
        # ====== Login Frame =========================
          self.frame2 = LabelFrame(self.root, bg='navyblue', width=500, height=650 )
          self.frame2.place(x=70, y=50)

          self.login = Label(self.frame2, text ="Floor Selection",font=("yu gothic ui", 30, "bold"),bg="navyblue",fg="white")
          self.login.place(x = 100, y = 20)

         #===============================1st, 2nd and 3rd Floor Buttons================================================
          self.ffloor = Button(self.frame2,text = 'FIRST FLOOR',font = ("arial",15),width=17,bg="white",fg="black", command=self.firfloor)
          self.ffloor.place(x = 140, y = 90,width = 170, height = 150)
                          
          self.sfloor = Button(self.frame2,text = 'SECOND FLOOR',font = ("arial",15),width=17,bg="white",fg="black", command=self.secfloor)
          self.sfloor.place(x = 140, y = 250,width = 170, height = 150)
      
          self.tfloor = Button(self.frame2,text = 'THIRD FLOOR',font = ("arial",15),width=17,bg="white",fg="black", command=self.thirrfloor)
          self.tfloor.place(x = 140, y = 410,width = 170, height = 150)

          self.backfloor = Button(self.frame2,text = 'Back to Login',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.back)
          self.backfloor.place(x = 30, y = 570,width = 100, height = 50)



      #===============================Defining how new screen appears================================================
    def back(self):
        self.backk= Toplevel (self.root)
        self.app = login(self.backk)

    def firfloor(self):
        self.firfloor= Toplevel (self.root)
        self.app = firstfloor(self.firfloor)
        
    def secfloor(self):
        self.secfloor= Toplevel (self.root)
        self.app = secondfloor(self.secfloor)

    def thirrfloor(self):
        self.thirfloor= Toplevel (self.root)
        self.app = thirdfloor(self.thirfloor)








        
      #========================================1st Floor  =========================================
      #======================================== 1st Floor =========================================
      #======================================== 1st Floor =========================================          
      #========================================1st Floor  =========================================
      #======================================== 1st Floor =========================================
      #======================================== 1st Floor =========================================


class firstfloor:
    def __init__(self, root):
          self.root =root
          self.root.title("Classroom Management Sytem")
          self.root.geometry('1350x750+0+0')
          self.root.config(bg='white')
          self.frame = Frame(self.root,bg='lightblue')
          self.frame.pack()
          
          
          self.bg_frame3 = Image.open('ccc.png')
          photo = ImageTk.PhotoImage(self.bg_frame3)
          self.bg_panel = Label(self.root, image=photo)
          self.bg_panel.image = photo
          self.bg_panel.pack(fill='both')
        # ====== Login Frame =========================
          self.frame3 = LabelFrame(self.root, bg='navyblue', width=600, height=650 )
          self.frame3.place(x=70, y=50)
          self.login = Label(self.frame3, text ="Select Classroom",font=("yu gothic ui", 30, "bold"),bg="navyblue",fg="white")
          self.login.place(x = 140, y = 20)

          self.room201 = Button(self.frame3,text = 'ROOM 201',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm201)
          self.room201.place(x = 120, y = 90,width = 160, height = 150)
                          
          self.room202 = Button(self.frame3,text = 'ROOM 202',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm202)
          self.room202.place(x = 120, y = 250,width = 160, height = 150)
      
          self.room203 = Button(self.frame3,text = 'LAB CL-1',font = ("arial",15),width=17,bg="white",fg="black", command=self.laab1)
          self.room203.place(x = 200, y = 410,width = 160, height = 150)

          self.room204 = Button(self.frame3,text = 'ROOM 203',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm203)
          self.room204.place(x = 290, y = 90,width = 160, height = 150)

          self.lab1 = Button(self.frame3,text = 'ROOM 204',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm204)
          self.lab1.place(x = 290, y = 250,width = 160, height = 150)

          

          self.backfloor22 = Button(self.frame3,text = 'Go to 2nd Floor',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.f2)
          self.backfloor22.place(x = 120, y = 580,width = 100, height = 50)

          self.backfloor33 = Button(self.frame3,text = 'Go to 3rd Floor',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.f3)
          self.backfloor33.place(x = 230, y = 580,width = 100, height = 50)

          self.backfloor = Button(self.frame3,text = 'Back to Login',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.back)
          self.backfloor.place(x = 340, y = 580,width = 100, height = 50)

    def f2(self):
        self.f22= Toplevel (self.root)
        self.app = secondfloor(self.f22)

    def f3(self):
        self.f33= Toplevel (self.root)
        self.app = thirdfloor(self.f33)

    def back(self):
        self.backk= Toplevel (self.root)
        self.app = login(self.backk)
        

      #===============================Defining how new screen appears================================================
    def romm201(self):
        self.rom201= Toplevel (self.root)
        self.app = room201(self.rom201)

    def romm202(self):
        self.rom202= Toplevel (self.root)
        self.app = room202(self.rom202)
        
    def romm203(self):
        self.rom203= Toplevel (self.root)
        self.app = room203(self.rom203)

    def romm204(self):
        self.rom204= Toplevel (self.root)
        self.app = room204(self.rom204)

    def laab1(self):
        self.laab1= Toplevel (self.root)
        self.app = lab1(self.laab1)


      #========================================R-201 Screen: 1st Floor  =========================================
      #========================================R-201Screen: 1st Floor =========================================
class room201:
    def __init__(self, ro201):
          self.ro201 =ro201
          self.ro201.title("classroom Management Sytem")
          self.ro201.geometry('1350x750+0+0')
          self.ro201.config(bg='White')
          self.frame = Frame(self.ro201,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro201,text="Room 201", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
                 #=====================all variables==============#
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()

          self.search_by=StringVar()
          self.search_text=StringVar()

                 #=====================Frames==============#
          frame1 = LabelFrame(self.ro201 ,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro201,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

       #   frame3 = Frame(self.root,bg="white",bd=10,relief=RIDGE)
        #  frame3.place(x=45,y=560,width=360)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
       
       
       
           #====================Buttons======================#
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

         # exiit = Button (frame1, text ="Exit", font("italic",15),bg="white",command=self.Exit).grid(row=0,column=0,padx=10,pady=10)

        #====================Search=====================
          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

        #==================================
          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)


          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)

          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)

          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          
          self.fetch()
          
        
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
           # messagebox.showerror("Error","Insert all attributes")
            room201(self.ro201)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r201 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
           # messagebox.showinfo("Inserted","Record has been inserted successfully")
            room201(self.ro201)
            
            
  #  def update(self):
   #         con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
    #        my_cursor = con.cursor()
     #       my_cursor.execute("update r201 set tname=%s,tid=%s,coursen=%s,courseid=%s,dept=%s,batch=%s,sec=%s,time=%s,day=%s",(self.tname.get(),self.tid.get(), self.coursen.get(),
       #                                                                                                                        self.courseid.get(), self.dept.get(), self.batch.get(),
        #                                                                                                                       self.sec.get(),self.time.get(),self.day.get()))
         #   con.commit()
          #  self.fetch()
           # con.close()
            #messagebox.showinfo("success","Record has been Updated")
            #room201(self.root)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r201")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()


    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r201 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()


        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r201 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
              # messagebox.showerror("Error", "Insert Accurate Time")
               room201(self.ro201)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r201 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
       #    if result:
           query="delete from r201 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
              #  messagebox.showinfo("Deleted","Record has been deleted")
       #    else:
              # messagebox.showerror("Message","Error! Insert Time")
               
           

           con.commit()
           con.close()
           self.fetch()
           room201(self.ro201)
          
          
        #  self.backfloor = Button(self.frame201,text = 'Back to Floor Selection',font = ("arial",10),width=17,bg="black",fg="white", command=self.back)
         # self.backfloor.place(x = 50, y = 500,width = 170, height = 50)

#    def back(self):
 #       self.backk= Toplevel (self.root)
  #      self.app =floor(self.backk)






      #========================================R-202 Screen: 1st Floor  =========================================
      #========================================R-202 Screen: 1st Floor =========================================
class room202:
    def __init__(self, ro202):
          self.ro202 =ro202
          self.ro202.title("classroom Management Sytem")
          self.ro202.geometry('1350x750+0+0')
          self.ro202.config(bg='White')
          self.frame = Frame(self.ro202,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro202,text="Room 202", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro202 ,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro202,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room202(self.ro202)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r202 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room202(self.ro202)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r202")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r202 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r202 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room202(self.ro202)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r202 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r202 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room202(self.ro202)




      #========================================R-203 Screen: 1st Floor  =========================================
      #========================================R-203Screen: 1st Floor =========================================


    
class room203:
    def __init__(self, ro203):
          self.ro203 =ro203
          self.ro203.title("classroom Management Sytem")
          self.ro203.geometry('1350x750+0+0')
          self.ro203.config(bg='White')
          self.frame = Frame(self.ro203,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro203,text="Room 203", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro203 ,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro203,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room203(self.ro203)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r203 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room203(self.ro203)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r203")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r203 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r203 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room203(self.ro203)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r203 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r203 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room203(self.ro203)


      #========================================R-204 Screen: 1st Floor  =========================================
      #========================================R-204 Screen: 1st Floor =========================================


    
class room204:
    def __init__(self, ro204):
          self.ro204 =ro204
          self.ro204.title("classroom Management Sytem")
          self.ro204.geometry('1350x750+0+0')
          self.ro204.config(bg='White')
          self.frame = Frame(self.ro204,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro204,text="Room 204", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro204 ,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro204,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room204(self.ro204)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r204 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room204(self.ro204)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r204")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r204 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r204 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room204(self.ro204)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r204 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r204 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room204(self.ro204)



      #========================================lab CL-1 Screen: 1st Floor  =========================================
      #========================================lab CL-1 Screen: 1st Floor =========================================
class lab1:
    def __init__(self, labb1):
          self.labb1 =labb1
          self.labb1.title("classroom Management Sytem")
          self.labb1.geometry('1350x750+0+0')
          self.labb1.config(bg='White')
          self.frame = Frame(self.labb1,bg='White')
          self.frame.pack()

          self.title_label= Label(self.labb1,text="CL-I", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.labb1,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.labb1,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            lab1(self.labb1)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into l1 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            lab1(self.labb1)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l1 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from l1 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               lab1(self.labb1)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from l1 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from l1 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           lab1(self.labb1)
           
      #======================================== 2nd Floor =========================================
      #======================================== 2nd Floor =========================================

class secondfloor:
    def __init__(self, root):
          self.root =root
          self.root.title("Student Management Sytem")
          self.root.geometry('1350x750+0+0')
          self.root.config(bg='black')
          self.frame = Frame(self.root,bg='lightblue')
          self.frame.pack()
          
          self.bg_frame3 = Image.open('ccc.png')
          photo = ImageTk.PhotoImage(self.bg_frame3)
          self.bg_panel = Label(self.root, image=photo)
          self.bg_panel.image = photo
          self.bg_panel.pack(fill='both')
        # ====== Login Frame =========================
          self.frame3 = LabelFrame(self.root, bg='navyblue', width=600, height=650 )
          self.frame3.place(x=70, y=50)
          self.login = Label(self.frame3, text ="Select Classroom",font=("yu gothic ui", 30, "bold"),bg="navyblue",fg="white")
          self.login.place(x = 140, y = 20)

          self.room201 = Button(self.frame3,text = 'ROOM 301',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm301)
          self.room201.place(x = 120, y = 90,width = 160, height = 150)
                          
          self.room202 = Button(self.frame3,text = 'ROOM 302',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm302)
          self.room202.place(x = 120, y = 250,width = 160, height = 150)
      
          self.room203 = Button(self.frame3,text = 'LAB CL-2',font = ("arial",15),width=17,bg="white",fg="black", command=self.laab2)
          self.room203.place(x = 120, y = 410,width = 160, height = 150)

          self.room204 = Button(self.frame3,text = 'ROOM 303',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm303)
          self.room204.place(x = 290, y = 90,width = 160, height = 150)

          self.lab1 = Button(self.frame3,text = 'ROOM 304',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm304)
          self.lab1.place(x = 290, y = 250,width = 160, height = 150)

          self.room203 = Button(self.frame3,text = 'LAB CL-4',font = ("arial",15),width=17,bg="white",fg="black", command=self.laab4)
          self.room203.place(x = 290, y = 410,width = 160, height = 150)

          

          self.backfloor11 = Button(self.frame3,text = 'Go to 1st Floor',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.f1)
          self.backfloor11.place(x = 120, y = 580,width = 100, height = 50)

          self.backfloor33 = Button(self.frame3,text = 'Go to 3rd Floor',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.f3)
          self.backfloor33.place(x = 230, y = 580,width = 100, height = 50)

          self.backfloor = Button(self.frame3,text = 'Back to Login',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.back)
          self.backfloor.place(x = 340, y = 580,width = 100, height = 50)
    def f1(self):
        self.f11= Toplevel (self.root)
        self.app = firstfloor(self.f11)

    def f3(self):
        self.f33= Toplevel (self.root)
        self.app = thirdfloor(self.f33)

    def back(self):
        self.backk= Toplevel (self.root)
        self.app = login(self.backk)




      #===============================Defining how new screen appears================================================
    def romm301(self):
        self.rom301= Toplevel (self.root)
        self.app = room301(self.rom301)

    def romm302(self):
        self.rom302= Toplevel (self.root)
        self.app = room302(self.rom302)
        
    def romm303(self):
        self.rom303= Toplevel (self.root)
        self.app = room303(self.rom303)

    def romm304(self):
        self.rom304= Toplevel (self.root)
        self.app = room304(self.rom304)

    def laab2(self):
        self.laab2= Toplevel (self.root)
        self.app = lab2(self.laab2)

    def laab4(self):
        self.laab4= Toplevel (self.root)
        self.app = lab4(self.laab4)

      #========================================R-301 Screen: 1st Floor  =========================================
      #========================================R-301Screen: 1st Floor =========================================


    
class room301:
    def __init__(self, ro301):
          self.ro301 =ro301
          self.ro301.title("classroom Management Sytem")
          self.ro301.geometry('1350x750+0+0')
          self.ro301.config(bg='White')
          self.frame = Frame(self.ro301,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro301,text="Room 301", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro301,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro301,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room301(self.ro301)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r301 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room301(self.ro301)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r301")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r301 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r301 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room301(self.ro301)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r301 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r301 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room301(self.ro301)

      #========================================R-302 Screen: 2nd Floor  =========================================
      #========================================R-302 Screen: 2nd Floor =========================================


    
class room302:
    def __init__(self, ro302):
          self.ro302 =ro302
          self.ro302.title("classroom Management Sytem")
          self.ro302.geometry('1350x750+0+0')
          self.ro302.config(bg='White')
          self.frame = Frame(self.ro302,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro302,text="Room 302", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro302,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro302,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room302(self.ro302)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r302 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room302(self.ro302)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r302")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r302 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r302 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room302(self.ro302)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r302 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r302 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room302(self.ro302)

      #========================================R-303 Screen: 2nd Floor  =========================================
      #========================================R-303Screen: 2nd Floor =========================================


    
class room303:
    def __init__(self, ro303):
          self.ro303 =ro303
          self.ro303.title("classroom Management Sytem")
          self.ro303.geometry('1350x750+0+0')
          self.ro303.config(bg='White')
          self.frame = Frame(self.ro303,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro303,text="Room 303", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro303,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro303,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room303(self.ro303)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r303 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room303(self.ro303)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r303")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r303 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r303 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room303(self.ro303)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r303 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r303 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room303(self.ro303)


      #========================================R-304 Screen: 2nd Floor  =========================================
      #========================================R-304 Screen: 2nd Floor =========================================


    
class room304:
    def __init__(self, ro304):
          self.ro304 =ro304
          self.ro304.title("classroom Management Sytem")
          self.ro304.geometry('1350x750+0+0')
          self.ro304.config(bg='White')
          self.frame = Frame(self.ro304,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro304,text="Room 304", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro304,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro304,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room304(self.ro304)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r304 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room304(self.ro304)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r304")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r304 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r304 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room304(self.ro304)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r304 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r304 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room304(self.ro304)

      #========================================lab CL-2 Screen: 2nd Floor  =========================================
      #========================================lab CL-2 Screen: 2nd Floor =========================================
class lab2:
    def __init__(self, labb2):
          self.labb2 =labb2
          self.labb2.title("classroom Management Sytem")
          self.labb2.geometry('1350x750+0+0')
          self.labb2.config(bg='White')
          self.frame = Frame(self.labb2,bg='White')
          self.frame.pack()

          self.title_label= Label(self.labb2,text="CL-II", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.labb2,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.labb2,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            lab2(self.labb2)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into l2 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            lab2(self.labb2)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l2")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l2 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from l2 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               lab2(self.labb2)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from l2 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from l2 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           lab2(self.labb2)
           
      #========================================lab CL-4 Screen: 2nd Floor  =========================================
      #========================================lab CL-4 Screen: 2nd Floor =========================================
class lab4:
    def __init__(self, labb4):
          self.labb4 =labb4
          self.labb4.title("classroom Management Sytem")
          self.labb4.geometry('1350x750+0+0')
          self.labb4.config(bg='White')
          self.frame = Frame(self.labb4,bg='White')
          self.frame.pack()

          self.title_label= Label(self.labb4,text="CL-IV", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.labb4,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.labb4,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            lab4(self.labb4)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into l4 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            lab4(self.labb4)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l4")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l4 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from l4 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               lab4(self.labb4)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from l4 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from l4 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           lab4(self.labb4)
           
      #========================================3rd Floor =========================================
      #======================================== 3rd Floor =========================================

class thirdfloor:
    def __init__(self, root):
          self.root =root
          self.root.title("classroom Management Sytem")
          self.root.geometry('1350x750+0+0')
          self.root.config(bg='black')
          self.frame = Frame(self.root,bg='lightblue')
          self.frame.pack()
          
          self.bg_frame3 = Image.open('ccc.png')
          photo = ImageTk.PhotoImage(self.bg_frame3)
          self.bg_panel = Label(self.root, image=photo)
          self.bg_panel.image = photo
          self.bg_panel.pack(fill='both')
        # ====== Login Frame =========================
          self.frame3 = LabelFrame(self.root, bg='navyblue', width=600, height=650 )
          self.frame3.place(x=70, y=50)
          self.login = Label(self.frame3, text ="Select Classroom",font=("yu gothic ui", 30, "bold"),bg="navyblue",fg="white")
          self.login.place(x = 140, y = 20)

          self.room201 = Button(self.frame3,text = 'ROOM 401',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm401)
          self.room201.place(x = 120, y = 90,width = 160, height = 150)
                          
          self.room202 = Button(self.frame3,text = 'ROOM 402',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm402)
          self.room202.place(x = 120, y = 250,width = 160, height = 150)
      
          self.room203 = Button(self.frame3,text = 'LAB CL-3',font = ("arial",15),width=17,bg="white",fg="black", command=self.laab3)
          self.room203.place(x = 200, y = 410,width = 160, height = 150)

          self.room204 = Button(self.frame3,text = 'ROOM 403',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm403)
          self.room204.place(x = 290, y = 90,width = 160, height = 150)

          self.lab1 = Button(self.frame3,text = 'ROOM 404',font = ("arial",15),width=17,bg="white",fg="black", command=self.romm404)
          self.lab1.place(x = 290, y = 250,width = 160, height = 150)

          

          self.backfloor1 = Button(self.frame3,text = 'Go to 1stFloor',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.f1)
          self.backfloor1.place(x = 120, y = 580,width = 100, height = 50)

          self.backfloor22 = Button(self.frame3,text = 'Go to 2nd Floor',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.f2)
          self.backfloor22.place(x = 230, y = 580,width = 100, height = 50)

          self.backfloor = Button(self.frame3,text = 'Back to Login',font = ("arial",10),width=17,bg="navyblue",fg="white", command=self.back)
          self.backfloor.place(x = 340, y = 580,width = 100, height = 50)

    def f1(self):
        self.f11= Toplevel (self.root)
        self.app = firstfloor(self.f11)

    def f2(self):
        self.f22= Toplevel (self.root)
        self.app = secondfloor(self.f22)

    def back(self):
        self.backk= Toplevel (self.root)
        self.app = login(self.backk)



                #===============================Defining how new screen appears================================================
    def romm401(self):
        self.rom401= Toplevel (self.root)
        self.app = room401(self.rom401)

    def romm402(self):
        self.rom402= Toplevel (self.root)
        self.app = room402(self.rom402)
        
    def romm403(self):
        self.rom403= Toplevel (self.root)
        self.app = room403(self.rom403)

    def romm404(self):
        self.rom404= Toplevel (self.root)
        self.app = room404(self.rom404)

    def laab3(self):
        self.laab3= Toplevel (self.root)
        self.app = lab3(self.laab3)


      #========================================R-401 Screen: 3rd Floor  =========================================
      #========================================R-401Screen: 3rd Floor =========================================


    
class room401:
    def __init__(self, ro401):
          self.ro401 =ro401
          self.ro401.title("classroom Management Sytem")
          self.ro401.geometry('1350x750+0+0')
          self.ro401.config(bg='White')
          self.frame = Frame(self.ro401,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro401,text="Room 401", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro401,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro401,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room401(self.ro401)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r401 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room401(self.ro401)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r401")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r401 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r401 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room401(self.ro401)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r401 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r401 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room401(self.ro401)

      #========================================R-402 Screen: 3rd Floor  =========================================
      #========================================R-402 Screen: 3rd Floor =========================================


    
class room402:
    def __init__(self, ro402):
          self.ro402 =ro402
          self.ro402.title("classroom Management Sytem")
          self.ro402.geometry('1350x750+0+0')
          self.ro402.config(bg='White')
          self.frame = Frame(self.ro402,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro402,text="Room 402", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro402,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro402,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room402(self.ro402)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r402 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room402(self.ro402)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r402")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r402 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r402 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room402(self.ro402)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r402 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r402 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room402(self.ro402)

      #========================================R-403 Screen: 3rd Floor  =========================================
      #========================================R-403Screen: 3rd Floor =========================================


    
class room403:
    def __init__(self, ro403):
          self.ro403 =ro403
          self.ro403.title("classroom Management Sytem")
          self.ro403.geometry('1350x750+0+0')
          self.ro403.config(bg='White')
          self.frame = Frame(self.ro403,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro403,text="Room 403", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro403,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro403,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room403(self.ro403)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r403 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room403(self.ro403)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r403")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r403 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r403 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room403(self.ro403)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r403 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r403 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room403(self.ro403)


      #========================================R-404 Screen: 3rd Floor  =========================================
      #========================================R-404 Screen: 3rd Floor =========================================


    
class room404:
    def __init__(self, ro404):
          self.ro404 =ro404
          self.ro404.title("classroom Management Sytem")
          self.ro404.geometry('1350x750+0+0')
          self.ro404.config(bg='White')
          self.frame = Frame(self.ro404,bg='White')
          self.frame.pack()

          self.title_label= Label(self.ro404,text="Room 404", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.ro404,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.ro404,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            room404(self.ro404)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into r404 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            room404(self.ro404)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r404")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from r404 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from r404 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               room404(self.ro404)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from r404 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from r404 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           room404(self.ro404)

      #========================================lab CL-3 Screen: 3rd Floor  =========================================
      #========================================lab CL-3 Screen: 3rd Floor =========================================
    
class lab3:
    def __init__(self, labb3):
          self.labb3 =labb3
          self.labb3.title("classroom Management Sytem")
          self.labb3.geometry('1350x750+0+0')
          self.labb3.config(bg='White')
          self.frame = Frame(self.labb3,bg='White')
          self.frame.pack()

          self.title_label= Label(self.labb3,text="CL-III", font = ("arial",30,"bold"),border=12,relief=GROOVE, bg="darkblue",foreground="white")
          self.title_label.pack(side=TOP,fill=X)
          self.time=StringVar()
          self.day=StringVar()
          self.tname=StringVar()
          self.tid=StringVar()
          self.coursen=StringVar()
          self.courseid=StringVar()
          self.dept=StringVar()
          self.batch=StringVar()
          self.sec=StringVar()
          self.search_by=StringVar()
          self.search_text=StringVar()

          frame1 = LabelFrame(self.labb3,bd=12,relief=GROOVE,bg="darkblue")
          frame1.place(x=20,y=90,width=420,height=575)

          frame2 = Frame(self.labb3,bd=12,bg="darkblue",relief=RIDGE)
          frame2.place(x=460,y=90,width=810,height=580)

          frame4 = Frame(frame2,bd=4,relief=RIDGE,bg="white")
          frame4.place(x=10,y=65,width=760,height=475)

          time = Label(frame1,text='Time',font='bold 15',bg="darkblue",fg="white")
          time.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          etime = Entry(frame1,textvariable=self.time,font='bold 10',bd=5,relief=GROOVE)
          etime.grid(row=0,column=1,pady=10,padx=20,sticky="w")
            
          day = Label(frame1,text='Day',font='bold 15',bg="darkblue",fg="white")
          day.grid(row=1,column=0,pady=10,padx=20,sticky="w")

          eday = Entry(frame1,textvariable=self.day,font='bold 10',bd=5,relief=GROOVE)
          eday.grid(row=1,column=1,pady=10,padx=20,sticky="w")

          tname = Label(frame1,text='Teacher Name',font='bold 15',bg="darkblue",fg="white")
          tname.grid(row=2,column=0,pady=10,padx=20,sticky="w")

          etname= Entry(frame1,textvariable=self.tname,font='bold 10',bd=5,relief=GROOVE)
          etname.grid(row=2,column=1,pady=10,padx=20,sticky="w")

          tid = Label(frame1,text='Teacher ID',font='bold 15',bg="darkblue",fg="white")
          tid.grid(row=3,column=0,pady=10,padx=20,sticky="w")

          etid = Entry(frame1,textvariable=self.tid,font='bold 10',bd=5,relief=GROOVE)
          etid.grid(row=3,column=1,pady=10,padx=20,sticky="w")

          coursen = Label(frame1,text='Course',font='bold 15',bg="darkblue",fg="white")
          coursen.grid(row=4,column=0,pady=10,padx=20,sticky="w")

          ecoursen = Entry(frame1,textvariable=self.coursen,font='bold 10',bd=5,relief=GROOVE)
          ecoursen.grid(row=4,column=1,pady=10,padx=20,sticky="w")
          
          courseid = Label(frame1,text='Course Code',font='bold 15',bg="darkblue",fg="white")
          courseid.grid(row=5,column=0,pady=10,padx=20,sticky="w")

          ecourseid = Entry(frame1,textvariable=self.courseid,font='bold 10',bd=5,relief=GROOVE)
          ecourseid.grid(row=5,column=1,pady=10,padx=20,sticky="w")

          dept = Label(frame1,text='Department',font='bold 15',bg="darkblue",fg="white")
          dept.grid(row=6,column=0,pady=10,padx=20,sticky="w")

          edept = Entry(frame1,textvariable=self.dept,font='bold 10',bd=5,relief=GROOVE)
          edept.grid(row=6,column=1,pady=10,padx=20,sticky="w")

          batch = Label(frame1,text='Batch',font='bold 15',bg="darkblue",fg="white")
          batch.grid(row=7,column=0,pady=10,padx=20,sticky="w")

          ebatch = Entry(frame1,textvariable=self.batch,font='bold 10',bd=5,relief=GROOVE)
          ebatch.grid(row=7,column=1,pady=10,padx=20,sticky="w")

          sec= Label(frame1,text='Section',font='bold 15',bg="darkblue",fg="white")
          sec.grid(row=8,column=0,pady=10,padx=20,sticky="w")

          esec = Entry(frame1,textvariable=self.sec,font='bold 10',bd=5,relief=GROOVE)
          esec.grid(row=8,column=1,pady=10,padx=20,sticky="w")
       
          insert = Button (frame1, text = "Insert",font=("italic", 15),fg="darkblue",bg="white",command=self.insert)
          insert.place(x=0,y=470,height=40,width=100)
 
          delete = Button (frame1, text = "Delete",font=("italic",15),fg="darkblue",bg="white",command=self.delete)
          delete.place(x=100,y=470,height=40,width=100)

          clear = Button (frame1, text = "Clear",font=("italic ",15),fg="darkblue",bg="white",command=self.clear)
          clear.place(x=200,y=470,height=40,width=100)

          get = Button (frame1, text = "Get",font=("italic ",15),fg="darkblue",bg="white",command=self.get)
          get.place(x=300,y=470,height=40,width=98)

          search = Label(frame2,text="Classroom Information",bg="darkblue",fg="white",font=("times new roman",15,"bold"))
          search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

          search2 =ttk.Combobox(frame2,textvariable=self.search_by,width=10,font=("times new roman",13,"bold"),state='readonly')
          search2['values']=("day","time")
          search2.grid(row=0,column=1,pady=20,padx=10)

          search3 = Entry(frame2, textvariable=self.search_text ,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
          search3.grid(row=0,column=2,pady=10,padx=20,sticky="w")

          searchb = Button(frame2,text="Search",bg="white",width=10,pady=5,command=self.search).grid(row=0,column=3,padx=10,pady=10)
          searchbb = Button(frame2,text="Show All",bg="white",width=10,padx=10,pady=5,command=self.fetch).grid(row=0,column=4,padx=10,pady=10)

          self.scrollx = Scrollbar(frame4,orient=HORIZONTAL)
          self.scrolly = Scrollbar(frame4,orient=VERTICAL)
          self.table= ttk.Treeview(frame4,columns=("time","day","tname","tid","coursen","courseid","dept","batch","sec"),xscrollcommand=self.scrollx.set,yscrollcommand=self.scrolly.set)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.pack(side=BOTTOM,fill=X)
          self.scrolly.pack(side=RIGHT,fill=Y)
          self.scrollx.config(command=self.table.xview)
          self.scrolly.config(command=self.table.yview)
          self.table.heading("time",text="Time")
          self.table.heading("day",text="Day")
          self.table.heading("tname",text="Teacher Name")
          self.table.heading("tid",text="Teacher ID")
          self.table.heading("coursen",text="Course Name")
          self.table.heading("courseid",text="Course ID")
          self.table.heading("dept",text="Department")
          self.table.heading("batch",text="Batch")
          self.table.heading("sec",text="Section")

          self.table['show']='headings'
          self.table.column("time",width=90)
          self.table.column("day",width=90)
          self.table.column("tname",width=90)
          self.table.column("tid",width=90)
          self.table.column("coursen",width=90)
          self.table.column("courseid",width=90)
          self.table.column("dept",width=90)
          self.table.column("batch",width=90)
          self.table.column("sec",width=90)
          self.table.pack(fill=BOTH,expand=2)
          self.table.bind("<ButtonRelease-1>",self.get)
          self.fetch()
          
    def insert(self):
        if self.day.get()=="" or self.time.get()=="":
            lab3(self.labb3)
        else:
            con = mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
            my_cursor = con.cursor()
            my_cursor.execute("insert into l3 values (%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.time.get(), self.day.get(), self.tname.get(),
                                                                                self.tid.get(), self.coursen.get(),self.courseid.get(),
                                                                                self.dept.get(), self.batch.get(), self.sec.get()))
            con.commit()
            self.fetch()
            con.close()
            lab3(self.labb3)
            
    def fetch(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l3")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()

    def search(self):
        con= mysqlconnector.connect(host="localhost", user="root", password="wajiha123", database="uitdbb")
        my_cursor=con.cursor()
        my_cursor.execute("select * from l3 where" +str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.table.delete(*self.table.get_children())
            for i in rows:
                self.table.insert("",END,values=i)
                con.commit()
        con.close()
        
    def get_cursor(self,event=""):
           cursor_row=self.table.focus()
           content=self.table.item(cursor_row)
           
           row=content["values"]
           self.time.set(row[0])
           self.day.set(row[1])
           self.tname.set(row[2])
           self.tid.set(row[3])
           self.coursen.set(row[4])
           self.courseid.set(row[5])
           self.dept.set(row[6])
           self.batch.set(row[7])
           self.sec.set(row[8])
           
    def clear (self):
            self.time.set("")
            self.day.set("")
            self.tname.set("")
            self.tid.set("")
            self.coursen.set("")
            self.courseid.set("")
            self.dept.set("")
            self.batch.set("")
            self.sec.set("")
    def get(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           query="select * from l3 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           rows=my_cursor.fetchall()
           if rows:
               for row in rows:
                   self.time.set(row[0])
                   self.day.set(row[1])
                   self.tname.set(row[2])
                   self.tid.set(row[3])
                   self.coursen.set(row[4])
                   self.courseid.set(row[5])
                   self.dept.set(row[6])
                   self.batch.set(row[7])
                   self.sec.set(row[8])

           else:
               lab3(self.labb3)

    def delete(self):
           con= mysqlconnector.connect(host='localhost', password='wajiha123',user='root',database='uitdbb')
           my_cursor=con.cursor()
           sql="select * from l3 where time=%s"
           In=(self.time.get(),)
           my_cursor.execute(sql,In)
           result=my_cursor.fetchall()
           query="delete from l3 where time=%s"
           value=(self.time.get(),)
           my_cursor.execute(query,value)
           con.commit()
           con.close()
           self.fetch()
           lab3(self.labb3)



          
main()


