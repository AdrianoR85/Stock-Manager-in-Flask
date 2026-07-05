from flask import Blueprint, render_template, request, redirect
from app.controller.User import UserController

user_controller = UserController()

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")


# Login route
@auth_bp.route("/login/", methods=["GET", "POST"])
def login():
    return render_template("pages/login.html")
    """if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = user_controller.login(email, password)
        
        if user:
            return redirect("/admin")
        else:
            return render_template("pages/login.html", data={"status": 401, "message": "Invalid email or password.", "type": None})
    return render_template("pages/login.html")"""


# Recovery password route
@auth_bp.route("/recovery_password/", methods=["GET", "POST"])
def recovery_password():
    if request.method == "POST":
        email = request.form["email"]

        user = user_controller.recovery_password(email)
        
        if user:
            return render_template("pages/recovery_password.html", data={"status": 200, "message": "Recovery email sent.", "type": None})
        else:
            return render_template("pages/recovery_password.html", data={"status": 404, "message": "Email not found.", "type": None})

    return render_template("pages/recovery_password.html")