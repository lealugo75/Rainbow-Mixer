import flet as ft

def main(page: ft.Page):
    page.title = "RBG COLOR MIXER"

    rgb_text = ft.Text(value="R: 0 G: 0 B: 0", size=20)

    def update_color(e):
        red = int(red_slider.value)
        green = int(green_slider.value)
        blue = int(blue_slider.value)

        page.bgcolor = f"#{red:02x}{green:02x}{blue:02x}"
        rgb_text.value = f"R: {red} G: {green} B: {blue}"

        page.update()

    red_slider= ft.Slider(min=0, max=255, value=0, on_change=update_color)
    green_slider= ft.Slider(min=0, max=255, value=0, on_change=update_color)
    blue_slider= ft.Slider(min=0, max=255, value=0, on_change=update_color)

    page.add(
        ft.Text("Red"), red_slider,
        ft.Text("Green"), green_slider,
        ft.Text("Blue"), blue_slider, 
        rgb_text 
    )
ft.app(target=main)