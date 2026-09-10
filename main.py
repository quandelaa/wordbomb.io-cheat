from PIL import ImageGrab
import pytesseract
import keyboard
from time import sleep

def take_ss():
    box = (435, 195, 530, 235)

    image = ImageGrab.grab(box)

    return image

def get_text(image):
    return pytesseract.image_to_string(image, "eng")

def load_text():
    with open("new_words.txt", "r", newline="") as f:
        f_reader = f.readlines()

        words = []

        for row in f_reader:
            words.append(row)

    return words

def main(words):
    while True:
        img = take_ss()
        text = str(get_text(img))

        print(text.lower())

        for word in words:
            if text.lower() in word.strip():
                print(word)
                return

        sleep(2)

if __name__ == "__main__":
    words = load_text()

    main(words)
