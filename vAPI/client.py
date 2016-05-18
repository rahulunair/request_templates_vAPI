import json
import random
import string

import requests

import syntribos.extensions.vAPI.config


def authenticate(url, username=None, password=None):

    url = '{0}/tokens'.format(url)

    kwargs = {}
    headers = {}
    kwargs["username"] = username
    kwargs["password"] = password
    headers["Content-Type"] = "Application/json"
    data = {"auth": {"passwordCredentials": kwargs}}

    r = requests.post(url, data=json.dumps(data), headers=headers)

    if not r.ok:
        raise Exception("Failed to authenticate")

    return json.loads(r.text)


def get_token():

    url = syntribos.extensions.vAPI.config.UserConfig(
        section_name="vAPI").url
    username = syntribos.extensions.vAPI.config.UserConfig(
        section_name="vAPI").username
    password = syntribos.extensions.vAPI.config.UserConfig(
        section_name="vAPI").password

    access_data = authenticate(url, username, password)
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
