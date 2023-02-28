
from flask import Flask, jsonify, request
from datetime import datetime
from core.file_manage import FileController
from core.image_processing import ImageProcessingController


app = Flask(__name__)
file_controller = FileController()
image_processing_controller = ImageProcessingController()

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
    responce = image_processing_controller.object_detection(request)
    api_log_save("fileupload", "Called")
    return responce

def api_log_save(api_name, message):
    logFile = open("./storage/log_file.txt", "a")  # append mode
    logFile.write(f"{api_name}|{message}|{str(datetime.now())}\n")
    logFile.close()


app.run(host='0.0.0.0', port=5002)
