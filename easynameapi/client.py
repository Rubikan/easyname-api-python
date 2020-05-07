from resources import Resources

class EasynameClient(Resources):
    key = None
    authsalt = None
    signsalt = None

    def __init__(self, key, authsalt, signsalt):
        self.key = key
        self.authsalt = authsalt
        self.signsalt = signsalt

    def send(self):
        # Send function used by the components, sign and send the data here
        return