import flet as ft
from flet import (
   AppBar,Page,Text,colors,ResponsiveRow,Column,Container,Image,Row,alignment,TextField
   ,Border,View,ElevatedButton,margin,CrossAxisAlignment,MainAxisAlignment,padding,Divider
)
import sqlite3



def sign_up(r_username, r_department, r_semester, r_pass, r_email, page):
   
   if r_username.value == "" or r_department.value == "" or r_semester.value == "" or r_email.value == "" or r_pass.value == "":
      print("Error")
      r_username.border_color = "RED"
      r_department.border_color = "RED"
      r_semester.border_color = "RED"
      r_email.border_color = "RED"
      r_pass.border_color = "RED"
      page.update()
      return 

   conn = sqlite3.connect("user_data.db")
   cursor = conn.cursor()

   cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        department TEXT,
        semester TEXT,
        password TEXT,
        email TEXT
    )
""")
   conn.commit()
   username = r_username.value  
   department = r_department.value
   semester = r_semester.value
   password = r_pass.value
   email = r_email.value

   cursor.execute("""
        INSERT INTO users (username, department, semester, password, email)
        VALUES (?, ?, ?, ?, ?)
    """, (username, department, semester, password, email))

   conn.commit()  # Commit the changes to the database
   print("Added")
   conn.close()  # Close the database connection
   r_username.border_color = '#b48811'
   r_department.border_color = '#b48811'
   r_semester.border_color = '#b48811'
   r_email.border_color = '#b48811'
   r_pass.border_color = '#b48811'
   r_username.value = ""
   r_department.value = ""
   r_email.value = ""
   r_semester.value = ""
   r_pass.value = ""
   page.update()


 #User Data
d_username = ft.TextField(label="Name",border_color='#b48811',color='WHite',width=450)
d_department = ft.TextField(label="Department",border_color='#b48811',color='WHite',width=450)
d_semester = ft.TextField(label="Semester",border_color='#b48811',color='WHite',width=450)
d_email = ft.TextField(label="Email",border_color='#b48811',color='WHite',width=450)
d_pass = ft.TextField(label="Password",border_color='#b48811',color='WHite',password=True,can_reveal_password=True,width=450)
current_email = ft.TextField(label="C_Email",border_color='#b48811',color='WHite',width=450)


import sqlite3

def update():
   conn = sqlite3.connect("user_data.db")
   cursor = conn.cursor()

    # Update the user's profile with new data
   cursor.execute("""
        UPDATE users
        SET username = ?, department = ?, semester = ?, password = ?, email = ?
        WHERE email = ?          
    """, (d_username.value, d_department.value, d_semester.value, d_pass.value, d_email.value,current_email.value))

   conn.commit()  # Commit the changes to the database
   print("Profile Updated")
  

def login(l_email, l_pass, page):
    if l_email.value == "" or l_pass.value == "":
        print("Error")
        l_email.border_color = "RED"
        l_pass.border_color = "RED"
        page.update()
        return
    
    conn = sqlite3.connect("user_data.db")
    cursor = conn.cursor()

    # Check if the provided email and password match a user in the database
    cursor.execute("""
        SELECT username, email, semester, department,password FROM users
        WHERE email = ? AND password = ?
    """, (l_email.value, l_pass.value))

    user = cursor.fetchone()

    if user:
        username, email, semester, department,password = user
        print("Welcome, " + username)  # Display a welcome message with the username
        # You can implement further actions for successful login here
        d_username.value = username
        d_email.value = email
        d_pass.value = password
        d_semester.value = semester
        d_department.value = department
        current_email.value = email
        page.go('/next')
    else:
        print("Invalid email or password")
        l_email.border_color = "RED"
        l_pass.border_color = "RED"
        page.update()
        return
    
    conn.close()

def post(post1,page):

   print("Success")
   page.add(ft.Text(f"Current route: {page.route}"))
   page.views[-1].controls.append(ft.Text(f"Current route: {page.route}"))
   print(post1.value)
   page.update()

def main(page: ft.Page):
 page.title = "Socio-Link"
 page.window_width = 390 
 page.window_height = 844
 page.horizontal_alignment = 'center'
 page.vertical_alignment = 'center'
  
 #Register User
 div = ft.Divider(height=9, thickness=12,color="Black")
 r_username = ft.TextField(label="Name",border_color='#b48811',color='WHite',width=450)
 r_department = ft.TextField(label="Department",border_color='#b48811',color='WHite',width=450)
 r_semester = ft.TextField(label="Semester",border_color='#b48811',color='WHite',width=450)
 r_email = ft.TextField(label="Email",border_color='#b48811',color='WHite',width=450)
 r_pass = ft.TextField(label="Password",border_color='#b48811',color='WHite',password=True,can_reveal_password=True,width=450)
 r_button = ft.ElevatedButton(text="Sign Up",bgcolor='#b48811',color='White',on_click=lambda _: sign_up(r_username,r_department,r_semester,r_pass,r_email,page))
 
 #post
 post1 = ft.TextField(label="Whats In Your Mind !",border_color='#b48811',color='WHite',width=450)
 post_button = ft.ElevatedButton(text="Publish",bgcolor='#b48811',color='White',on_click=lambda _: post(post1,page)) 
 
 #User Data Update
 update_button = ft.ElevatedButton(text="Update Record",bgcolor='#b48811',color='White',on_click=lambda _: update(page))

 #LogIn User
 l_email = ft.TextField(label="Email",border_color='#b48811',color='WHite',width=450)
 l_pass = ft.TextField(label="Password",border_color='#b48811',color='WHite',password=True,can_reveal_password=True,width=450)
 l_button = ft.ElevatedButton(text="LogIn",bgcolor='#b48811',color='White',on_click=lambda _: login(l_email,l_pass,page))
 
 def route_change(route):
  if page.route == '/':
   page.views.clear()
   
   page.views.append(    
   View (
   route='/',
   controls=[
   ft.Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Sign Up ",
                icon = ft.icons.PERSON_PIN,
                content=ft.Column(
                [ 
                ft.Image(
                src=f"https://miflexwave.com/wp-content/uploads/2023/09/cropped-WhatsApp_Image_2023-09-07_at_4.35.36_AM-removebg-preview-1.png",
                width=300,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                ), 
                div,   
                r_username,
                div,
                r_department,
                div,
                r_semester,
                div,
                r_email,
                div,
                r_pass,
                div,  
                r_button,
                div,
                ft.Text(value="Developed By Socio-Link",size=14,color='#b48811'),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                
                ),
                
                
            ),
            ft.Tab(
                text="LogIn ",
                icon=ft.icons.PERSON_2_ROUNDED,
                content=ft.Column(
                [
                ft.Image(
                src=f"https://miflexwave.com/wp-content/uploads/2023/09/cropped-WhatsApp_Image_2023-09-07_at_4.35.36_AM-removebg-preview-1.png",
                width=300,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                ),
                div,       
                l_email,
                div,
                l_pass,
                div,
                l_button,
                div,
                ft.Text(value="Developed By Socio-Link",size=14,color='#b48811'),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
            ft.Tab(
                #text="About Us ",
                icon=ft.icons.APP_REGISTRATION,
                content=ft.Column(
                [
                ft.Divider(height=39, thickness=4), 
                ft.Text(value="About Us",size=30),
                ft.Text(value="This Is U-I BASES WEB APPLICATION DESIGNED IN PYTHON \n\nWe'd love to hear your feedback, suggestions, or any questions you may have. Feel free to reach out to us at msmtimes21@gmail.com  \n\n> COPYRIGHT @ MUDDASSIR FAROOQ",text_align='justify'),
                ],
                )

            ),
            
        ],
        expand=1,
    )
   
   ],
   padding=30,
   bgcolor='Black',
   scroll=True
   )
  
  )


  elif page.route == '/next':
   page.views.clear()
   
   page.views.append(    
   View (
   route='/',
   controls=[
   ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Profile ",
                icon = ft.icons.PERSON_PIN,
                content=ft.Column(
                [ 
                ft.Image(
                src=f"https://miflexwave.com/wp-content/uploads/2023/09/cropped-WhatsApp_Image_2023-09-07_at_4.35.36_AM-removebg-preview-1.png",
                width=300,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                ), 
                div,   
                d_username,
                div,
                d_department,
                div,
                d_semester,
                div,
                d_email,
                div,
                d_pass,
                div,
                update_button,
                div,     
                ft.Text(value="Developed By Socio-Link",size=14,color='#b48811'),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                
                ),
                
                
            ),
            ft.Tab(
                text="Home ",
                icon=ft.icons.PERSON_2_ROUNDED,
                content=ft.Column(
                [
                ft.Image(
                src=f"https://miflexwave.com/wp-content/uploads/2023/09/cropped-WhatsApp_Image_2023-09-07_at_4.35.36_AM-removebg-preview-1.png",
                width=300,
                height=100,
                fit=ft.ImageFit.CONTAIN,
                ),
                div,
                post1,
                div,
                post_button,
                div,
                ft.Text(value="Developed By Socio-Link",size=14,color='#b48811'),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER               
                )
            ),
            
        ],
        expand=1,
    )
   
   ],
   padding=30,
   bgcolor='Black',
   scroll=True
   )
  
  )
 page.update()
 
 def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)
 
 page.on_route_change = route_change
 page.on_view_pop = view_pop
 page.go(page.route)
 
ft.app(target=main)
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)
