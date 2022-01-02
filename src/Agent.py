from src import DiGraph


class Agent:

    def __init__(self, agent: dict = {}, location: dict = {}):
        self.agent: dict = agent
        self.location: dict = location

    def move(self, id: int, pos: int):
        self.location[id]=pos

    def add_agent(self, id: int , pos: int):
        d={id:pos}
        self.agent.update(d)

    def remove_agent(self, id: int):
        del self.agent[id]
        del self.location[id]

    def get_agent(self, id: int):
        return self.agent[id]

    def chooseNextEdge(self, id: int, ):
        return  self



