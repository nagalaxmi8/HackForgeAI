from pydantic import BaseModel

class ProjectRequest(BaseModel):
    project_idea: str
    team_size: int
    skills: list[str]
    deadline_days: int