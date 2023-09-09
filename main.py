import flet as ft, time
from PIL import Image

def main(page: ft.Page):
    
    pokemon_gif = "pikachu.gif"
    pokemon_pil = Image.open(f"assets/{pokemon_gif}")
    ball_img = "poke-ball.png"
    delay = 0.5

    page.window_visible = False
    page.window_always_on_top = True
    page.window_width = (pokemon_pil.width*1.5)+120
    page.window_height = (pokemon_pil.height*1.5)+120
    page.window_title_bar_hidden = True
    page.window_bgcolor = ft.colors.TRANSPARENT
    page.bgcolor = ft.colors.TRANSPARENT
    page.window_title_bar_hidden = True
    page.window_frameless = True
    page.window_maximizable = False
    page.window_skip_task_bar = True
    page.update()

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
        page.window_close()


    def on_hover(is_hovered):

        if is_hovered.data == "true" and exit_btn.data['show']:
            exit_btn.visible = True
        else:
            exit_btn.visible = False

        page.update()


    pokemon = ft.Image(
            src=ball_img, 
            fit=ft.ImageFit.CONTAIN, animate_opacity=500, opacity=0, 
            width=pokemon_pil.width*1.5, 
            height=pokemon_pil.height*1.5,
            data={'iswithdrawn':True}
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
            ft.Container(
                content=pokemon,
                on_long_press=run,
                left=0
            ),
            ft.Container(
                content=exit_btn,
                right=0
            ),
        ],
        width=page.window_width, height=page.window_height
    )
    
    page.add(
        ft.WindowDragArea(
            content=ft.Container(
                content=app_content,
                on_hover=on_hover
            )
        )
    )

    #A hack to apply and respect the window properties
    page.window_visible = True
    page.update()

    run()

ft.app(target=main, assets_dir="assets", name="Poke-DeskBuddy")