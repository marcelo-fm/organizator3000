

class Organizator:
    def __init__(self, path) -> None:
        self.path = path
    
    def print_path(self):
        print(self.path)

o = Organizator("C:/users/m_fos/Documents")
o.print_path()