import customtkinter as ctk
from PIL import Image, ImageTk
import os
pin=1
def home():
        try:
            p1.destroy()
        except:
            pass
        try:
            pbal.destroy()
        except:
            pass 
        try:
            pwith.destroy()
        except:
            pass 
        try:
            pwit.destroy()
        except:
            pass
        try:
            pdepo.destroy()
        except:
            pass 
        try:
            pdep.destroy()
        except:
            pass
        try:
            app.destroy()
        except:
            pass
        try:
            pt.destroy()
        except:
            pass
        try:
            ptr.destroy()
        except:
            pass
        try:
            ptra.destroy()
        except:
            pass
        second()
def close():
        try:
            global pin
            if pin==5561:
                f=open('5561.txt','w')
                f.write(str(bal))
                f.close()
            if pin==4823:
                f=open('4823.txt','w')
                f.write(str(bal))
                f.close()
            if pin==6034:
                f=open('6034.txt','w')
                f.write(str(bal))
                f.close()
            p1.destroy()
        except:
            pass
        try:
            pbal.destroy()
        except:
            pass 
        try:
            pwith.destroy()
        except:
            pass 
        try:
            pwit.destroy()
        except:
            pass
        try:
            pdepo.destroy()
        except:
            pass 
        try:
            pdep.destroy()
        except:
            pass
        try:
            app.destroy()
        except:
            pass
        try:
            ptr.destroy()
        except:
            pass
        try:
            pt.destroy()
        except:
            pass
        try:
            ptra.destroy()
        except:
            pass
def pincheck(e):
    global bal
    input=t1.get()
    global pin
    if str(input)=="5561":
        pin=5561
        f=open('5561.txt','r')
        a= f.read()
        bal=int(a)
        f.close()
        p1.destroy()
        second()
    elif str(input)=="4823":
        pin=4823
        f=open('4823.txt','r')
        a= f.read()
        bal=int(a)
        f.close()
        p1.destroy()
        second()
    elif str(input)=="6034":
        pin=6034
        f=open('6034.txt','r')
        a= f.read()
        bal=int(a)
        f.close()
        p1.destroy()
        second()
    else:
        l=ctk.CTkLabel(master=p1,text="Try Again",font=("Gill Sans MT Bold", 25,),fg_color="#a80202", text_color="#FFFFFF",)
        l.grid(row=0,column=0, padx=(0,180),pady=(180,0))
