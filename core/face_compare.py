import face_recognition
import cv2

class FaceComparer:
    
    def compare_faces(self, image_path1, image_path2):
        # Load the images
        img1 = cv2.imread(image_path1, cv2.IMREAD_COLOR)
        img2 = cv2.imread(image_path2, cv2.IMREAD_COLOR)

        # Get the face encodings of the images
        face_encoding1 = face_recognition.face_encodings(img1)[0]
        face_encoding2 = face_recognition.face_encodings(img2)[0]

        # Compare the face encodings 
        dist = face_recognition.compare_faces([face_encoding1], face_encoding2)

        # Compare the distance to a threshold
        if dist[0]==True:
            return "Matching"
        else:
            return "Not matching"