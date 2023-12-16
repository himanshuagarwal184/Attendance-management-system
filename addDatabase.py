import firebase_admin

from firebase_admin import db

cred = firebase_admin.credentials.Certificate(r"C:\Users\himan\OneDrive\Desktop\python\Machine Learning\Deep Learning\attendence_project\facerecognition-52bb7-firebase-adminsdk-8nr3m-4cc8f35368.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://facerecognition-52bb7-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "1":
    {
        "name":"XYZ",
        "major":"abc",
        "starting":2017,
        "total_attendance":6,
        "standing":"G",
        "Year":4,
        "LastAttendanceTime":"2023-12-01 00:54:34"
    },
    "2":
    {
        "name":"Modi",
        "major":"qqq",
        "starting":2014,
        "total_attendance":60,
        "standing":"E",
        "Year":9,
        "LastAttendanceTime":"2023-12-01 01:43:41"
    },
    "3":
    {
        "name":"Himanshu",
        "major":"CSE",
        "starting":2021,
        "total_attendance":4,
        "standing":"A+",
        "Year":3,
        "LastAttendanceTime":"2023-12-09 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)