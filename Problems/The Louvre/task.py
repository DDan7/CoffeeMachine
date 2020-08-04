class Painting:
    museum = "Louvre"

    def __init__(self, title, painter, year):
        self.title = title
        self.painter = painter
        self.year = year

    def info(self):
        print('"{0}" by {1} ({2}) hangs in the {3}.'.format(self.title,
                                                            self.painter,
                                                            self.year,
                                                            Painting.museum))


paintings = Painting(input(), input(), input())
paintings.info()
