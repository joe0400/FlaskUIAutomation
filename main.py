

from flask import Flask


application = Flask(__name__)

main_page_file = "index.html"

@application.route("/")
def load_page():
    with open(main_page_file,"r") as file:
        return "".join(file.readlines());


