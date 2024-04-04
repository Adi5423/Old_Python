import random
from tkinter import Canvas, Tk, PhotoImage

class DuckShootingGame:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        # Load the duck image.
        self.duck_image = PhotoImage(file="duck.png")
        self.duck_x = random.randint(0, 400)
        self.duck_y = random.randint(0, 400)

        # Draw the duck on the canvas.
        self.canvas.create_image(self.duck_x, self.duck_y, image=self.duck_image)

        # Bind the mouse click event to the shoot() method.
        self.canvas.bind("<Button-1>", self.shoot)

        # Start the game loop.
        self.root.mainloop()

    def shoot(self, event):
        # Get the mouse cursor coordinates.
        mouse_x = event.x
        mouse_y = event.y

        # Check if the mouse cursor is over the duck.
        if (mouse_x >= self.duck_x and mouse_x <= self.duck_x + self.duck_image.width) and (mouse_y >= self.duck_y and mouse_y <= self.duck_y + self.duck_image.height):
            # The mouse cursor is over the duck.
            # Remove the duck from the canvas.
            self.canvas.delete("duck")

            # Display a message that the duck was shot.
            self.canvas.create_text(250, 250, text="Duck shot!", font=("Arial", 20))

            # Start a new round.
            self.duck_x = random.randint(0, 400)
            self.duck_y = random.randint(0, 400)
            self.canvas.create_image(self.duck_x, self.duck_y, image=self.duck_image)

if __name__ == "__main__":
    DuckShootingGame()
