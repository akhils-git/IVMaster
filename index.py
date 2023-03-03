
from flask import Flask, jsonify, request
from datetime import datetime
from core.file_manage import FileController
from core.image_processing import ImageProcessingController
from core.text_detection_rfid_card import TextDetector
from core.video_processing import VideoProcessingController
from core.face_compare import FaceComparer
from core.face_detection import FaceDetector

app = Flask(__name__)
file_controller = FileController()
image_processing_controller = ImageProcessingController()
card=TextDetector()
video_processing_controller=VideoProcessingController()
facecompare = FaceComparer()
facedetection = FaceDetector()

print("IV-Master Api Running...")



@app.route("/")
def hello():
    api_log_save("Homepage", "Running Good")
    return open('./pages/home.html', 'r')


@app.route('/api/getname/<name>', methods=['GET'])
def getname(name):
    api_log_save("getname", "Get name")
    return jsonify("Hi " + name + " Called at " + str(datetime.now()))


@app.route('/api/fileupload', methods=['POST'])
def upload_file():
    print(request.files)
    responce = file_controller.upload_file(request)
    api_log_save("fileupload", "Called")
    return responce


@app.route('/api/detectimageobjects', methods=['POST'])
def detectimageobjects():
    print(request.files)
    responce = file_controller.upload_file(request)
    data=responce.get_json()
    path=r'.\storage\uploads\\'
    output=image_processing_controller.object_detection(f"{path}{data['file_name']}")
    #api_log_save("fileupload", "Called")
    return output


@app.route('/api/CardDetection', methods=['POST'])
def TextDetection():
    print(request.files)
    responce = file_controller.upload_file(request)
    data=responce.get_json()
    
    path=r'.\storage\uploads\\'
    output=card.get_value_from_rfid(f"{path}{data['file_name']}")
    api_log_save("fileupload", "Called")
    return output

@app.route('/api/detectvideoobjects', methods=['POST'])
def detectvideoobjects():
    print(request.files)
    responce = file_controller.upload_file(request)
    data=responce.get_json()
    path=r'.\storage\uploads\\'
    output=video_processing_controller.DetectedObjects(f"{path}{data['file_name']}")
    api_log_save("VideoObjectDetection", "Completed")
    return output
@app.route('/api/facecompare', methods=['POST'])
def FaceCompare():
    print(request.files)
    responce = file_controller.upload_file(request)
    data=responce.get_json()
    
    
    path1=r'.\storage\uploads\\'+data[0]['file_name']
    path2=r'.\storage\uploads\\'+data[1]['file_name']
    #path1 = r".\storage\uploads\Dhoni.jpg"
    #path=r'.\storage\uploads\\'

    output=facecompare.compare_faces(path1,path2)
    api_log_save("fileupload", "Called")
    return output
@app.route('/api/FaceDetection', methods=['POST'])
def FaceDetection():
    print(request.files)
    responce = file_controller.upload_file(request)
    data=responce.get_json()
    
    
    path=r'.\storage\uploads\\'
    output=facedetection.detect_faces(f"{path}{data[0]['file_name']}")
    api_log_save("fileupload", "Called")
    return jsonify(output)

def api_log_save(api_name, message):
    logFile = open("./storage/log_file.txt", "a")  # append mode
    logFile.write(f"{api_name}|{message}|{str(datetime.now())}\n")
    logFile.close()


app.run(host='0.0.0.0', port=5002)
