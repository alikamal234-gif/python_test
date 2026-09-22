

class Reponse:
    def __init__(self , body , status , header = None):
        self.body = body
        self.status = status
        if header is None:
            header = {}
        self.header = header


