def handle_uploaded_file(f):
    with open("musicshare/uploaded_files/audiofile.dat", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)