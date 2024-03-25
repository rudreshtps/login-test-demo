import json
from django.shortcuts import HttpResponse
from .models import CourseDetails

# Create your views here.
def getcourse(request):
    try:
        courses = CourseDetails.objects.all()
        courseData = []
        for c in courses:
            courseData.append({'courseId':c.courseId,'courseName':c.courseName,'path':c.path})
        return HttpResponse(json.dumps(courseData))
    except Exception as e:
        print("Exception Occured while getting all the courses")
        print(str(e))
        return HttpResponse('Server Error! Please Try Again Later',status=500)
    