from media import(Media)
class Series(Media):
    def __init__(self, n, d, r, l, k, ep):
       Media.__init__(self, n, d, r, l, k)
       self.episode = ep