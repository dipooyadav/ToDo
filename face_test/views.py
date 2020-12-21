from django.shortcuts import render  
from django.http import HttpResponse  
from .functions import handle_uploaded_file  
from .forms import StudentForm  
from .face_recon.face2 import predict
import json
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid():  
            list_students = []
            full_file_path = handle_uploaded_file(request.FILES['file'])  
            predictions = predict(full_file_path, model_path="face_test/face_recon/trained_knn_model.clf")
            for name, (top, right, bottom, left) in predictions:
                list_students.append(name)
            response_data = {}
            response_data["results"] = list_students    
            return  HttpResponse(json.dumps(response_data), content_type="application/json")
    else:  
        student = StudentForm()  
        return render(request,"face_test/face.html",{'form':student})




