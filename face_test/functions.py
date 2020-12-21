def handle_uploaded_file(f):  
    with open('face_test/face_recon/knn_examples/test/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

    return 'face_test/face_recon/knn_examples/test/'+f.name