from media import Media
class Film(Media):
    def __init__(self, n, d, r, l, k, dur):
       Media.__init__(self, n, d, r, l, k)
       self.duration = dur