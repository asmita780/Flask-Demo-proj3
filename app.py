# from flask import Flask,render_template

# app=Flask(__name__)

# @app.route("/")
# def student_profile():
#     return render_template(
#         "profile.html",
#         name="Jhon singh",
#         is_topper=True,
#         subjects=["math","chemistry","physic"]
#     )


# if __name__=="__main__":
#     app.run()


from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__=="__main__":
    app.run()