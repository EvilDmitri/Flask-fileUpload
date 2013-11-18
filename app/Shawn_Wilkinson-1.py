import os

from flask import Flask, redirect, request, render_template, url_for, flash, g, abort
from werkzeug import secure_filename
#from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import storage


app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['DEFAULT_FILE_STORAGE'] = 'filesystem'


#app.config['UPLOAD_FOLDER'] = os.path.realpath('.') + '/files/upload/'
app.config['UPLOAD_FOLDER'] = '/home/dimas/WORK/Shawn_Wilkinson/Shawn_Wilkinson-1/app/files/upload/'

app.config['FILE_SYSTEM_STORAGE_FILE_VIEW'] = 'upload'


@app.route('/')
def index():
    """List the uploads."""
    #uploads = Upload.query.all()
    uploads = '1, 2'
    return render_template('list.html', uploads=uploads)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'somefile' in request.files:
        file = request.files['somefile']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filename)

            #flash("Photo saved.")
            print '1'
            return redirect(url_for('upload'))

    return render_template('upload.html')

from flask import send_from_directory


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)


@app.route('/file/<id>')
def show(id):
    photo = Photo.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo)




if __name__ == '__main__':
    app.run()