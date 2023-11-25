import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFilter


def create_gui_interface():
    """
    This function creates a GUI interface to insert, resize, color, rotate, draw on, and blur an image.
    """
    # Create the main window
    window = tk.Tk()
    window.title("Image Editor")
    window.geometry("700x700")

    # Function to handle image resizing
    def resize_image():
        # Get the user input for the new dimensions
        new_width = int(width_entry.get())
        new_height = int(height_entry.get())

        # Resize the image
        resized_image = image.resize((new_width, new_height))

        # Update the image in the GUI
        new_image = ImageTk.PhotoImage(resized_image)
        image_label.configure(image=new_image)
        image_label.image = new_image
        return new_image

    def crop_image():
        # Get the user input for the new dimensions
        left = int(crop_left_entry.get())
        top = int(crop_top_entry.get())
        right = int(crop_right_entry.get())
        bottom = int(crop_bottom_entry.get())

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Shows the image in image viewer
        #im1.show()

        # Update the image in the GUI
        new_image = ImageTk.PhotoImage(cropped_image)
        image_label.configure(image=new_image)
        image_label.image = new_image

        return new_image

    # Function to handle image rotation
    def rotate_image():
        # Get the user input for the rotation angle
        angle = int(angle_entry.get())

        # Rotate the image
        rotated_image = image.rotate(angle)

        # Update the image in the GUI
        new_image = ImageTk.PhotoImage(rotated_image)
        image_label.configure(image=new_image)
        image_label.image = new_image

    # Function to handle drawing on the image
    def draw_on_image():
        # Get the user input for the drawing color and coordinates
        red = int(draw_red_entry.get())
        green = int(draw_green_entry.get())
        blue = int(draw_blue_entry.get())
        x = int(draw_x_entry.get())
        y = int(draw_y_entry.get())

        # Draw on the image
        draw = ImageDraw.Draw(image)
        draw.rectangle([(x, y), (x + 50, y + 50)], fill=(red, green, blue))

        # Update the image in the GUI
        new_image = ImageTk.PhotoImage(image)
        image_label.configure(image=new_image)
        image_label.image = new_image

    # Function to handle image blurring
    def blur_image():
        # Get the user input for the blur radius
        radius = int(blur_radius_entry.get())

        # Blur the image
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius))

        # Update the image in the GUI
        new_image = ImageTk.PhotoImage(blurred_image)
        image_label.configure(image=new_image)
        image_label.image = new_image

    # Load the initial image
    image = Image.open("sample.jpg")
    tk_image = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(window, image=tk_image)
    image_label.grid(row=1, column=2, columnspan=4)

    # Create top margin
    top_margin = tk.Label(window, text="")
    top_margin.grid(row=0, column=0, columnspan=6)

    # Create left margin
    left_margin = tk.Label(window, text="")
    left_margin.grid(row=0, column=0)

    # Create input fields and buttons for each operation
    width_label = tk.Label(window, text="New Width:")
    width_label.grid(row=4, column=1)
    width_entry = tk.Entry(window)
    width_entry.grid(row=5, column=1)
    height_label = tk.Label(window, text="New Height:")
    height_label.grid(row=6, column=1)
    height_entry = tk.Entry(window)
    height_entry.grid(row=7, column=1)
    resize_button = tk.Button(window, text="Resize", command=resize_image)
    resize_button.grid(row=8, column=1)

    angle_label = tk.Label(window, text="Rotation Angle:")
    angle_label.grid(row=4, column=2)
    angle_entry = tk.Entry(window)
    angle_entry.grid(row=5, column=2)
    rotate_button = tk.Button(window, text="Rotate", command=rotate_image)
    rotate_button.grid(row=6, column=2)

    draw_general_label_1 = tk.Label(window, text="Draw coordinates:")
    draw_general_label_1.grid(row=4, column=3, columnspan=2)
    draw_general_label_2 = tk.Label(window, text="(axis starts in top left corner, set colors in RGB scale)")
    draw_general_label_2.grid(row=5, column=3, columnspan=2)
    draw_red_label = tk.Label(window, text="Red:")
    draw_red_label.grid(row=6, column=3)
    draw_red_entry = tk.Entry(window)
    draw_red_entry.grid(row=7, column=3)
    draw_green_label = tk.Label(window, text="Green:")
    draw_green_label.grid(row=8, column=3)
    draw_green_entry = tk.Entry(window)
    draw_green_entry.grid(row=9, column=3)
    draw_blue_label = tk.Label(window, text="Blue:")
    draw_blue_label.grid(row=10, column=3)
    draw_blue_entry = tk.Entry(window)
    draw_blue_entry.grid(row=11, column=3)

    draw_x_label = tk.Label(window, text="X Coordinate:")
    draw_x_label.grid(row=6, column=4)
    draw_x_entry = tk.Entry(window)
    draw_x_entry.grid(row=7, column=4)
    draw_y_label = tk.Label(window, text="Y Coordinate:")
    draw_y_label.grid(row=8, column=4)
    draw_y_entry = tk.Entry(window)
    draw_y_entry.grid(row=9, column=4)
    draw_button = tk.Button(window, text="Draw", command=draw_on_image)
    draw_button.grid(row=10, column=4)

    blur_radius_label = tk.Label(window, text="Blur Radius:")
    blur_radius_label.grid(row=4, column=5)
    blur_radius_entry = tk.Entry(window)
    blur_radius_entry.grid(row=5, column=5)
    blur_button = tk.Button(window, text="Blur", command=blur_image)
    blur_button.grid(row=6, column=5)

    crop_general_label_3 = tk.Label(window, text="Crop image (set coordinates):")
    crop_general_label_3.grid(row=4, column=6, columnspan=2)
    crop_left_label = tk.Label(window, text="Left:")
    crop_left_label.grid(row=5, column=6)
    crop_left_entry = tk.Entry(window)
    crop_left_entry.grid(row=6, column=6)
    crop_top_label = tk.Label(window, text="Top:")
    crop_top_label.grid(row=7, column=6)
    crop_top_entry = tk.Entry(window)
    crop_top_entry.grid(row=8, column=6)
    crop_right_label = tk.Label(window, text="Right:")
    crop_right_label.grid(row=5, column=7)
    crop_right_entry = tk.Entry(window)
    crop_right_entry.grid(row=6, column=7)
    crop_bottom_label = tk.Label(window, text="Bottom:")
    crop_bottom_label.grid(row=7, column=7)
    crop_bottom_entry = tk.Entry(window)
    crop_bottom_entry.grid(row=8, column=7)
    crop_button = tk.Button(window, text="Crop", command=crop_image)
    crop_button.grid(row=9, column=6, columnspan=2)

    # Create right margin
    right_margin = tk.Label(window, text="")
    right_margin.grid(row=0, column=8)

    # Start the main loop
    window.mainloop()


create_gui_interface()
