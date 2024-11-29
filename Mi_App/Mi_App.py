import reflex as rx
def index() -> rx.Component:
    return rx.container(
    
        rx.hstack(
            rx.vstack(
                    rx.image(src="blob:https://web.whatsapp.com/a41da3b4-bebc-4806-b9ab-d31599152513"),
                    rx.link("siguiente",href="/iniciar")
                ),
            ),
      
    ),


app = rx.App()
app.add_page(index)