def deposit():
    global pdep
    app.destroy()
    pdep=ctk.CTk()
    pdep.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdraw.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pdep, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    b1=ctk.CTkButton(master=pdep, text="100 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=deposited1)
    b1.grid(row=0, column=0, padx=(0,175), pady=(0,200))
    b2=ctk.CTkButton(master=pdep, text="200 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=deposited2)
    b2.grid(row=0, column=0, padx=(0,175), pady=(0,0))
    b3=ctk.CTkButton(master=pdep, text="500AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=deposited3)
    b3.grid(row=0, column=0, padx=(0,175), pady=(200,0))
    b4=ctk.CTkButton(master=pdep, text="1000 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=deposited4)
    b4.grid(row=0, column=0, padx=(0,175), pady=(400,0),)
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pdep, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pdep, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pdep.mainloop()
def second():
    global app
    app=ctk.CTk()
    app.geometry("1200x700")
    i=ctk.CTkImage(Image.open("2.png"), size=(1200,700))
    bg= ctk.CTkLabel(master=app, image=i, text="")
    bg.grid(row=0, column=0, padx=(0,170), pady=(0,70))
    b1=ctk.CTkButton(master=app, text="Withdraw", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=withdraw)
    b1.grid(row=0, column=0, padx=(0,175), pady=(0,200))
    b2=ctk.CTkButton(master=app, text="Deposit", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101", command=deposit)
    b2.grid(row=0, column=0, padx=(0,175), pady=(0,0))
    b3=ctk.CTkButton(master=app, text="Transfer", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101", command=transfer)
    b3.grid(row=0, column=0, padx=(0,175), pady=(200,0))
    b4=ctk.CTkButton(master=app, text="Balance", width=220, font=("Gill Sans MT Bold", 20,), height=60,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=balance)
    b4.grid(row=0, column=0, padx=(810,0), pady=(0,525),)
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=app, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=app, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    app.mainloop()
def balance():
    global pbal
    app.destroy()
    pbal=ctk.CTk()
    pbal.geometry("1200x700")
    i2=ctk.CTkImage(Image.open("Balance.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pbal, image=i2, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    l1=ctk.CTkLabel(master=pbal,text=str(bal),font=("Gill Sans MT Bold", 40,),fg_color="#a80202", text_color="#FFFFFF",)
    l1.grid(row=0,column=0, padx=(0,180),pady=(100,0))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pbal, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pbal, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pbal.mainloop()
def withdraw():
    global pwit
    app.destroy()
    pwit=ctk.CTk()
    pwit.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdraw.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pwit, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    b1=ctk.CTkButton(master=pwit, text="100 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=withdrew1)
    b1.grid(row=0, column=0, padx=(0,175), pady=(0,200))
    b2=ctk.CTkButton(master=pwit, text="200 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=withdrew2)
    b2.grid(row=0, column=0, padx=(0,175), pady=(0,0))
    b3=ctk.CTkButton(master=pwit, text="500AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=withdrew3)
    b3.grid(row=0, column=0, padx=(0,175), pady=(200,0))
    b4=ctk.CTkButton(master=pwit, text="1000 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=withdrew4)
    b4.grid(row=0, column=0, padx=(0,175), pady=(400,0),)
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pwit, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pwit, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pwit.mainloop()
def withdrew1():
    global pwith
    global bal
    bal=bal-100
    pwit.destroy()
    pwith=ctk.CTk()
    pwith.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdrew.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pwith, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pwith.mainloop()
def withdrew2():
    global pwith
    global bal
    bal=bal-200
    pwit.destroy()
    pwith=ctk.CTk()
    pwith.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdrew.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pwith, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pwith.mainloop()
def withdrew3():
    global pwith
    global bal
    bal=bal-500
    pwit.destroy()
    pwith=ctk.CTk()
    pwith.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdrew.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pwith, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pwith.mainloop()
def withdrew4():
    global pwith
    global bal
    bal=bal-1000
    pwit.destroy()
    pwith=ctk.CTk()
    pwith.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdrew.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pwith, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pwith, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pwith.mainloop()
def deposited1():
    global pdepo
    global bal
    bal=bal+100
    pdep.destroy()
    pdepo=ctk.CTk()
    pdepo.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Deposit.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pdepo, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pdepo.mainloop()
def deposited2():
    global pdepo
    global bal
    bal=bal+200
    pdep.destroy()
    pdepo=ctk.CTk()
    pdepo.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Deposit.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pdepo, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pdepo.mainloop()
def deposited3():
    global pdepo
    global bal
    bal=bal+500
    pdep.destroy()
    pdepo=ctk.CTk()
    pdepo.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Deposit.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pdepo, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pdepo.mainloop()
def deposited4():
    global pdepo
    global bal
    bal=bal+1000
    pdep.destroy()
    pdepo=ctk.CTk()
    pdepo.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Deposit.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=pdepo, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pdepo, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pdepo.mainloop()
def transfer():
    global t2
    global pt
    app.destroy()
    pt=ctk.CTk()
    pt.geometry("1200x700")
    img=ctk.CTkImage(Image.open("Transfer.png"), size=(1200,700))
    bg= ctk.CTkLabel(master=pt, image=img, text="")
    bg.grid(row=0, column=0, padx=(0,170), pady=(0,70))
    t2=ctk.CTkEntry(master=pt, placeholder_text="", border_width=0, corner_radius=7, width=260, height=70, bg_color="#FFFFFF", fg_color="#FFFFFF",font=("Gill Sans MT Bold", 25 ,),text_color="Black")
    t2.grid(row=0, column=0, padx=(0,150), pady=(35,0))
    pt.bind('<Return>',tcheck)
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=pt, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=pt, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    pt.mainloop()
def tcheck(e):
    global l1
    global l2
    global l3
    input=t2.get()
    if input.isnumeric()==False:
        try:
            l2.destroy()
        except:
            pass
        try:
            l3.destroy()
        except:
            pass
        l1=ctk.CTkLabel(master=pt,text="Enter only numbers",font=("Gill Sans MT Bold", 25,),fg_color="#a80202", text_color="#FFFFFF",)
        l1.grid(row=0,column=0, padx=(0,180),pady=(180,0))
    elif len(str(input))!=10:
        try:
            l1.destroy()
        except:
            pass
        try:
            l3.destroy()
        except:
            pass
        l2=ctk.CTkLabel(master=pt,text="Account number must be 10 characters long",font=("Gill Sans MT Bold", 25,),fg_color="#a80202", text_color="#FFFFFF",)
        l2.grid(row=0,column=0, padx=(0,180),pady=(180,0))
    elif str(input)[0]=="0":
        try:
            l2.destroy()
        except:
            pass
        try:
            l1.destroy()
        except:
            pass
        l3=ctk.CTkLabel(master=pt,text="Enter valid account number",font=("Gill Sans MT Bold", 25,),fg_color="#a80202", text_color="#FFFFFF",)
        l3.grid(row=0,column=0, padx=(0,180),pady=(180,0))
    else:
        transferring()
def transferring():
    global ptr
    pt.destroy()
    ptr=ctk.CTk()
    ptr.geometry("1200x700")
    i3=ctk.CTkImage(Image.open("Withdraw.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=ptr, image=i3, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    b1=ctk.CTkButton(master=ptr, text="100 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=transferred1)
    b1.grid(row=0, column=0, padx=(0,175), pady=(0,200))
    b2=ctk.CTkButton(master=ptr, text="200 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=transferred2)
    b2.grid(row=0, column=0, padx=(0,175), pady=(0,0))
    b3=ctk.CTkButton(master=ptr, text="500AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=transferred3)
    b3.grid(row=0, column=0, padx=(0,175), pady=(200,0))
    b4=ctk.CTkButton(master=ptr, text="1000 AED", width=291.9, font=("Gill Sans MT Bold", 25,), height=90.3,bg_color="#a80202",fg_color="#a80202", hover_color="#470101",command=transferred4)
    b4.grid(row=0, column=0, padx=(0,175), pady=(400,0),)
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=ptr, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=ptr, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    ptr.mainloop()
def transferred1():
    global ptra
    global bal
    bal=bal-100
    ptr.destroy()
    ptra=ctk.CTk()
    ptra.geometry("1200x700")
    i4=ctk.CTkImage(Image.open("Transferred.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=ptra, image=i4, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    ptra.mainloop()
def transferred2():
    global ptra
    global bal
    bal=bal-200
    ptr.destroy()
    ptra=ctk.CTk()
    ptra.geometry("1200x700")
    i4=ctk.CTkImage(Image.open("Transferred.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=ptra, image=i4, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    ptra.mainloop()
def transferred3():
    global ptra
    global bal
    bal=bal-500
    ptr.destroy()
    ptra=ctk.CTk()
    ptra.geometry("1200x700")
    i4=ctk.CTkImage(Image.open("Transferred.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=ptra, image=i4, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    ptra.mainloop()
def transferred4():
    global ptra
    global bal
    bal=bal-1000
    ptr.destroy()
    ptra=ctk.CTk()
    ptra.geometry("1200x700")
    i4=ctk.CTkImage(Image.open("Transferred.png"), size=(1200,700))
    bg1= ctk.CTkLabel(master=ptra, image=i4, text="")
    bg1.grid(row=0,column=0,padx=(0,170),pady=(0,70))
    img= ctk.CTkImage(Image.open("Home.png"))
    b=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img,command=home)
    b.grid(row=0, column=0, padx=(0,1200), pady=(0,685))
    img2= ctk.CTkImage(Image.open("x.png"))
    x=ctk.CTkButton(master=ptra, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
    x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
    ptra.mainloop()
p1=ctk.CTk()
p1.geometry("1200x700")
img=ctk.CTkImage(Image.open("du.png"), size=(1200,700))
bg= ctk.CTkLabel(master=p1, image=img, text="")
bg.grid(row=0, column=0, padx=(0,170), pady=(0,70))
t1=ctk.CTkEntry(master=p1, placeholder_text="", border_width=0, corner_radius=7, width=260, height=70, bg_color="#FFFFFF", fg_color="#FFFFFF",font=("Gill Sans MT Bold", 25 ,),text_color="Black")
t1.grid(row=0, column=0, padx=(0,172), pady=(50,0))
p1.bind('<Return>',pincheck)
img2= ctk.CTkImage(Image.open("x.png"))
x=ctk.CTkButton(master=p1, text="", width=40, font=("Gill Sans MT Bold", 25,), height=40,bg_color="#a80202",fg_color="#a80202", hover_color="#a80202",image=img2,command=close)
x.grid(row=0, column=0, padx=(900,0), pady=(0,685))
p1.mainloop()
