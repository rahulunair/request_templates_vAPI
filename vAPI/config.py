import cafe.engine.models.data_interfaces as data_interfaces


class UserConfig(data_interfaces.ConfigSectionInterface):
    SECTION_NAME = 'credentials'

    @property
    def url(self):
        return self.get("url")

    @property
    def username(self):
        return self.get("username")

    @property
    def password(self):
        return self.get_raw("password")
