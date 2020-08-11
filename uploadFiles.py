import dropbox
import os

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    
                    # Upload the file to Dropbox

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
        with open(localPath,'rb')    as f:
            dbx.fileUpload(f.read(),dropbox_path, mode=WriteMode('overwrite'))


def main():
    acessToken = 'sl.AfnyOh_DStRTM8cB6MMgYiBxdnZ0nIYRh8HvsWRLpSe3_mjM4vG18PNyQggDKOccxmFZzuXj55EhFt7UCDjZTmnaBMq0UftqAxQ2WvdS2uqxVBo7rj6SLixMtOTMDzA3axH7srs'
    transferData =  TransferData(acessToken)

    file_from = input("Please enter the full file path that you need to transfer :   ")
    file_to = input("Please enter the full path to upload to dropbox : ")

    transferData.upload_file(file_from, file_to)
    print("Your file has been uploaded successfully!")

if __name__ == "__main__":
    main()
    \