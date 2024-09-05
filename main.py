

from flask import Flask, request
import os
import openai

application = Flask(__name__)

main_page_file = os.path.join(os.path.join(os.getcwd(),"pages"),"index.html")



@application.route("/")
def load_page():
    with open(main_page_file,"r") as file:
        return "".join(file.readlines())


def register_app_routes():

    for each in os.listdir(os.path.join(os.getcwd(),"pages")):
        if os.path.isfile(os.path.join(os.path.join(os.getcwd(),"pages"),each)):
            @application.route(f"/${each}")
            def handler():
                with open(os.path.join(os.path.join(os.getcwd(),"pages"),each),"r") as file:
                    return "".join(file.readlines())


@application.route("/settings", methods=['GET','POST'])
def settings():
    match request.method:
        case "GET":
            return getsettings()
        case "POST":
            return modifysettings()

def getsettings():
    with open(os.path.join(os.path.join(os.getcwd(),"settings"),"settings.json"),"r") as file:
        return application.response_class(
            response="".join(file.readlines()),
            status=200,
            mimetype="application/json"
        )
OpenAIConnector = None
Errors = None
try:
    OpenAIConnector = openai.OpenAI(
        api_key=getsettings().response["key"],
        base_url=getsettings().response["base_url"]
    )
except Exception as e:
    Errors = e

def modifysettings():
    # now that we know the settings exist we can trigger the changes fromt he request object. we wont be
    # doing any check here for validity, as i will assume the request is not malformed.

    pass


def reload_open_ai_connector():
    # get the settings file
    file = getsettings().response






@application.route("/listeners")
def listen_to_server_port():
    pass

register_app_routes()

if __name__ == '__main__':
    application.run()

