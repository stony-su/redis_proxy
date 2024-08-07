

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Users\Darre\Downloads\TKinter\Tkinter-Designer-master\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("390x844")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 844,
    width = 390,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    2.0,
    533.0,
    394.0,
    593.0,
    fill="#85D139",
    outline="")

canvas.create_rectangle(
    0.0,
    593.0,
    390.0,
    655.0,
    fill="#CA2020",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    56.0,
    33.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    326.0,
    28.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    189.0,
    745.0,
    image=image_image_3
)

canvas.create_rectangle(
    164.0,
    743.0,
    215.0,
    781.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    96.0,
    739.0,
    130.0,
    777.0,
    fill="#FFFFFF",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    111.0,
    757.0,
    image=image_image_4
)

canvas.create_rectangle(
    13.0,
    733.0,
    52.0,
    781.0,
    fill="#FFFFFF",
    outline="")

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    37.0,
    758.0,
    image=image_image_5
)

canvas.create_text(
    84.0,
    101.0,
    anchor="nw",
    text="DISCOMFORT-30",
    fill="#005ACD",
    font=("Poppins Bold", 25 * -1)
)

canvas.create_text(
    40.0,
    158.0,
    anchor="nw",
    text="Welcome back David!\nYou’re on DAY 15.",
    fill="#000000",
    font=("Inter", 25 * -1)
)

canvas.create_text(
    105.0,
    250.0,
    anchor="nw",
    text="Singers Oscar",
    fill="#000000",
    font=("Poppins Bold", 25 * -1)
)

canvas.create_text(
    27.0,
    317.0,
    anchor="nw",
    text="Sing the full  “Let It Go” song\n\n\n+10 Points for body gestures.",
    fill="#000000",
    font=("Poppins Regular", 22 * -1)
)

canvas.create_text(
    30.0,
    353.0,
    anchor="nw",
    text="near a crowd as loud as you can. ",
    fill="#000000",
    font=("Poppins Regular", 22 * -1)
)

canvas.create_rectangle(
    145.0,
    303.0,
    240.0,
    307.0,
    fill="#000000",
    outline="")

canvas.create_text(
    138.0,
    484.0,
    anchor="nw",
    text="LEVEL: 4/5",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

canvas.create_text(
    162.0,
    600.0,
    anchor="nw",
    text="ABORT",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

canvas.create_text(
    132.0,
    543.0,
    anchor="nw",
    text="COMPLETED",
    fill="#000000",
    font=("Poppins Regular", 25 * -1)
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    195.0,
    759.0,
    image=image_image_6
)

canvas.create_rectangle(
    246.0,
    731.0,
    298.0,
    777.0,
    fill="#FFFFFF",
    outline="")

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    273.0,
    754.0,
    image=image_image_7
)

canvas.create_rectangle(
    246.0,
    731.0,
    298.0,
    777.0,
    fill="#FFFFFF",
    outline="")

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    273.0,
    754.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    195.0,
    56.0,
    image=image_image_9
)
window.resizable(False, False)
window.mainloop()
