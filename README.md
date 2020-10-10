# bottle-project
REST Server style project for IOT use using Bottle

Steps on how to run this application:

1.  Install Python
2.  Install pip
3.  Install bottle
      pip install bottle
4.  Install paste
      pip install Paste
5.  Download the code or the zip file of this project      
6.  cd to the directory where you download this zip file and unzip it
7.  Run the project
      D:\git\bottle-project>python student_db_server.py
8.  You should see the following message being shown
      D:\git\bottle-project>python student_db_server.py
      serving on 0.0.0.0:8080 view at http://127.0.0.1:8080
      
9.  Go to your browser and enter the following in the url
      http://localhost:8080/student/isauthorized?rf_id_code=00-55-66
      
10. You should see the following information shown
      {"is_authorized": "true"}

