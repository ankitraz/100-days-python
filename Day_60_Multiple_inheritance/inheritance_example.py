class Stream:
    def __init__(self) -> None:
        self.isOpen = False

    def open(self):

        if self.isOpen:
            print("file is already opened.")
        else:
            self.isOpen = True
            print("Opening file...")
    
    def close(self):
        if self.isOpen:
            self.isOpen = False
            print("Closing file...")
        else:
            print("File is already closed!")


# s = Stream()
# s.open()
# s.close()