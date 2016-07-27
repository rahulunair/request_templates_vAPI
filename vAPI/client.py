import json
import random
import string

import requests

from oslo_config import cfg


CONF = cfg.CONF


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

    vAPI_group = cfg.OptGroup(name="vAPI", title="vAPI config")
    CONF.register_group(vAPI_group)
    CONF.register_opts(list_vAPI_opts(), group=vAPI_group)

    url = CONF.vAPI.url
    username = CONF.vAPI.username
    password = CONF.vAPI.password

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


def list_vAPI_opts():
    return [
        cfg.StrOpt("url", default="", help="vAPI endpoint URL"),
        cfg.StrOpt("username", default="", help="vAPI username"),
        cfg.StrOpt("password", default="", help="vAPI user password",
                   secret=True)
    ]
