from PIL import ImageGrab
import pytesseract
import wayland_automation as wa
from time import sleep

def take_ss():
    box = (435, 195, 530, 235)

    image = ImageGrab.grab(box)

    return image

def get_text(image):
    return pytesseract.image_to_string(image, "eng")

def load_text():
    with open("tools/new_words3.txt", "r", newline="") as f:
        f_reader = f.readlines()

        words = []

        for row in f_reader:
            words.append(row)

    return words

def quick_checks(text):
    if text.lower().strip() == "19.4)":
        text = "ext"
    elif text.lower().strip() == "ouu":
        text = "ou"
    elif text.lower().strip() == r"[\ [e]\|":
        text = "non"
    elif text.lower().strip() == "I0":
        text = "io"
    elif text.lower().strip() == r"(efe] 7|":
        text = "com"
    elif text.lower().strip() == "\"'/ -\\":
        text = "wa"
    
    return text

def main(words: list):
    words_ = []

    while True:
        img = take_ss()
        text = str(get_text(img))

        text = quick_checks(text)

        found_word = ""

        for word in words:
            if text.lower().strip() in word.strip():
                if word.strip() in words_:
                    continue

                if len(word.strip()) > len(found_word):
                    found_word = word.strip()

        words_.append(found_word.strip())

        print(text.lower().strip())
        print(found_word, "\n")

        wa.typewrite(found_word, interval=0)
        wa.press("enter")

        sleep(1.5)

if __name__ == "__main__":
    words = load_text()

    main(words)
