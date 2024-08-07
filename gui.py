

from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Users\Darre\Downloads\TKinter\Tkinter-Designer-master\build\assets\frame0")


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
    102.0,
    170.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    364.0,
    170.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    194.0,
    654.0,
    image=image_image_3
)

canvas.create_text(
    14.0,
    211.0,
    anchor="nw",
    text="Took a selfie with strangers on the beach! This was 🔥🔥🔥",
    fill="#000000",
    font=("Poppins Regular", 12 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    56.0,
    33.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    326.0,
    28.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    205.0,
    109.0,
    image=image_image_6
)

canvas.create_text(
    188.0,
    134.0,
    anchor="nw",
    text="POST",
    fill="#000000",
    font=("Poppins Bold", 12 * -1)
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    194.0,
    731.0,
    image=image_image_7
)

canvas.create_rectangle(
    169.0,
    742.0,
    220.0,
    780.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    101.0,
    738.0,
    135.0,
    776.0,
    fill="#FFFFFF",
    outline="")

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    195.0,
    757.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    109.0,
    760.0,
    image=image_image_9
)

canvas.create_rectangle(
    254.0,
    734.0,
    306.0,
    780.0,
    fill="#FFFFFF",
    outline="")

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    281.0,
    757.0,
    image=image_image_10
)

canvas.create_rectangle(
    254.0,
    734.0,
    306.0,
    780.0,
    fill="#FFFFFF",
    outline="")

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    281.0,
    757.0,
    image=image_image_11
)

image_image_12 = PhotoImage(
    file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(
    195.0,
    55.0,
    image=image_image_12
)

canvas.create_rectangle(
    4.0,
    92.0,
    433.0,
    97.0,
    fill="#565656",
    outline="")

image_image_13 = PhotoImage(
    file=relative_to_assets("image_13.png"))
image_13 = canvas.create_image(
    195.0,
    434.0,
    image=image_image_13
)
window.resizable(False, False)
window.mainloop()
