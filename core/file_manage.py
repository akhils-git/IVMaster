from flask import jsonify
import os


class FileController:

    def __init__(self):
        self.ALLOWED_EXTENSIONS = set(
            ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'exe'])
    # body of the constructor

    def allowed_file(self, filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in self.ALLOWED_EXTENSIONS

    def upload_file(self, request):
        # check if the post request has the file part.
        if 'file' not in request.files:
            resp = jsonify({'message': 'No file part in the request'})
            resp.status_code = 400
            return resp
        file = request.files['file']
        if file.filename == '':
            resp = jsonify({'message': 'No file selected for uploading'})
            resp.status_code = 400
            return resp
        if file and self.allowed_file(file.filename):
            upload_basepath = './storage/uploads/'+file.filename
            file.save(upload_basepath)
            file_size = os.stat(upload_basepath)
            resp = jsonify(
                {'message': 'File successfully uploaded', 'size': file_size.st_size/1024, "file_name": file.filename})
            resp.status_code = 201
            return resp
        else:
            resp = jsonify(
                {'message': 'Allowed file types are txt, pdf, png, jpg, jpeg, gif'})
            resp.status_code = 400
            return resp

    def list_files(self):
        staticPath = "./storage/uploads/"
        print(f"Files in the directory: {staticPath}")
        files = os.listdir(staticPath)
        print(files)
        # Filtering only the files.
        files = [f for f in files if os.path.isfile(staticPath + '/' + f)]

        return files
