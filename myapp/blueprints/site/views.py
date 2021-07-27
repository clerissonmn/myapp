from flask import Blueprint, render_template

site = Blueprint(
    "site",
    __name__,
    url_prefix="/",
    static_url_path="",
    static_folder="static",
    template_folder="templates",
)


@site.route("/")
def index():
    return render_template("index.html")


@site.route("/about")
def about():
    return render_template("about.html")


@site.route("/work")
def work():
    return render_template("work.html")


@site.route("/work-single")
def work_single():
    return render_template("work-single.html")


@site.route("/pricing")
def pricing():
    return render_template("pricing.html")


@site.route("/contact")
def contact():
    return render_template("contact.html")
