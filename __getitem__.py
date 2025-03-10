class ProjectList:
    def __init__(self, projects):
        self.projects = projects
        
    def __getitem__(self, index):
        return self.projects[index]
        
pl = ProjectList(["پروژه A", "پروژه B", "پروژه C"])
print(pl[1])