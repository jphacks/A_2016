import base64
import json
import os

import firebase_admin
from firebase_admin.credentials import Certificate

GCP_SERVICE_ACCOUNT_KEY = os.environ.get("GCP_SERVICE_ACCOUNT_KEY", "")

app = None


def new_app():
    if GCP_SERVICE_ACCOUNT_KEY != "":
        cred = json.loads(base64.b64decode(GCP_SERVICE_ACCOUNT_KEY).decode('utf-8'))
        return firebase_admin.initialize_app(Certificate(cred))


def init():
    global app
    app = new_app()
