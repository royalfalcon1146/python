from IPython.display import display
import fileupload
import io
import sys

#Make sure to download the above modules first!
#This shows how you can upload a file to python, it displays a widget for you to open your txt file with!
#The contents of the file are stored in a string called: file_contents

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()