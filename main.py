import flet as ft, time, sys, os
from PIL import Image

def main(page: ft.Page):
    
    #Necessary for relative path to assets
    try:
        os.chdir(sys._MEIPASS)
        print('Running from executable...')
    except:
        pass

    pokemon_gif = "pikachu.gif"
    pokemon_pil = Image.open(f"assets/{pokemon_gif}")
    ball_img = "poke-ball.png"
    delay = 0.5

    #page.window.visible = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.always_on_top = True
    page.window.width = 150
    page.window.height = 150

    page.window.bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.window.title_bar_hidden = True
    page.window.frameless = True
    page.window.maximizable = False
    #page.window.skip_task_bar = True

    def launch_pokemon():

        pokemon.opacity = 1
        page.update()

        time.sleep(delay)

        pokemon.color = "grey"
        pokemon.opacity = 0
        page.update()

        time.sleep(delay)

        #Display pokemon gif and exit button
        exit_btn.data['show'] = True
        pokemon.src = pokemon_gif
        pokemon.color = None
        pokemon.opacity = 1
        pokemon.data['iswithdrawn'] = False

        page.update()


    def withdraw_pokemon():

        pokemon.color = "grey"
        pokemon.opacity = 0
        page.update()
        
        time.sleep(delay)

        #Display pokeball
        pokemon.color = None
        pokemon.src = ball_img
        pokemon.opacity = 1
        pokemon.data['iswithdrawn'] = True

        page.update()


    def run(e=None):

        if pokemon.data['iswithdrawn']:
            launch_pokemon()
        else:
            withdraw_pokemon()
    

    def exit_app():

        #Hide exit button
        exit_btn.data['show'] = False
        exit_btn.visible = False
        
        if not pokemon.data['iswithdrawn']:
            withdraw_pokemon()

        time.sleep(delay)
        page.window.close()


    def on_hover(is_hovered):

        if is_hovered.data == "true" and exit_btn.data['show']:
            exit_btn.visible = True
        else:
            exit_btn.visible = False

        page.update()


    def on_focused(window_event):
        if window_event.data == "focus":
        
            background_container.border = ft.border.all(2, ft.colors.WHITE)
            background_container.bgcolor = "#262626"
        else:
            background_container.border = None
            background_container.bgcolor = None

        page.update()
        

    pokemon = ft.Image(
        src=ball_img, 
        fit=ft.ImageFit.CONTAIN, animate_opacity=500, opacity=0, 
        width=80, 
        height=80,
        data={'iswithdrawn':True}
    )
    
    background_container =  ft.Container(
        content=pokemon,
        on_long_press=run,
        left=0,
        border_radius=5,
        image_fit=ft.ImageFit.CONTAIN
        # border=ft.border.all(2, ft.colors.WHITE),
        # bgcolor="#262626"
    )
    
    exit_btn = ft.IconButton(
        icon=ft.icons.CLOSE, 
        on_click=lambda _: exit_app(), 
        visible=False, 
        bgcolor=ft.colors.RED_ACCENT, 
        icon_color=ft.colors.WHITE, icon_size=10,
        width=28, height=28,
        data={'show':False}
    )

    app_content = ft.Stack(
        [
            background_container,
            ft.Container(
                content=exit_btn,
                right=0
            ),
        ],
        height=100, width=100
    )
    page.add(
        ft.WindowDragArea(
            content=ft.Container(
                content=app_content,
                on_hover=on_hover
            ),
        )
    )

    #A hack to apply and respect the window properties
    page.window.visible = True
    page.update()

    run()
    #page.window.on_event = on_focused

ft.app(target=main, assets_dir="assets", name="Poke-DeskBuddy")