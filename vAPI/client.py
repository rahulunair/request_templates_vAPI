import json
import random
import string

import requests

import syntribos.extensions.vAPI.config


config = syntribos.extensions.vAPI.config.UserConfig(section_name="vAPI")


def authenticate(url, username=None, password=None):

    url = "{0}/tokens".format(url)

    creds = {"username": username, "password": password}
    headers = {"Content-Type": "application/json"}
    data = {"auth": {"passwordCredentials": creds}}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    if not r.ok:
        raise Exception("Failed to authenticate")

    try:
        dat = json.loads(r.text)
        return dat
    except ValueError:
        return None


def get_token():

    url = config.url
    username = config.username
    password = config.password

    access_data = authenticate(url, username, password)
    if access_data:
        return access_data["access"]["token"]["id"]


def get_random_string(length=10, type=None):
    """
    A simple random string generator for injecting in places
    where dynamic strings are required.
    """

    if type == "ascii":
        return "".join(random.choice(
            string.ascii_letters) for i in range(length))
    return "".join(random.choice(string.printable) for i in range(length))
