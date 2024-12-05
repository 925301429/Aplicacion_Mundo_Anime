import reflex as rx

def homeScreen() -> rx.Component:
    return rx.mobile_and_tablet(
        rx.container(
            rx.color_mode.button(position="top-right"),
            rx.text("notificaciones", margin_top="15px"),
            rx.vstack(
                rx.image(src="anime.png", width="200px", padding="10px", margin_bottom="25px", margin_top="-50px"),
                rx.text("VIENVENIDO AL MUNDO ANIME", size="6", font_size="poppins"),
                rx.text("aqui podras verLlos animes que mas te sugerimos deacuerdo con elgenerok mas te guste", size="4", text_align="center"),
                rx.button("BUSCAR TU ANIME FAVORITO", font_size="poppins", background_color="black", margin_top="15px",
                          _hover={"background_color": "lightgreen"}),
                display="flex",
                align_items="center",
                margin_top="32vh",
                height="100vh"
            ),
        ),
    )