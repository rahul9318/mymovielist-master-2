from flask import Flask
from flask import render_template
from flask import  request, redirect
import smtplib

app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       name = request.form.get("fname")
       # getting input with name = lname in HTML form
       email = request.form.get("lname")
       subject = request.form.get("subject")
       message = request.form.get("message")
       message= (f"Name:{name}\n"
             f"email:{email}\n"
                 f"Subject:{email}\n"
             f"subject:{subject}\n")
       return redirect("http://rahuldev.atwebpages.com/")


#        my_email = "rahulbhardwaj930@gmail.com"
#        password = "fastandfurious8"
       
       
#        connection = smtplib.SMTP("smtp.gmail.com")
#        connection.starttls()
#        connection.login(user=my_email, password=password)
#        connection.sendmail(from_addr=my_email, to_addrs="rahulbhardwaj8851046@gmail.com",msg=message)
       
#        connection.close

    return render_template("index.html")









if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
