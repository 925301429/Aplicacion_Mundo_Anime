import reflex as rx

@rx.page(route="/iniciar", title="inicia secion")
def iniciar()->rx.Component:
    return rx.heading("soy inicio de sesion",font_family="tangerine",)