from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from pydantic import BaseModel, Field
from crewai_tools import SerperDevTool

class TrendingTopics(BaseModel):
    """ A Topic on Subject {subject} that is in the news and attracting attention as of date {date}"""
    name: str = Field(description="Topic Name")
    link: str = Field(description="Url of the website")
    description: str = Field(description="Reason for this Topic trending in the news")
    contents: str = Field(description='description')

class TrendingCompanyList(BaseModel):
    """ List of trending Topics that are in the news """
    companies: List[TrendingTopics] = Field(description="List of Topics trending in the news")

@CrewBase
class TrendingTopics():
    """TrendingTopics crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def curator(self) -> Agent:
        return Agent(
            config=self.agents_config['curator'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def publisher(self) -> Agent:
        return Agent(
            config=self.agents_config['publisher'],
            verbose=True
        )

    @task
    def researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['researcher_task']
        )

    @task
    def curator_task(self) -> Task:
        return Task(
            config=self.tasks_config['curator_task']
        )

    @task
    def publisher_task(self) -> Task:
        return Task(
            config=self.tasks_config['publisher_task'],
            output_pydantic=TrendingCompanyList
        )

    @crew
    def crew(self) -> Crew:
        """Creates the TrendingTopics crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
