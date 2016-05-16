import json

import requests

import syntribos.extensions.vAPI.config


def authenticate(url, username=None, password=None):

    url = '{0}/tokens'.format(url)

    kwargs = {}
    kwargs["username"] = username
    kwargs["password"] = password
    data = {"auth": {"passwordCredentials": kwargs}}
    r = requests.post(url, data=json.dumps(data))

    if not r.ok:
        raise Exception("Failed to authenticate")

    if r.entity is None:
        raise Exception("Failed to parse Auth response Body")
    return r


def get_token():

    username = syntribos.extensions.vAPI.config.UserConfig(
        section_name="credentials").url
    password = syntribos.extensions.vAPI.config.UserConfig(
        section_name="credentials").username
    url = syntribos.extensions.vAPI.config.UserConfig(
        section_name="credentials").password

    access_data = authenticate(url, username, password)
    return access_data["access"]["token"]["id"]
