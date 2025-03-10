class ProjectList:
    def __init__(self, projects):
        self.projects = projects
    def __len__(self):
        return len(self.projects)

pl = ProjectList(["پروژه A", "پروژه B", "پروژه C"])
print(len(pl))