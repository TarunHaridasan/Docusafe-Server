class Document:
    #Initialize
    def __init__(self, documentName, fp, thumbnailFp):
        self.name = documentName
        self.fp = fp
        self.thumbnailFp = thumbnailFp
        self.encription = 0