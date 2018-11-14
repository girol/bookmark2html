class BookmarkGroup:
    '''A bookmark group/folder, with a name, bookmarks and subgroups'''
    
    def __init__(self,name):
        self.name = name
        self.subgroups = []
        self.bookmarks = []

