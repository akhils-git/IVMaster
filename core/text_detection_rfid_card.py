import cv2
import easyocr



class TextDetector:
    def __init__(self, languages=['en']):
        self.reader = easyocr.Reader(languages)

    def get_value_from_rfid(self, image_path):
        img = cv2.imread(image_path)
        g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        b_img = cv2.bitwise_not(g_img)
        result = self.reader.readtext(b_img)
        text_list = [i[1] for i in result]
        detected_text = ' '.join(text_list)
        return detected_text