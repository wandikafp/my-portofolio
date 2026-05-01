from dataclasses import dataclass
from typing import Optional


@dataclass
class Project:
    """Data class untuk menyimpan informasi proyek."""
    id: str
    title: str
    description: str
    long_description: str
    tools: list[str]
    image_url: str
    github_url: Optional[str] = None
    demo_url: Optional[str] = None
    metrics: Optional[dict[str, str]] = None
    challenges: Optional[list[str]] = None
    outcomes: Optional[list[str]] = None

    def __init__(self, id, title, description, long_description, tools, 
                 image_url, github_url, demo_url, metrics, challenges, outcomes):
        self.id = id
        self.title = title
        self.description = description
        self.long_description = long_description
        self.tools = tools
        self.image_url = image_url
        self.github_url = github_url
        self.demo_url = demo_url
        self.metrics = metrics
        self.challenges = challenges
        self.outcomes = outcomes