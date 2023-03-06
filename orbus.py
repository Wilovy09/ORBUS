import os

banner = """
░█████╗░██████╗░██████╗░██╗░░░██╗░██████╗
██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
██║░░██║██████╔╝██████╦╝██║░░░██║╚█████╗░
██║░░██║██╔══██╗██╔══██╗██║░░░██║░╚═══██╗
╚█████╔╝██║░░██║██████╦╝╚██████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═════╝░░╚═════╝░╚═════╝░
"""

def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

# ! MAIN
def main():
    borrarPantalla()
    print(banner)
    print("\n")
    print("En que quieres iniciar tu proyecto?")
    print("\n")
    print("    1 - Flet")
    print("\n")
    opcion = input("    >> ")

    if opcion == "1":
        borrarPantalla()
        print(banner)
        print("\n")
        print("Ruta donde se creara el proyecto (se recomienda dejar ' \ ' al final)")
        print(r"Ejemplo: C:\Users\User\Desktop\   ")
        ruta = input("\n>> ")
        
        if os.path.exists(ruta) == False:
            print("La ruta no existe o es incorrecta")
            exit()
        else:
            print("La ruta si existe")
            print("\n")
            nombre = input("Nombre del proyecto: ")
            
            os.chdir(ruta)
            os.mkdir(nombre)
            
            os.chdir(nombre)
            main = open("main.py", "w")
            main.write("""
import flet as ft
from flet import *
from pages.index import _view_ as v1
from pages.about import _view_ as v2
from pages.contact import _view_ as v3

def main(page: Page):

    page.theme_mode = "dark"
    page.title = 'Document' 

    my_music = v1()
    playlists = v2()
    contact = v3()
    
    def route_change(route):
        page.views.clear()
        if page.route == '/playlists':
            page.views.append(playlists)
        if page.route == '/contact':
            page.views.append(contact)
        if page.route == '/my_music':
            page.views.append(my_music)
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)


    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(playlists)
    page.views.append(contact)
    page.views.append(my_music)
    
    page.update()

ft.app(target=main, assets_dir='assets')
# ft.app(target=main, assets_dir='assets', port=5000, view=ft.WEB_BROWSER)
            """)
            main.close()
            
            os.mkdir("pages")
            os.chdir("pages")
            
            index = open("index.py", "w")
            index.write("""
import flet as ft
from flet import *

def _view_():
    return View(
        '/my_music',
        controls=[
            Column(
                controls=[
                    Row(
                        controls=[
                            FilledButton(
                                text='Index',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/my_music'),
                            ),
                            FilledButton(
                                text='About',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/playlists'),
                            ),
                            FilledButton(
                                text='Contact',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/contact'),
                            ),
                        ]
                    ),
                    ft.Divider(thickness=1),
                    # MAIN CONTENT
                ]
            )
        ],
    )
            """)
            index.close()
            
            about = open("about.py", "w")
            about.write("""
import flet as ft
from flet import *

import flet as ft
from flet import *

def _view_():
    return View(
        '/about',
        controls=[
            Column(
                controls=[
                    Row(
                        controls=[
                            FilledButton(
                                text='Index',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/index'),
                            ),
                            FilledButton(
                                text='About',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/About'),
                            ),
                            FilledButton(
                                text='Contact',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/contact'),
                            ),
                        ]
                    ),
                    ft.Divider(thickness=1),
                    # MAIN CONTENT
                ]
            )
        ],
    )
            """)
            about.close()

            contact = open("contact.py", "w")
            contact.write("""
import flet as ft
from flet import *

def _view_():
    return View(
        '/contact',
        controls=[
            Column(
                controls=[
                    Row(
                        controls=[
                            FilledButton(
                                text='Index',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/index'),
                            ),
                            FilledButton(
                                text='About',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/about'),
                            ),
                            FilledButton(
                                text='Contact',
                                width=100,
                                height=40,
                                on_click=lambda e: e.page.go('/contact'),
                            ),
                        ]
                    ),
                    ft.Divider(thickness=1),
                    # MAIN CONTENT
                ]
            )
        ],
    )
            """)
            contact.close()

            borrarPantalla()
            print(banner)
            print("\n")
            print("Proyecto creado con exito! \n")
            print("Nombre del proyecto: " + nombre + "\n")
            print("Ruta del proyecto: " + ruta + nombre + "\n")
            print("Para iniciar el proyecto ejecuta el archivo main.py\n")
            print("FLET HOT RELOAD")
            print("flet -r " + ruta + nombre + "\main.py\n")
            print("PYTHON")
            print("python " + ruta + nombre + "\main.py\n")

# ! No Mover
if __name__ == "__main__":
    main()