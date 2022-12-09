from app import app
from app.controllers import user_management

# app.route("/users", methods=["GET"])(tes.index)
app.route("/register", methods = ["POST"])(user_management.Register)