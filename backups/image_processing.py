# import face_recognition
# from PIL import Image, ImageDraw


# def detect_faces(image_file, outline_color):
#     image = face_recognition.load_image_file(image_file)
#     face_locations = face_recognition.face_locations(image)
#     number_of_faces = len(face_locations)
#     print("I found {} face(s) in this photograph.".format(number_of_faces))
#     Pil_image = Image.fromarray(image)
#     draw = ImageDraw.Draw(Pil_image)
#     for face_location in face_locations:
#         top, right, bottom, left = face_location
#         draw.rectangle([left, top, right, bottom], outline=outline_color)
#     return Pil_image


# output_image = detect_faces("/content/drive/MyDrive/Dhoni.jpg", "blue")
# output_image.save("/content/drive/MyDrive/output8.jpg")
