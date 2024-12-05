import reflex as rx

def notifyScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.hstack(
            rx.color_mode.button(position="top-right"),
            rx.text("notificaciones", margin_top="15px", margin_bottom="10px"),
            style={
                "border_bottom":"2px solid #c56dfc"},
            margin_bottom="100px"),
            rx.vstack(
                rx.button("tienes una capitulo pendiente", height="50px", background_color="sky blue"),
                rx.button("tines una capitulo de kimetsu noyaiva pendiente", height="50px", background_color="sky blue"),
             
            )))