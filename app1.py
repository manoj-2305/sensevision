AK='Confirmation'
AJ='*.mp4;*.avi;*.mov'
AI='Video files'
AH='Do you want to use a sample video or upload your own? (Yes for sample, No to upload)'
AG='Select Video'
AF='User ID is not defined'
AE='*.jpg;*.jpeg;*.png'
AD='Image files'
AC='Do you want to use a sample image or upload your own? (Yes for sample, No to upload)'
AB='Select Image'
AA='python/video_object_detection.py'
A9='python/image_object_detection.py'
A8='emotionpy/video_emotion.py'
A7='emotionpy/img_emotion.py'
A6='Could not fetch history'
A5='<Button-1>'
A4='history'
A3='http://localhost/SenseVision_Application/php/history.php'
A2='password'
A1='login_frame'
A0='Password'
z='Camera Detection'
y='Video Detection'
x='Image Detection'
w='Emotion Detection'
v=print
t='file_type'
s='Helvetica'
r='☰'
q='*'
p='Register'
o='main_frame'
n='Object Detection'
m='-v'
l='-i'
k='file_name'
j='Back'
i='Login'
h=getattr
e='utf-8'
d='python'
c='./uploads'
b='No file selected!'
a='nw'
Z='Invalid response from server.'
X='email'
W='#00ccff'
V=ValueError
U='yes'
T='message'
S='user_id'
R='success'
Q='w'
O='Success'
N='history_frame'
M='both'
L=Exception
J=True
I='left'
H=hasattr
G='bold'
F=None
D='Error'
C='white'
import sys as Y,customtkinter as A
from tkinter import messagebox as B,filedialog as f
import requests as P,subprocess as E,os as K,shutil as g
class AL:
	def __init__(B,root):B.root=root;B.root.title(n);B.root.geometry('1200x600');A.set_appearance_mode('dark');B.user_id=F;B.title_font=A.CTkFont(size=24,weight=G);B.button_font=A.CTkFont(size=12);B.label_font=A.CTkFont(size=10);B.default_bg='#282a36';B.button_color='#6272a4';B.label_color='#f8f8f2';B.main_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.main_frame.pack(fill=M,expand=J);B.create_main_window()
	def destroy_main_app(A):
		if H(A,'home_page_frame'):A.home_page_frame.pack_forget();A.home_page_frame.destroy();A.home_page_frame=F
	def load_text_file(B,file_path):
		with open(file_path,'r')as A:return A.read()
	def create_main_window(B):
		F='#2a2a40';E='#1e1e2f'
		if H(B,o):B.main_frame.pack_forget();B.main_frame.destroy()
		B.main_frame=A.CTkFrame(B.root,fg_color=E);B.main_frame.pack(fill=M,expand=J);A.CTkLabel(B.main_frame,text='SenseVision Application',font=A.CTkFont(size=36,weight=G),text_color='#ff6600').pack(pady=(20,10));D=A.CTkFrame(B.main_frame,fg_color=E);D.pack(pady=(10,5));K=A.CTkButton(D,text=n,font=A.CTkFont(size=18,weight=G),text_color=C,command=B.show_object_detection_content);K.pack(side=I,padx=(10,20));L=A.CTkButton(D,text=w,font=A.CTkFont(size=18,weight=G),text_color=C,command=B.show_emotion_detection_content);L.pack(side=I);B.scrollable_frame=A.CTkScrollableFrame(B.main_frame,width=1200,height=600,fg_color=F);B.scrollable_frame.pack(padx=20,pady=10);B.show_object_detection_content();B.login_register_frame=A.CTkFrame(B.main_frame,fg_color=E);B.login_register_frame.place(relx=.85,rely=.1,anchor='center');N=A.CTkButton(B.login_register_frame,text=i,font=B.button_font,fg_color=F,text_color=C,command=B.show_login_frame);N.pack(side=I,padx=10);O=A.CTkButton(B.login_register_frame,text=p,font=B.button_font,fg_color=F,text_color=C,command=B.show_register_frame);O.pack(side=I,padx=10)
	def show_object_detection_content(B):
		for D in B.scrollable_frame.winfo_children():D.destroy()
		A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/object.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(10,20),padx=10);A.CTkLabel(B.scrollable_frame,text=x,font=A.CTkFont(size=28,weight=G),text_color=W).pack(pady=(10,5));A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/image.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(5,20),padx=10);A.CTkLabel(B.scrollable_frame,text=y,font=A.CTkFont(size=28,weight=G),text_color=W).pack(pady=(10,5));A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/video.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(5,20),padx=10);A.CTkLabel(B.scrollable_frame,text=z,font=A.CTkFont(size=28,weight=G),text_color=W).pack(pady=(10,5));A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/camera.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(5,20),padx=10)
	def show_emotion_detection_content(B):
		for D in B.scrollable_frame.winfo_children():D.destroy()
		A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/emotion.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(10,20),padx=10);A.CTkLabel(B.scrollable_frame,text='Emotion Detection via Image',font=A.CTkFont(size=28,weight=G),text_color=W).pack(pady=(10,5));A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/image_emotion.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(5,20),padx=10);A.CTkLabel(B.scrollable_frame,text='Emotion Detection via Video',font=A.CTkFont(size=28,weight=G),text_color=W).pack(pady=(10,5));A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/video_emotion.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(5,20),padx=10);A.CTkLabel(B.scrollable_frame,text='Emotion Detection via Camera',font=A.CTkFont(size=28,weight=G),text_color=W).pack(pady=(10,5));A.CTkLabel(B.scrollable_frame,text=B.load_text_file('textfiles/camera_emotion.txt'),font=A.CTkFont(size=18),text_color=C,justify=I,wraplength=1100).pack(anchor=Q,pady=(5,20),padx=10)
	def show_login_frame(B):
		if H(B,o):B.main_frame.pack_forget()
		if H(B,'register_frame'):B.register_frame.pack_forget()
		B.login_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.login_frame.pack(fill=M,expand=J);A.CTkLabel(B.login_frame,text=i,font=B.title_font,text_color=B.label_color).pack(pady=20);A.CTkLabel(B.login_frame,text='Email',font=B.label_font,text_color=B.label_color).pack(pady=5);B.email_entry=A.CTkEntry(B.login_frame,width=300);B.email_entry.pack(pady=5);A.CTkLabel(B.login_frame,text=A0,font=B.label_font,text_color=B.label_color).pack(pady=5);B.password_entry=A.CTkEntry(B.login_frame,width=300,show=q);B.password_entry.pack(pady=5);A.CTkButton(B.login_frame,text='Forgot Password?',font=B.button_font,fg_color=B.default_bg,text_color=B.label_color,command=B.show_forgot_password_frame).pack(padx=5,pady=5);A.CTkButton(B.login_frame,text=i,font=B.button_font,fg_color=B.button_color,text_color=C,command=B.login).pack(pady=10);A.CTkButton(B.login_frame,text=j,font=B.button_font,fg_color=B.button_color,text_color=C,command=lambda:[B.create_main_window(),B.login_frame.destroy()]).pack(pady=10)
	def show_forgot_password_frame(B):
		if H(B,A1):B.login_frame.pack_forget()
		B.forgot_password_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.forgot_password_frame.pack(fill=M,expand=J);A.CTkLabel(B.forgot_password_frame,text='Forgot Password',font=B.title_font,text_color=B.label_color).pack(pady=20);A.CTkLabel(B.forgot_password_frame,text='Enter your email:',font=B.label_font,text_color=B.label_color).pack(pady=15);B.forgot_email_entry=A.CTkEntry(B.forgot_password_frame,width=300);B.forgot_email_entry.pack(pady=5);B.otp_entry=F;B.new_password_entry=F;A.CTkButton(B.forgot_password_frame,text='Send OTP',font=B.button_font,fg_color=B.button_color,text_color=C,command=B.send_otp).pack(pady=10);B.loading_label=A.CTkLabel(B.forgot_password_frame,text='',font=B.button_font,text_color=B.label_color);B.loading_label.pack(pady=15)
	def send_otp(A):
		C=A.forgot_email_entry.get()
		if not C:B.showerror(D,'Please enter your email address.');return
		A.loading_label.configure(text='Sending mail, please wait...');A.root.update_idletasks();F=P.post('http://localhost/SenseVision_Application/php/forgot_password.php',data={X:C})
		try:
			E=F.json()
			if E.get(R):B.showinfo(O,'OTP sent to your email.');A.display_otp_entry(C)
			else:B.showerror(D,E.get(T,'Failed to send OTP.'))
		except V:B.showerror(D,Z)
		finally:A.loading_label.configure(text='')
	def display_otp_entry(B,email):
		if B.otp_entry:B.otp_entry.destroy()
		A.CTkLabel(B.forgot_password_frame,text='Enter OTP:',font=B.label_font,text_color=B.label_color).pack(pady=5);B.otp_entry=A.CTkEntry(B.forgot_password_frame,width=300);B.otp_entry.pack(pady=5);A.CTkButton(B.forgot_password_frame,text='Verify OTP',font=B.button_font,fg_color=B.button_color,text_color=C,command=lambda:B.verify_otp(email)).pack(pady=10)
	def verify_otp(C,email):
		E=email;A=C.otp_entry.get()
		if not A:B.showerror(D,'Please enter the OTP.');return
		G=P.post('http://localhost/SenseVision_Application/php/verify_otp.php',data={X:E,'otp':A})
		try:
			F=G.json()
			if F.get(R):B.showinfo(O,'OTP verified successfully.');C.display_new_password_entry(E,A)
			else:B.showerror(D,F.get(T,'Invalid or expired OTP.'))
		except V:B.showerror(D,Z)
	def display_new_password_entry(B,email,otp):
		if B.new_password_entry:B.new_password_entry.destroy()
		A.CTkLabel(B.forgot_password_frame,text='Enter New Password:',font=B.label_font,text_color=B.label_color).pack(pady=5);B.new_password_entry=A.CTkEntry(B.forgot_password_frame,width=300,show=q);B.new_password_entry.pack(pady=5);A.CTkButton(B.forgot_password_frame,text='Reset Password',font=B.button_font,fg_color=B.button_color,text_color=C,command=lambda:B.reset_password(email,otp)).pack(pady=10)
	def reset_password(A,email,otp,new_password=F):
		C=new_password;C=A.new_password_entry.get()
		if not C:B.showerror(D,'Please enter the new password.');return
		F=P.post('http://localhost/SenseVision_Application/php/reset_password.php',data={X:email,'otp':otp,'new_password':C})
		try:
			E=F.json()
			if E.get(R):B.showinfo(O,'Password reset successfully!');A.forgot_password_frame.destroy();A.login_frame.pack(fill=M,expand=J)
			else:B.showerror(D,E.get(T,'Failed to reset password.'))
		except V:B.showerror(D,Z)
	def show_register_frame(B):
		if H(B,o):B.main_frame.pack_forget()
		if H(B,A1):B.login_frame.pack_forget()
		B.register_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.register_frame.pack(fill=M,expand=J);A.CTkLabel(B.register_frame,text=p,font=B.title_font,text_color=B.label_color).pack(pady=20);A.CTkLabel(B.register_frame,text='Name',font=B.label_font,text_color=B.label_color).pack(pady=5);B.name_entry=A.CTkEntry(B.register_frame,width=300);B.name_entry.pack(pady=5);A.CTkLabel(B.register_frame,text='Phone',font=B.label_font,text_color=B.label_color).pack(pady=5);B.phone_entry=A.CTkEntry(B.register_frame,width=300);B.phone_entry.pack(pady=5);A.CTkLabel(B.register_frame,text='Email',font=B.label_font,text_color=B.label_color).pack(pady=5);B.register_email_entry=A.CTkEntry(B.register_frame,width=300);B.register_email_entry.pack(pady=5);A.CTkLabel(B.register_frame,text=A0,font=B.label_font,text_color=B.label_color).pack(pady=5);B.register_password_entry=A.CTkEntry(B.register_frame,width=300,show=q);B.register_password_entry.pack(pady=5);A.CTkButton(B.register_frame,text=p,font=B.button_font,fg_color=B.button_color,text_color=C,command=B.register).pack(pady=10);A.CTkButton(B.register_frame,text=j,font=B.button_font,fg_color=B.button_color,text_color=C,command=lambda:[B.create_main_window(),B.register_frame.destroy()]).pack(pady=10)
	def login(A):
		H='Login Error';I=A.email_entry.get();J=A.password_entry.get();E=P.post('http://localhost/SenseVision_Application/php/login.php',data={X:I,A2:J})
		try:C=E.json()
		except V:B.showerror(D,'Invalid response from server: '+E.text);return
		if C.get(R):
			B.showinfo(i,'Login successful!');G=C.get(S)
			if G is not F:A.user_id=G;A.login_frame.destroy();A.show_main_app(C['user'])
			else:B.showerror(H,'User  ID not found in response.')
		else:B.showerror(H,C.get(T,'Invalid credentials'))
	def register(A):
		C=A.name_entry.get();E=A.phone_entry.get();F=A.register_email_entry.get();G=A.register_password_entry.get();H=P.post('http://localhost/SenseVision_Application/php/register.php',data={'name':C,'phone':E,X:F,A2:G});I=H.json()
		if I.get(R):B.showinfo(O,'Registration Successful!');A.register_frame.destroy();A.show_login_frame()
		else:B.showerror(D,'All fields are required!')
	def show_main_app(B,user):D=user;B.main_frame.pack_forget();B.home_page_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.home_page_frame.pack(fill=M,expand=J);E=A.CTkButton(B.home_page_frame,text=r,font=(s,16),fg_color=B.button_color,text_color=C,width=40,height=40,command=lambda:B.toggle_menu(D));E.pack(side=I,padx=10,pady=10,anchor=a);A.CTkButton(B.home_page_frame,text=n,font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda user=D:[B.show_object_detection(user),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.home_page_frame,text=w,font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda user=D:[B.show_Emotion_Detection(user),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20)
	def show_Emotion_Detection(B,user):B.home_page_frame.pack_forget();B.Emotion_Detection_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.Emotion_Detection_frame.pack(fill=M,expand=J);D=A.CTkButton(B.Emotion_Detection_frame,text=r,font=(s,16),fg_color=B.button_color,text_color=C,width=40,height=40,command=lambda:B.toggle_menu(user));D.pack(side=I,padx=10,pady=10,anchor=a);A.CTkButton(B.Emotion_Detection_frame,text='Emotion Detection(image)',font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.run_image_emotion_detection(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.Emotion_Detection_frame,text='Emotion Detection(video)',font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.run_video_emotion_detection(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.Emotion_Detection_frame,text='Emotion Detection(webcam)',font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.run_cam_emotion_detection(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.Emotion_Detection_frame,text=j,font=B.button_font,fg_color=B.button_color,text_color=C,command=lambda:[B.show_main_app(user),B.Emotion_Detection_frame.destroy(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=10)
	def show_object_detection(B,user):B.home_page_frame.pack_forget();B.object_detection_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.object_detection_frame.pack(fill=M,expand=J);D=A.CTkButton(B.object_detection_frame,text=r,font=(s,16),fg_color=B.button_color,text_color=C,width=40,height=40,command=lambda:B.toggle_menu(user));D.pack(side=I,padx=10,pady=10,anchor=a);A.CTkButton(B.object_detection_frame,text=x,font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.run_image_detection(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.object_detection_frame,text=y,font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.run_video_detection(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.object_detection_frame,text=z,font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.run_camera_detection(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=20);A.CTkButton(B.object_detection_frame,text=j,font=B.button_font,fg_color=B.button_color,text_color=C,command=lambda:[B.show_main_app(user),B.object_detection_frame.destroy(),B.history_frame.destroy()if H(B,N)else F]).pack(pady=10)
	def toggle_menu(B,user):D=A.CTkToplevel(B.root);D.geometry('350x650');D.title('Menu');D.configure(fg_color=B.default_bg);D.attributes('-topmost',J);A.CTkLabel(D,text=f"Name: {user["name"]}",font=A.CTkFont(size=16,weight=G),text_color=B.label_color).pack(padx=10,pady=10);A.CTkLabel(D,text=f"Email: {user[X]}",font=A.CTkFont(size=16,weight=G),text_color=B.label_color).pack(pady=10);A.CTkButton(D,text='History',font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[D.destroy(),B.history_frame.destroy()if H(B,N)else F,B.show_history_frame()]).pack(pady=20);A.CTkButton(D,text='Logout',font=A.CTkFont(size=14,weight=G),fg_color=B.button_color,text_color=C,command=lambda:[B.destroy_main_app(),B.create_main_window(),D.destroy(),B.history_frame.destroy()if H(B,N)else F,B.Emotion_Detection_frame.destroy()if H(B,'Emotion_Detection_frame')else F,B.object_detection_frame.destroy()if H(B,'object_detection_frame')else F]).pack(pady=20)
	def show_history_frame(B):B.history_frame=A.CTkFrame(B.root,fg_color=B.default_bg);B.history_frame.pack(fill=M,expand=J);A.CTkLabel(B.history_frame,text='Upload History',font=B.title_font,text_color=B.label_color).pack(pady=20,padx=20,anchor=a);B.search_entry=A.CTkEntry(B.history_frame,placeholder_text='Search history...',width=300);B.search_entry.pack(pady=10,padx=20);B.history_list_frame=A.CTkFrame(B.history_frame,fg_color=B.default_bg);B.history_list_frame.pack(fill=M,expand=J);B.search_entry.bind('<KeyRelease>',B.filter_history);B.canvas=A.CTkCanvas(B.history_list_frame,bg=B.default_bg);B.scrollbar=A.CTkScrollbar(B.history_list_frame,orientation='vertical',command=B.canvas.yview);B.scrollable_frame=A.CTkFrame(B.canvas,fg_color=B.default_bg);B.scrollable_frame.bind('<Configure>',lambda e:B.canvas.configure(scrollregion=B.canvas.bbox('all')));B.canvas.create_window((0,0),window=B.scrollable_frame,anchor=a);B.canvas.pack(side=I,fill=M,expand=J);B.scrollbar.pack(side='right',fill='y');B.canvas.configure(yscrollcommand=B.scrollbar.set);B.load_history();A.CTkButton(B.history_frame,text='Run Detection',font=B.button_font,fg_color=B.button_color,text_color=C,command=B.run_detection_on_selected_file).pack(pady=10)
	def load_history(C):
		K=h(C,S,F)
		if not C.user_id:B.showerror(D,'User not logged in.');return
		L=P.Session();M=L.post(A3,data={S:K})
		try:
			H=M.json()
			if H.get(R):
				for N in C.scrollable_frame.winfo_children():N.destroy()
				for J in H[A4]:O=f"{J[k]} ({J[t]})";E=A.CTkFrame(C.scrollable_frame,fg_color=C.button_color);E.pack(pady=5,padx=10,fill='x');Q=A.CTkLabel(E,text='📁',font=A.CTkFont(size=30,weight=G),text_color=C.label_color);Q.pack(side=I,padx=5);U=A.CTkLabel(E,text=O,font=A.CTkFont(size=10,weight=G),text_color=C.label_color);U.pack(side=I,padx=5);E.bind(A5,lambda event,file_name=J[k],item=E:C.select_history_item(file_name,item))
			else:B.showerror(D,H.get(T,A6))
		except V:B.showerror(D,Z)
	def select_history_item(A,file_name,history_item):
		C=file_name
		for D in A.scrollable_frame.winfo_children():D.configure(fg_color=A.button_color)
		history_item.configure(fg_color='#44475a');A.selected_file_name=C;B.showinfo('Selected File',f"You selected: {C}")
	def filter_history(C,event):
		L=C.search_entry.get().lower()
		for M in C.scrollable_frame.winfo_children():M.destroy()
		J=h(C,S,F)
		if not J:B.showerror(D,'User  not logged in.');return
		N=P.Session();O=N.post(A3,data={S:J})
		try:
			G=O.json()
			if G.get(R):
				for H in G[A4]:
					K=f"{H[k]} ({H[t]})"
					if L in K.lower():E=A.CTkFrame(C.scrollable_frame,fg_color=C.button_color);E.pack(pady=5,padx=10,fill='x');Q=A.CTkLabel(E,text='📁',font=C.label_font,text_color=C.label_color);Q.pack(side=I,padx=5);U=A.CTkLabel(E,text=K,font=C.label_font,text_color=C.label_color);U.pack(side=I,padx=5);E.bind(A5,lambda event,file_name=H[k],item=E:C.select_history_item(file_name,item))
			else:B.showerror(D,G.get(T,A6))
		except V:B.showerror(D,Z)
	def run_detection_on_selected_file(R):
		Q='.mov';P='.avi';N='.mp4';M='.png';J='.jpeg';I='.jpg'
		if not H(R,'selected_file_name'):B.showerror(D,b);return
		G=R.selected_file_name;F=K.path.join(c,G);A=K.path.splitext(G)[1].lower()
		try:
			if A in[I,J,M,N,P,Q]:
				S=B.askquestion('Detection Type','Do you want to perform Emotion Detection? (No for Object Detection)')
				if S==U:
					if A in[I,J,M]:C=E.Popen([Y.executable,A7,l,F],stdout=E.PIPE,stderr=E.PIPE)
					elif A in[N,P,Q]:C=E.Popen([Y.executable,A8,m,F],stdout=E.PIPE,stderr=E.PIPE)
					else:B.showerror(D,'Unsupported file type for Emotion Detection!');return
				elif A in[I,J,M]:C=E.Popen([d,A9,l,F],stdout=E.PIPE,stderr=E.PIPE)
				elif A in[N,P,Q]:C=E.Popen([d,AA,m,F],stdout=E.PIPE,stderr=E.PIPE)
				else:B.showerror(D,'Unsupported file type for Object Detection!');return
				W,T=C.communicate()
				if C.returncode!=0:raise L(f"Error in detection process: {T.decode(e)}")
				B.showinfo(O,f"Detection completed for {G}")
			else:B.showerror(D,'Unsupported file type!')
		except L as V:B.showerror(D,str(V))
	def run_image_detection(G):
		P=B.askquestion(AB,AC)
		if P==U:A='samples/sample.jpg'
		else:
			A=f.askopenfilename(filetypes=[(AD,AE)])
			if not A:B.showerror(D,b);return
		H=c;K.makedirs(H,exist_ok=J);I=K.path.basename(A);C=K.path.join(H,I)
		try:
			g.copy2(A,C);M=E.Popen([d,A9,l,C],stdout=E.PIPE,stderr=E.PIPE);T,Q=M.communicate()
			if M.returncode!=0:raise L(f"Error in detection process: {Q.decode(e)}")
			N=h(G,S,F)
			if not N:raise L(AF)
			G.upload_file(C,N,'image');B.showinfo(O,f"Image detection completed for {I}")
		except L as R:B.showerror(D,f"Error during image detection: {R}")
	def run_image_emotion_detection(G):
		P=B.askquestion(AB,AC)
		if P==U:A='samples/sample1.jpg'
		else:
			A=f.askopenfilename(filetypes=[(AD,AE)])
			if not A:B.showerror(D,b);return
		H=c;K.makedirs(H,exist_ok=J);I=K.path.basename(A);C=K.path.join(H,I)
		try:
			g.copy2(A,C);M=E.Popen([Y.executable,A7,l,C],stdout=E.PIPE,stderr=E.PIPE);T,Q=M.communicate()
			if M.returncode!=0:raise L(f"Error in detection process: {Q.decode(e)}")
			N=h(G,S,F)
			if not N:raise L(AF)
			G.upload_file(C,N,'image');B.showinfo(O,f"Image detection completed for {I}")
		except L as R:B.showerror(D,f"Error during image detection: {R}")
	def upload_file(H,file_path,user_id,file_type):
		C='file';D='http://localhost/SenseVision_Application/php/upload.php';B={C:open(file_path,'rb')};E={S:user_id,t:file_type}
		try:
			F=P.post(D,files=B,data=E);A=F.json()
			if not A.get(R):raise L(A.get(T,'Unknown error occurred'))
			v('File upload successful:',A)
		except L as G:v(f"Error during file upload: {G}")
		finally:B[C].close()
	def run_video_detection(F):
		M=B.askquestion(AG,AH)
		if M==U:A='samples/sample_video.mp4'
		else:
			A=f.askopenfilename(filetypes=[(AI,AJ)])
			if not A:B.showerror(D,b);return
		G=c;K.makedirs(G,exist_ok=J);H=K.path.basename(A);C=K.path.join(G,H)
		try:
			g.copy2(A,C);I=E.Popen([d,AA,m,C],stdout=E.PIPE,stderr=E.PIPE);R,N=I.communicate()
			if I.returncode!=0:raise L(f"Error in detection process: {N.decode(e)}")
			P=F.user_id;F.upload_file(C,P,'video');B.showinfo(O,f"Video detection completed for {H}")
		except L as Q:B.showerror(D,f"Error during video detection: {Q}")
	def run_video_emotion_detection(F):
		M=B.askquestion(AG,AH)
		if M==U:A='samples/sample_video1.mp4'
		else:
			A=f.askopenfilename(filetypes=[(AI,AJ)])
			if not A:B.showerror(D,b);return
		G=c;K.makedirs(G,exist_ok=J);H=K.path.basename(A);C=K.path.join(G,H)
		try:
			g.copy2(A,C);I=E.Popen([Y.executable,A8,m,C],stdout=E.PIPE,stderr=E.PIPE);R,N=I.communicate()
			if I.returncode!=0:raise L(f"Error in detection process: {N.decode(e)}")
			P=F.user_id;F.upload_file(C,P,'video');B.showinfo(O,f"Video emotion detection completed for {H}")
		except L as Q:B.showerror(D,f"Error during video emotion detection: {Q}")
	def run_camera_detection(F):
		A=B.askquestion(AK,'Are you sure you want to start camera detection?')
		if A==U:
			try:G=E.Popen([d,'python/cam_object_detection.py'])
			except E.CalledProcessError as C:B.showerror(D,f"Error running camera detection: {C}")
	def run_cam_emotion_detection(F):
		A=B.askquestion(AK,'Are you sure you want to start camera emotion detection?')
		if A==U:
			try:G=E.Popen([Y.executable,'emotionpy/cam_emotion.py'])
			except E.CalledProcessError as C:B.showerror(D,f"Error running camera emotion detection: {C}")
if __name__=='__main__':u=A.CTk();AM=AL(u);u.mainloop()