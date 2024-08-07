
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Users\Darre\Downloads\TKinter\Tkinter-Designer-master\build\assets\frame3")


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

canvas.create_rectangle(
    13.0,
    733.0,
    52.0,
    781.0,
    fill="#FFFFFF",
    outline="")

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    197.0,
    760.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    44.0,
    763.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    114.0,
    762.0,
    image=image_image_6
)

canvas.create_rectangle(
    59.0,
    331.0,
    333.0,
    415.0,
    fill="#D8F2FF",
    outline="")

canvas.create_rectangle(
    59.0,
    431.0,
    333.0,
    515.0,
    fill="#D8F2FF",
    outline="")

canvas.create_rectangle(
    55.0,
    539.0,
    329.0,
    623.0,
    fill="#5B9735",
    outline="")

canvas.create_text(
    136.0,
    361.0,
    anchor="nw",
    text="Location",
    fill="#000000",
    font=("Poppins Regular", 22 * -1)
)

canvas.create_text(
    72.0,
    194.0,
    anchor="nw",
    text="Challenge Counter: 50",
    fill="#000000",
    font=("Poppins Regular", 22 * -1)
)

canvas.create_text(
    76.0,
    268.0,
    anchor="nw",
    text="Configurations",
    fill="#000000",
    font=("Poppins Bold", 30 * -1)
)

canvas.create_text(
    118.0,
    460.0,
    anchor="nw",
    text="Select Level",
    fill="#000000",
    font=("Poppins Regular", 22 * -1)
)

canvas.create_text(
    120.0,
    96.0,
    anchor="nw",
    text="“Get comfortable ",
    fill="#000000",
    font=("Poppins Regular", 18 * -1)
)

canvas.create_text(
    107.0,
    124.0,
    anchor="nw",
    text="being uncomfortable”",
    fill="#000000",
    font=("Poppins Regular", 18 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    283.0,
    470.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    282.0,
    371.0,
    image=image_image_8
)

canvas.create_text(
    86.0,
    562.0,
    anchor="nw",
    text="Generate Challenge",
    fill="#D8F2FF",
    font=("Poppins Regular", 22 * -1)
)

canvas.create_rectangle(
    250.0,
    735.0,
    302.0,
    781.0,
    fill="#FFFFFF",
    outline="")

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    277.0,
    758.0,
    image=image_image_9
)

canvas.create_rectangle(
    250.0,
    735.0,
    302.0,
    781.0,
    fill="#FFFFFF",
    outline="")

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    277.0,
    758.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    198.0,
    58.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    196.0,
    58.0,
    image=image_image_12
)
window.resizable(False, False)
window.mainloop()
