'''Use to interact with a deployment post-setup'''

from jujuclient import Environment as JujuEnv


class Environment(object):
    def __init__(self, bootstrap, admin_secret, port=17070):
        self.env = JujuEnv("ws://%s:%d" % (bootstrap, port))
        self.env.login(admin_secret)

    def configure(self, service, options=None):
        if not options:
            return

        self.env.set_config(service, options)

    def add_unit(self, service):
        self.add_unit(service, 1)

    def add_units(self, service, num_units=1):
        if not isinstance(num_units, int):
            raise ValueError("num_units is not an int")

        self.env.add_units(service, num_units)

    def remove_unit(self, unit):
        if not isinstance(unit, list):
            units = [unit]

        self.remove_units(units)

    def remove_units(self, units):
        if not isinstance(units, list):
            raise ValueError('Expected a list a list of units')

        self.env.remove_units(units)

    def expose(self, service):
        self.env.expose(service)

    def unexpose(self, service):
        self.env.unexpose(service)
