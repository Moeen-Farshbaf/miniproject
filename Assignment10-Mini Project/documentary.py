from media import(Media)
class Documentary(Media):
    def __init__(self, n, d, r, l, k, rc):
       Media.__init__(self, n, d, r, l, k)
       self.realitycheck = rc

