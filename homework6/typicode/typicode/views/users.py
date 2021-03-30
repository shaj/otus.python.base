from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

from ..models.database import db
from ..models.user import User


users_app = Blueprint("users_app", __name__)


@users_app.route("/", endpoint="list")
def users_list():
    users = User.query.all()
    return render_template("users/index.html", users=users)


@users_app.route("/<int:user_id>/", endpoint="details")
def user_details(user_id):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        # raise NotFound(f"User with id {user_id} doesn't exist!")
        return render_template("users/add-new.html")

    return render_template(
        "users/details.html",
        user=user,
    )


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add")
def user_add():
    if request.method == "GET":
        return render_template(
            "users/add.html",
            msg='',
        )

    username = request.form.get("user-name")
    user = User.query.filter_by(username=username).one_or_none()
    if not user is None:
        return render_template(
            "users/add.html",
            msg='User name must be unique ' + username,
        )
    user = User()
    user.username = username
    user.fullname = request.form.get("user-fullname")
    user.phone = request.form.get("user-phone")
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("users_app.list"))
