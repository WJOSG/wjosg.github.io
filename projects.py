class Project:
    def __init__(self, title, description, sourceurl):
        self.title = title
        self.description = description
        self.sourceurl = sourceurl

PROJECTS = [
    Project("wjmanage [WIP]", 
            "Server-based managment software for small businesses/startups. This project has just started development so there is no release yet.", 
            "https://github.com/WJOSG/wjmanage"),
]
