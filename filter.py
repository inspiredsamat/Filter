import tkinter as tk
from tkinter import filedialog
import cv2 as cv
from PIL import ImageTk, Image
import numpy as np
import sys
import pyautogui

screen_width, screen_height = pyautogui.size()


def on_clicked(window):
    window.destroy()
    file_path = filedialog.askopenfilename()
    new_window = tk.Tk()
    new_window.title("Filter")
    new_window.geometry("800x800")
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(new_window, image=photo)
    button_x = tk.Button(new_window, text="Derivative in X",
                         command=lambda: derivative_xdirection(file_path, new_window))
    button_y = tk.Button(new_window, text="Derivative in Y",
                         command=lambda: derivative_ydirection(file_path, new_window))
    button_gaussian = tk.Button(
        new_window, text="Gaussian blur", command=lambda: gaussian_blur(file_path, new_window))
    label.pack()
    button_x.pack(side="left", pady=20, padx=(240, 10))
    button_y.pack(side="left", pady=20, padx=10)
    button_gaussian.pack(side="left", pady=20, padx=(10, 100))
    x = int((screen_width/2) - (800/2))
    y = int((screen_height/2) - (800/2))
    new_window.geometry(f"+{x}+{y}")
    new_window.mainloop()


def gaussian_blur(file_path, window):
    window.destroy()
    image = cv.imread(file_path)
    gaussian_image = cv.GaussianBlur(image, (5, 5), 0)
    cv.imshow("Image applied Gaussian blur", gaussian_image)
    if cv.waitKey(0):
        continue_window()


def derivative_xdirection(file_path, window):
    window.destroy()
    image = cv.imread(file_path)
    image_x = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=3)
    cv.imshow("Derivative of image in x direction", image_x)
    if cv.waitKey(0):
        continue_window()


def derivative_ydirection(file_path, window):
    window.destroy()
    image = cv.imread(file_path)
    image_y = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=3)
    cv.imshow("Derivative of image in x direction", image_y)
    if cv.waitKey(0):
        continue_window()


def continue_window():
    window = tk.Tk()
    window.title("Filter")
    label = tk.Label(window, text="Do you want\n to continue?",
                     font=("Arial", 24), fg="red")
    label.pack(pady=20)
    button_yes = tk.Button(window, text="Yes, I do",
                           command=lambda: on_clicked_yes(window))
    button_no = tk.Button(window, text="No, I don't",
                          command=lambda: sys.exit(0))
    button_yes.pack(side="left", padx=40)
    button_no.pack(side="right", padx=40)
    window.geometry("300x250")
    x = int((screen_width/2) - (360/2))
    y = int((screen_height/2) - (300/2))
    window.geometry(f"+{x}+{y}")
    window.mainloop()


def on_clicked_yes(window):
    window.destroy()
    start()


def start():
    window = tk.Tk()
    window.title("Filter")
    label = tk.Label(window, text="Welcome to Filter",
                     font=("Arial", 24), fg="blue")
    label.pack(pady=20)
    button = tk.Button(window, text="Select an image",
                       command=lambda: on_clicked(window))
    button.pack(pady=40)
    window.geometry("260x200")
    x = int((screen_width/2) - (300/2))
    y = int((screen_height/2) - (300/2))
    window.geometry(f"+{x}+{y}")
    window.mainloop()


start()
