import  sys
import customtkinter as ctk
from tkinter import messagebox, filedialog
import requests,subprocess,os,shutil
class ObjectDetectionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Object Detection")
        self.root.geometry("1200x600")
        ctk.set_appearance_mode("dark")
        self.user_id = None

        # Fonts and Styles
        self.title_font = ctk.CTkFont(size=24, weight="bold")
        self.button_font = ctk.CTkFont(size=12)
        self.label_font = ctk.CTkFont(size=10)
        self.default_bg = "#282a36"
        self.button_color = "#6272a4"
        self.label_color = "#f8f8f2"

        # Main Frame
        self.main_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.main_frame.pack(fill="both", expand=True)

        self.create_main_window()
    
    def destroy_main_app(self):
        """Destroys the main application frame if it exists."""
        if hasattr(self, 'home_page_frame'):
            self.home_page_frame.pack_forget()  # Hide the main app frame
            self.home_page_frame.destroy()       # Destroy it
            self.home_page_frame = None  
            # Clear the reference
    def load_text_file(self, file_path):
        with open(file_path, 'r') as file:
            return file.read()
        
    def create_main_window(self):

        if hasattr(self, 'main_frame'):
            self.main_frame.pack_forget()  # Hide the existing main frame
            self.main_frame.destroy()       # Destroy the existing main frame

        # Create a new main frame
        self.main_frame = ctk.CTkFrame(self.root, fg_color="#1e1e2f")
        self.main_frame.pack(fill="both", expand=True)
    
        # Title
        ctk.CTkLabel(
            self.main_frame,
            text="SenseVision Application",
            font=ctk.CTkFont(size=36, weight="bold"),
            text_color="#ff6600"
        ).pack(pady=(20, 10))

        # Buttons for Object Detection and Emotion Detection
        button_frame = ctk.CTkFrame(self.main_frame, fg_color="#1e1e2f")
        button_frame.pack(pady=(10, 5))

        object_detection_btn = ctk.CTkButton(
            button_frame,
            text="Object Detection",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="white",
            command=self.show_object_detection_content
        )
        object_detection_btn.pack(side="left", padx=(10, 20))

        emotion_detection_btn = ctk.CTkButton(
            button_frame,
            text="Emotion Detection",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color="white",
            command=self.show_emotion_detection_content
        )
        emotion_detection_btn.pack(side="left")

        # Scrollable Frame for content
        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.main_frame,
            width=1200,
            height=600,
            fg_color="#2a2a40"
        )
        self.scrollable_frame.pack(padx=20, pady=10)

        # Default content for Object Detection
        self.show_object_detection_content()

        # Login and Register buttons (top-right corner)
        self.login_register_frame = ctk.CTkFrame(self.main_frame, fg_color="#1e1e2f")
        self.login_register_frame.place(relx=0.85, rely=0.1, anchor="center")

        login_btn = ctk.CTkButton(
            self.login_register_frame,
            text="Login",
            font=self.button_font,
            fg_color="#2a2a40",
            text_color="white",
            command=self.show_login_frame
        )
        login_btn.pack(side="left", padx=10)

        register_btn = ctk.CTkButton(
            self.login_register_frame,
            text="Register",
            font=self.button_font,
            fg_color="#2a2a40",
            text_color="white",
            command=self.show_register_frame
        )
        register_btn.pack(side="left", padx=10)


    def show_object_detection_content(self):
        # Clear previous content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Add Object Detection Description
        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/object.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(10, 20), padx=10)

        # Add Subtopics for Object Detection
        ctk.CTkLabel(
            self.scrollable_frame,
            text="Image Detection",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ccff"
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/image.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(5, 20), padx=10)

        ctk.CTkLabel(
            self.scrollable_frame,
            text="Video Detection",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ccff"
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/video.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(5, 20), padx=10)

        ctk.CTkLabel(
            self.scrollable_frame,
            text="Camera Detection",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ccff"
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/camera.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(5, 20), padx=10)


    def show_emotion_detection_content(self):
        # Clear previous content
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        # Add Emotion Detection Description
        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/emotion.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(10, 20), padx=10)

        # Add Subtopics for Emotion Detection
        ctk.CTkLabel(
            self.scrollable_frame,
            text="Emotion Detection via Image",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ccff"
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/image_emotion.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(5, 20), padx=10)

        ctk.CTkLabel(
            self.scrollable_frame,
            text="Emotion Detection via Video",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ccff"
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/video_emotion.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(5, 20), padx=10)

        ctk.CTkLabel(
            self.scrollable_frame,
            text="Emotion Detection via Camera",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#00ccff"
        ).pack(pady=(10, 5))

        ctk.CTkLabel(
            self.scrollable_frame,
            text=self.load_text_file("textfiles/camera_emotion.txt"),
            font=ctk.CTkFont(size=18),
            text_color="white",
            justify="left",
            wraplength=1100
        ).pack(anchor="w", pady=(5, 20), padx=10)



    def show_login_frame(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.pack_forget()
        if hasattr(self, 'register_frame'):
            self.register_frame.pack_forget()

        self.login_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.login_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(self.login_frame, text="Login", font=self.title_font, text_color=self.label_color).pack(pady=20)
        ctk.CTkLabel(self.login_frame, text="Email", font=self.label_font, text_color=self.label_color).pack(pady=5)
        self.email_entry = ctk.CTkEntry(self.login_frame, width=300)
        self.email_entry.pack(pady=5)
        ctk.CTkLabel(self.login_frame, text="Password", font=self.label_font, text_color=self.label_color).pack(pady=5)
        self.password_entry = ctk.CTkEntry(self.login_frame, width=300, show="*")
        self.password_entry.pack(pady=5)

        ctk.CTkButton(
            self.login_frame,
            text="Forgot Password?",
            font=self.button_font,
            fg_color=self.default_bg,
            text_color=self.label_color,
            command=self.show_forgot_password_frame
        ).pack(padx=5,pady=5)

        ctk.CTkButton(
            self.login_frame,
            text="Login",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=self.login
        ).pack(pady=10)
        
        ctk.CTkButton(
            self.login_frame,
            text="Back",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.create_main_window(), self.login_frame.destroy()]
            
        ).pack(pady=10)
        
    def show_forgot_password_frame(self):
        if hasattr(self, 'login_frame'):
            self.login_frame.pack_forget()

        self.forgot_password_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.forgot_password_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.forgot_password_frame, 
            text="Forgot Password", 
            font=self.title_font, 
            text_color=self.label_color
        ).pack(pady=20)

        ctk.CTkLabel(
            self.forgot_password_frame, 
            text="Enter your email:", 
            font=self.label_font, 
            text_color=self.label_color
        ).pack(pady=15)

        self.forgot_email_entry = ctk.CTkEntry(self.forgot_password_frame, width=300)
        self.forgot_email_entry.pack(pady=5)

        self.otp_entry = None
        self.new_password_entry = None
        ctk.CTkButton(
            self.forgot_password_frame,
            text="Send OTP",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=self.send_otp
        ).pack(pady=10)
         
        self.loading_label = ctk.CTkLabel( 
            self.forgot_password_frame, 
            text="", 
            font=self.button_font, 
            text_color=self.label_color 
        ) 
        self.loading_label.pack(pady=15)

    def send_otp(self):
        email = self.forgot_email_entry.get()
        if not email:
            messagebox.showerror("Error", "Please enter your email address.")
            return

        # Show loading animation 
        self.loading_label.configure(text="Sending mail, please wait...") 
        self.root.update_idletasks() # Force update to display loading text

        response = requests.post("http://localhost/SenseVision_Application/php/forgot_password.php", data={
            'email': email
        })
        try:
            result = response.json()
            if result.get("success"):
                messagebox.showinfo("Success", "OTP sent to your email.")
                self.display_otp_entry(email)
            else:
                messagebox.showerror("Error", result.get("message", "Failed to send OTP."))
        except ValueError:
            messagebox.showerror("Error", "Invalid response from server.")
        finally: 
            # Hide loading animation 
            self.loading_label.configure(text="")

    def display_otp_entry(self, email):
        if self.otp_entry:
            self.otp_entry.destroy()
        ctk.CTkLabel(
            self.forgot_password_frame, 
            text="Enter OTP:", 
            font=self.label_font, 
            text_color=self.label_color
        ).pack(pady=5)
        self.otp_entry = ctk.CTkEntry(self.forgot_password_frame, width=300)
        self.otp_entry.pack(pady=5)

        ctk.CTkButton(
            self.forgot_password_frame,
            text="Verify OTP",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=lambda: self.verify_otp(email)
        ).pack(pady=10)

    def verify_otp(self, email):
        otp = self.otp_entry.get()
        if not otp:
            messagebox.showerror("Error", "Please enter the OTP.")
            return

        response = requests.post("http://localhost/SenseVision_Application/php/verify_otp.php", data={
            'email': email,
            'otp': otp,
        })
        try:
            result = response.json()
            if result.get("success"):
                messagebox.showinfo("Success", "OTP verified successfully.")
                self.display_new_password_entry(email, otp)
            else:
                messagebox.showerror("Error", result.get("message", "Invalid or expired OTP."))
        except ValueError:
            messagebox.showerror("Error", "Invalid response from server.")

    def display_new_password_entry(self, email, otp):
        if self.new_password_entry:
            self.new_password_entry.destroy()
        ctk.CTkLabel(
            self.forgot_password_frame, 
            text="Enter New Password:", 
            font=self.label_font, 
            text_color=self.label_color
        ).pack(pady=5)
        self.new_password_entry = ctk.CTkEntry(self.forgot_password_frame, width=300, show="*")
        self.new_password_entry.pack(pady=5)

        ctk.CTkButton(
            self.forgot_password_frame,
            text="Reset Password",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=lambda: self.reset_password(email, otp)
        ).pack(pady=10)

    def reset_password(self, email, otp, new_password=None):
        new_password = self.new_password_entry.get()
        if not new_password:
            messagebox.showerror("Error", "Please enter the new password.")
            return

        response = requests.post("http://localhost/SenseVision_Application/php/reset_password.php", data={
            'email': email,
            'otp': otp,
            'new_password': new_password
        })
        try:
            result = response.json()
            if result.get("success"):
                messagebox.showinfo("Success", "Password reset successfully!")
                self.forgot_password_frame.destroy()
                self.login_frame.pack(fill="both", expand=True)
            else:
                messagebox.showerror("Error", result.get("message", "Failed to reset password."))
        except ValueError:
            messagebox.showerror("Error", "Invalid response from server.")
    def show_register_frame(self):
        if hasattr(self, 'main_frame'):
            self.main_frame.pack_forget()
        if hasattr(self, 'login_frame'):
            self.login_frame.pack_forget()

        self.register_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.register_frame.pack(fill="both", expand=True)

        ctk.CTkLabel(self.register_frame, text="Register", font=self.title_font, text_color=self.label_color).pack(pady=20)
        ctk.CTkLabel(self.register_frame, text="Name", font=self.label_font, text_color=self.label_color).pack(pady=5)
        self.name_entry = ctk.CTkEntry(self.register_frame, width=300)
        self.name_entry.pack(pady=5)
        ctk.CTkLabel(self.register_frame, text="Phone", font=self.label_font, text_color=self.label_color).pack(pady=5)
        self.phone_entry = ctk.CTkEntry(self.register_frame, width=300)
        self.phone_entry.pack(pady=5)
        ctk.CTkLabel(self.register_frame, text="Email", font=self.label_font, text_color=self.label_color).pack(pady=5)
        self.register_email_entry = ctk.CTkEntry(self.register_frame, width=300)
        self.register_email_entry.pack(pady=5)
        ctk.CTkLabel(self.register_frame, text="Password", font=self.label_font, text_color=self.label_color).pack(pady=5)
        self.register_password_entry = ctk.CTkEntry(self.register_frame, width=300, show="*")
        self.register_password_entry.pack(pady=5)

        ctk.CTkButton(
            self.register_frame,
            text="Register",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=self.register
        ).pack(pady=10)
        ctk.CTkButton(
            self.register_frame,
            text="Back",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.create_main_window(), self.register_frame.destroy()]
        ).pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        response = requests.post("http://localhost/SenseVision_Application/php/login.php", data={
            'email': email,
            'password': password
        })
        try:
            result = response.json()  # Attempt to decode JSON
        except ValueError:
            messagebox.showerror("Error", "Invalid response from server: " + response.text)
            return  # Exit the method if JSON decoding fails

        if result.get("success"):
            messagebox.showinfo("Login", "Login successful!")
            user_id = result.get('user_id')  # Safely access user_id
            if user_id is not None:
                self.user_id = user_id  # Store user ID in the instance variable
                self.login_frame.destroy()
                self.show_main_app(result['user'])
            else:
                messagebox.showerror("Login Error", "User  ID not found in response.")
        else:
            messagebox.showerror("Login Error", result.get("message", "Invalid credentials"))

    def register(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.register_email_entry.get()
        password = self.register_password_entry.get()

        response = requests.post("http://localhost/SenseVision_Application/php/register.php", data={
            'name': name,
            'phone': phone,
            'email': email,
            'password': password
        })

        result = response.json()
        if result.get("success"):
            messagebox.showinfo("Success", "Registration Successful!")
            self.register_frame.destroy()
            self.show_login_frame()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def show_main_app(self, user):
        self.main_frame.pack_forget()

        self.home_page_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.home_page_frame.pack(fill="both", expand=True)

        menu_button = ctk.CTkButton(
            self.home_page_frame,
            text="\u2630",
            font=("Helvetica", 16),
            fg_color=self.button_color,
            text_color="white",
            width=40,
            height=40,
            command=lambda: self.toggle_menu(user)
        )
        menu_button.pack(side="left", padx=10, pady=10, anchor="nw")

        ctk.CTkButton(
            self.home_page_frame,
            text="Object Detection",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda user=user: [self.show_object_detection(user),self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)

        ctk.CTkButton(
            self.home_page_frame,
            text="Emotion Detection",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda user=user:[self.show_Emotion_Detection(user),self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)

    def show_Emotion_Detection(self,user):
        self.home_page_frame.pack_forget()

        self.Emotion_Detection_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.Emotion_Detection_frame.pack(fill="both", expand=True)

        menu_button = ctk.CTkButton(
            self.Emotion_Detection_frame,
            text="\u2630",
            font=("Helvetica", 16),
            fg_color=self.button_color,
            text_color="white",
            width=40,
            height=40,
            command=lambda: self.toggle_menu(user)
        )
        menu_button.pack(side="left", padx=10, pady=10, anchor="nw")

        ctk.CTkButton(
            self.Emotion_Detection_frame,
            text="Emotion Detection(image)",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.run_image_emotion_detection(), self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)

        ctk.CTkButton(
            self.Emotion_Detection_frame,
            text="Emotion Detection(video)",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.run_video_emotion_detection(),self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)

        ctk.CTkButton(
            self.Emotion_Detection_frame,
            text="Emotion Detection(webcam)",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.run_cam_emotion_detection(),self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)

        ctk.CTkButton(
            self.Emotion_Detection_frame,
            text="Back",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.show_main_app(user), self.Emotion_Detection_frame.destroy(),(self.history_frame.destroy() if hasattr(self, 'history_frame') else None)]
        ).pack(pady=10)

    def show_object_detection(self,user):
        self.home_page_frame.pack_forget()

        self.object_detection_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.object_detection_frame.pack(fill="both", expand=True)

        menu_button = ctk.CTkButton(
            self.object_detection_frame,
            text="\u2630",
            font=("Helvetica", 16),
            fg_color=self.button_color,
            text_color="white",
            width=40,
            height=40,
            command=lambda: self.toggle_menu(user)
        )
        menu_button.pack(side="left", padx=10, pady=10, anchor="nw")

        ctk.CTkButton(
            self.object_detection_frame,
            text="Image Detection",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.run_image_detection(),self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)
        ctk.CTkButton(
            self.object_detection_frame,
            text="Video Detection",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda:[self.run_video_detection(),self.history_frame.destroy() if hasattr(self, 'history_frame') else None]
        ).pack(pady=20)
        ctk.CTkButton(
            self.object_detection_frame,
            text="Camera Detection",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda:[self.run_camera_detection(),self.history_frame.destroy() if hasattr(self, 'history_frame') else None] 
        ).pack(pady=20)

        ctk.CTkButton(
            self.object_detection_frame,
            text="Back",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.show_main_app(user), self.object_detection_frame.destroy(),(self.history_frame.destroy() if hasattr(self, 'history_frame') else None)]
        ).pack(pady=10)


    def toggle_menu(self, user):

        menu = ctk.CTkToplevel(self.root)
        menu.geometry("350x650")
        menu.title("Menu")
        menu.configure(fg_color=self.default_bg)

        menu.attributes('-topmost', True)

        ctk.CTkLabel(
            menu,
            text=f"Name: {user['name']}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.label_color
        ).pack(padx=10, pady=10)
        ctk.CTkLabel(
            menu,
            text=f"Email: {user['email']}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=self.label_color
        ).pack(pady=10)

        ctk.CTkButton(
            menu,
            text="History",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [menu.destroy(),self.history_frame.destroy() if hasattr(self, 'history_frame') else None, self.show_history_frame()]
        ).pack(pady=20)
        
        ctk.CTkButton(
            menu,
            text="Logout",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color=self.button_color,
            text_color="white",
            command=lambda: [self.destroy_main_app(),self.create_main_window(), menu.destroy(),(self.history_frame.destroy() if hasattr(self, 'history_frame') else None),(self.Emotion_Detection_frame.destroy() if hasattr(self, 'Emotion_Detection_frame') else None),(self.object_detection_frame.destroy() if hasattr(self, 'object_detection_frame') else None)]
        ).pack(pady=20)
    
    def show_history_frame(self):
        self.history_frame = ctk.CTkFrame(self.root, fg_color=self.default_bg)
        self.history_frame.pack(fill="both", expand=True)


        ctk.CTkLabel(self.history_frame, text="Upload History", font=self.title_font, text_color=self.label_color).pack(pady=20, padx=20, anchor="nw")

        self.search_entry = ctk.CTkEntry(self.history_frame, placeholder_text="Search history...", width=300)
        self.search_entry.pack(pady=10, padx=20)

        # Create a frame for the history items
        self.history_list_frame = ctk.CTkFrame(self.history_frame, fg_color=self.default_bg)
        self.history_list_frame.pack(fill="both", expand=True)

        self.search_entry.bind("<KeyRelease>", self.filter_history)

        # Create a canvas to allow scrolling
        self.canvas = ctk.CTkCanvas(self.history_list_frame, bg=self.default_bg)
        self.scrollbar = ctk.CTkScrollbar(self.history_list_frame, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas, fg_color=self.default_bg)

        # Bind the configure event to update the scroll region
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # Create a window in the canvas to hold the scrollable frame
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Pack the canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Link the scrollbar to the canvas
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.load_history()

        # Button to run detection on selected file
        ctk.CTkButton(
            self.history_frame,
            text="Run Detection",
            font=self.button_font,
            fg_color=self.button_color,
            text_color="white",
            command=self.run_detection_on_selected_file
        ).pack(pady=10)

    def load_history(self):
        user_id = getattr(self, 'user_id', None)  # Get the user ID from session or context

        if not self.user_id:  # If user_id is None or invalid
            messagebox.showerror("Error", "User not logged in.")
            return

        # Use a session for maintaining cookies if required
        session = requests.Session()
        response = session.post(
            "http://localhost/SenseVision_Application/php/history.php",
            data={'user_id': user_id}
        )

        try:
            result = response.json()
            if result.get("success"):
                # Clear existing history items from the scrollable frame
                for widget in self.scrollable_frame.winfo_children():
                    widget.destroy()  # Destroy existing widgets in the scrollable frame

                for record in result['history']:
                    file_info = f"{record['file_name']} ({record['file_type']})"
                    # Create a custom frame for each history item
                    history_item = ctk.CTkFrame(self.scrollable_frame, fg_color=self.button_color)
                    history_item.pack(pady=5, padx=10, fill="x")

                    # Add an icon or label
                    icon_label = ctk.CTkLabel(history_item, text="📁", font=ctk.CTkFont(size=30, weight="bold"), text_color=self.label_color)
                    icon_label.pack(side="left", padx=5)

                    # Add the file info label
                    file_label = ctk.CTkLabel(history_item, text=file_info, font=ctk.CTkFont(size=10, weight="bold"), text_color=self.label_color)
                    file_label.pack(side="left", padx=5)

                    history_item.bind("<Button-1>", lambda event, file_name=record['file_name'], item=history_item: self.select_history_item(file_name, item))

                    
            else:
                messagebox.showerror("Error", result.get("message", "Could not fetch history"))
        except ValueError:
            messagebox.showerror("Error", "Invalid response from server.")

    def select_history_item(self, file_name, history_item):
        # Reset the background color of all items
        for widget in self.scrollable_frame.winfo_children():
            widget.configure(fg_color=self.button_color)  # Reset color

        # Highlight the selected item
        history_item.configure(fg_color="#44475a")  # Change to a different color for selection
        self.selected_file_name = file_name  # Store the selected file name
        messagebox.showinfo("Selected File", f"You selected: {file_name}")  # Optional: Show a message


    def filter_history(self, event):
        search_query = self.search_entry.get().lower()  # Get the search query
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()  # Clear existing items

        # Load the full history again
        user_id = getattr(self, 'user_id', None)
        if not user_id:
            messagebox.showerror("Error", "User  not logged in.")
            return

        session = requests.Session()
        response = session.post(
            "http://localhost/SenseVision_Application/php/history.php",
            data={'user_id': user_id}
        )

        try:
            result = response.json()
            if result.get("success"):
                for record in result['history']:
                    file_info = f"{record['file_name']} ({record['file_type']})"
                    # Check if the search query is in the file_info
                    if search_query in file_info.lower():
                        # Create a custom frame for each matching history item
                        history_item = ctk.CTkFrame(self.scrollable_frame, fg_color=self.button_color)
                        history_item.pack(pady=5, padx=10, fill="x")

                        # Add an icon or label
                        icon_label = ctk.CTkLabel(history_item, text="📁", font=self.label_font, text_color=self.label_color)
                        icon_label.pack(side="left", padx=5)

                        # Add the file info label
                        file_label = ctk.CTkLabel(history_item, text=file_info, font=self.label_font, text_color=self.label_color)
                        file_label.pack(side="left", padx=5)

                        history_item.bind("<Button-1>", lambda event, file_name=record['file_name'], item=history_item: self.select_history_item(file_name, item))
            else:
                messagebox.showerror("Error", result.get("message", "Could not fetch history"))
        except ValueError:
            messagebox.showerror("Error", "Invalid response from server.")

            
    def run_detection_on_selected_file(self):
        if not hasattr(self, 'selected_file_name'):
            messagebox.showerror("Error", "No file selected!")
            return

        file_name = self.selected_file_name  # Get the selected file name
        file_path = os.path.join('./uploads', file_name)  # Construct the file path

        # Determine the file extension to check if it's an image or video
        file_extension = os.path.splitext(file_name)[1].lower()  # Get the file extension

        try:
            if file_extension in ['.jpg', '.jpeg', '.png', '.mp4', '.avi', '.mov']:
                # Ask the user whether to perform emotion or object detection
                choice = messagebox.askquestion(
                    "Detection Type",
                    "Do you want to perform Emotion Detection? (No for Object Detection)")

                if choice == 'yes':  # Emotion Detection
                    if file_extension in ['.jpg', '.jpeg', '.png']:  # Image file types
                        process = subprocess.Popen(
                            [sys.executable, "emotionpy/img_emotion.py", "-i", file_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                    elif file_extension in ['.mp4', '.avi', '.mov']:  # Video file types
                        process = subprocess.Popen(
                            [sys.executable, "emotionpy/video_emotion.py", "-v", file_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                    else:
                        messagebox.showerror("Error", "Unsupported file type for Emotion Detection!")
                        return

                else:  # Object Detection
                    if file_extension in ['.jpg', '.jpeg', '.png']:  # Image file types
                        process = subprocess.Popen(
                            ["python", "python/image_object_detection.py", "-i", file_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                    elif file_extension in ['.mp4', '.avi', '.mov']:  # Video file types
                        process = subprocess.Popen(
                            ["python", "python/video_object_detection.py", "-v", file_path],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE
                        )
                    else:
                        messagebox.showerror("Error", "Unsupported file type for Object Detection!")
                        return

                stdout, stderr = process.communicate()  # Capture output and errors
                if process.returncode != 0:
                    raise Exception(f"Error in detection process: {stderr.decode('utf-8')}")

                messagebox.showinfo("Success", f"Detection completed for {file_name}")

            else:
                messagebox.showerror("Error", "Unsupported file type!")

        except Exception as e:
            messagebox.showerror("Error", str(e))
  # Show any errors that occurred during the process
    def run_image_detection(self):
        # Ask the user whether to use a sample or upload their own file
        choice = messagebox.askquestion(
            "Select Image",
            "Do you want to use a sample image or upload your own? (Yes for sample, No to upload)"
        )

        if choice == 'yes':
            image_path = 'samples/sample.jpg'  # Use the predefined sample image
        else:
            image_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
            )
            if not image_path:
                messagebox.showerror("Error", "No file selected!")
                return

        # Ensure uploads folder exists
        uploads_folder = './uploads'
        os.makedirs(uploads_folder, exist_ok=True)

        # Save the uploaded or selected image in the uploads folder
        file_name = os.path.basename(image_path)
        save_path = os.path.join(uploads_folder, file_name)

        try:
            # Copy image to uploads folder using shutil
            shutil.copy2(image_path, save_path)
            
            # Call the detection script with the uploaded/selected image
            process = subprocess.Popen(
                ["python", "python/image_object_detection.py", "-i", save_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            stdout, stderr = process.communicate()  # Capture output and errors
            if process.returncode != 0:
                raise Exception(f"Error in detection process: {stderr.decode('utf-8')}")

            # Assuming self.user_id is defined elsewhere in your class
            user_id = getattr(self, 'user_id', None)
            if not user_id:
                raise Exception("User ID is not defined")

            # Upload the file
            self.upload_file(save_path, user_id, 'image')

            messagebox.showinfo("Success", f"Image detection completed for {file_name}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error during image detection: {e}")

    def run_image_emotion_detection(self):
        choice = messagebox.askquestion(
            "Select Image",
            "Do you want to use a sample image or upload your own? (Yes for sample, No to upload)"
        )

        if choice == 'yes':
            image_path = 'samples/sample1.jpg'  # Use the predefined sample image
        else:
            image_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.jpg;*.jpeg;*.png")]
            )
            if not image_path:
                messagebox.showerror("Error", "No file selected!")
                return

        # Ensure uploads folder exists
        uploads_folder = './uploads'
        os.makedirs(uploads_folder, exist_ok=True)

        # Save the uploaded or selected image in the uploads folder
        file_name = os.path.basename(image_path)
        save_path = os.path.join(uploads_folder, file_name)

        try:
            # Copy image to uploads folder using shutil
            shutil.copy2(image_path, save_path)
            
            # Call the detection script with the uploaded/selected image
            process = subprocess.Popen(

                [sys.executable, "emotionpy/img_emotion.py", "-i", save_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            stdout, stderr = process.communicate()  # Capture output and errors
            if process.returncode != 0:
                raise Exception(f"Error in detection process: {stderr.decode('utf-8')}")

            # Assuming self.user_id is defined elsewhere in your class
            user_id = getattr(self, 'user_id', None)
            if not user_id:
                raise Exception("User ID is not defined")

            # Upload the file
            self.upload_file(save_path, user_id, 'image')

            messagebox.showinfo("Success", f"Image detection completed for {file_name}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error during image detection: {e}")

    def upload_file(self, file_path, user_id, file_type):
        url = 'http://localhost/SenseVision_Application/php/upload.php'
        files = {'file': open(file_path, 'rb')}
        data = {'user_id': user_id, 'file_type': file_type}
    
        try:
            response = requests.post(url, files=files, data=data)
            result = response.json()  # Parse the JSON response
            if not result.get("success"):
                raise Exception(result.get("message", "Unknown error occurred"))
            print("File upload successful:", result)
        except Exception as e:
            print(f"Error during file upload: {e}")
        finally:
            files['file'].close()  # Ensure the file is closed after upload

    def run_video_detection(self):
        # Ask the user whether to use a sample or upload their own file
        choice = messagebox.askquestion(
            "Select Video",
            "Do you want to use a sample video or upload your own? (Yes for sample, No to upload)"
        )

        if choice == 'yes':
            video_path = 'samples/sample_video.mp4'  # Use the predefined sample video
        else:
            video_path = filedialog.askopenfilename(
                filetypes=[("Video files", "*.mp4;*.avi;*.mov")]
            )
            if not video_path:
                messagebox.showerror("Error", "No file selected!")
                return

        # Ensure uploads folder exists
        uploads_folder = './uploads'
        os.makedirs(uploads_folder, exist_ok=True)

        # Save the uploaded or selected video in the uploads folder
        file_name = os.path.basename(video_path)
        save_path = os.path.join(uploads_folder, file_name)

        try:
            # Copy video to uploads folder using shutil
            shutil.copy2(video_path, save_path)

            # Call the detection script with the uploaded/selected video
            process = subprocess.Popen(
                ["python", "python/video_object_detection.py", "-v", save_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            stdout, stderr = process.communicate()  # Capture output and errors
            if process.returncode != 0:
                raise Exception(f"Error in detection process: {stderr.decode('utf-8')}")
            
            user_id = self.user_id  # Get the current user's ID (assuming it's stored in self.user_id)
            self.upload_file(save_path, user_id, 'video')

            messagebox.showinfo("Success", f"Video detection completed for {file_name}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error during video detection: {e}")   
    def run_video_emotion_detection(self):
        # Ask the user whether to use a sample or upload their own file
        choice = messagebox.askquestion(
            "Select Video",
            "Do you want to use a sample video or upload your own? (Yes for sample, No to upload)"
        )

        if choice == 'yes':
            video_path = 'samples/sample_video1.mp4'  # Use the predefined sample video
        else:
            video_path = filedialog.askopenfilename(
                filetypes=[("Video files", "*.mp4;*.avi;*.mov")]
            )
            if not video_path:
                messagebox.showerror("Error", "No file selected!")
                return

        # Ensure uploads folder exists
        uploads_folder = './uploads'
        os.makedirs(uploads_folder, exist_ok=True)

        # Save the uploaded or selected video in the uploads folder
        file_name = os.path.basename(video_path)
        save_path = os.path.join(uploads_folder, file_name)

        try:
            # Copy video to uploads folder using shutil
            shutil.copy2(video_path, save_path)

            # Call the detection script with the uploaded/selected video
            process = subprocess.Popen(
                [sys.executable, "emotionpy/video_emotion.py", "-v", save_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE  
            )
            
            stdout, stderr = process.communicate()  # Capture output and errors
            if process.returncode != 0:
                raise Exception(f"Error in detection process: {stderr.decode('utf-8')}")
            
            user_id = self.user_id  # Get the current user's ID (assuming it's stored in self.user_id)
            self.upload_file(save_path, user_id, 'video')


            messagebox.showinfo("Success", f"Video emotion detection completed for {file_name}")
        
        except Exception as e:
            messagebox.showerror("Error", f"Error during video emotion detection: {e}")
            
    def run_camera_detection(self):
        result = messagebox.askquestion("Confirmation", "Are you sure you want to start camera detection?")
        if result == 'yes':
            try:
                # Start the subprocess for camera detection
                process = subprocess.Popen(["python", "python/cam_object_detection.py"])
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Error running camera detection: {e}")

    def run_cam_emotion_detection(self):
        result = messagebox.askquestion("Confirmation", "Are you sure you want to start camera emotion detection?")
        if result == 'yes':
            try:
                # Start the subprocess for camera emotion detection
                process = subprocess.Popen([sys.executable, "emotionpy/cam_emotion.py"])
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Error running camera emotion detection: {e}")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ObjectDetectionApp(root)
    root.mainloop()