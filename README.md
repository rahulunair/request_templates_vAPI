# Request templates for the vulnerable API(vAPI)

The vAPI, https://github.com/mattvaldes/vulnerable-api, is an API designed to be vulnerable.

These templates can be used by automated API security testing tools like Syntribos https://github.com/openstack/syntribos to test and make the tool better.
The vAPI is also a good source to learn, *what not to do* when designing a API.

Add the vAPI directory to  the local syntribos/extensions/ and the vAPI.config file in the config directory inside .opencafe. 
Edit the config file so that your credentials to the vAPI is reflected.
