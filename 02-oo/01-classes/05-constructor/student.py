class Wall:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth
        self.volume = height * width * depth