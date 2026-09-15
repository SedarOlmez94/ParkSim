"""
The MESA model object that initialises all agents, steps agent activation and allows the model to run.
"""

import numpy as np
import pandas as pd
import seaborn as sns
from mesa import Model
from mesa.space import NetworkGrid
from mesa.datacollection import DataCollector
from vehicle import Vehicle
import geopandas
from geopandas import GeoDataFrame, sjoin
from typing import Optional


class Model(Model):
    def __init__(self, n=100, iigraph = [], network = [], nodes_data: Optional[GeoDataFrame] = None) -> None:
        super().__init__()
        engine_type = ["EV", "ICEV"]
        self.igraph = iigraph
        self.network = network
        self.nodes = nodes_data
        # random_ids = np.random.uniform(0, self.n, size = self.n)

        # Sample real node ids from the GeoDataFrame index so that each
        # Vehicle's `destination` is a valid osmnx node id. Vehicle then
        # resolves it via self.model.nodes.index.get_loc(self.destination)
        # into a positional igraph id (self.destination_igraph_id).
        node_ids = self.nodes.index.to_numpy()
        destinations = self.random.choices(list(node_ids), k=n)

        Vehicle.create_agents(
            model=self,
            n=n,
            fuel_type=self.random.choices(engine_type, k=n),
            max_speed=120.0,
            lat=0.0,
            lon=0.0,
            pos=0,
            destination=destinations,  # A valid osmnx node id per agent
        )

    

    def step(self):
        # Actions agents undertake per timestep.
        # Random activation — each agent acts in a random order
        # self.agents.shuffle_do("accelerate") # randomly activate the agents and run the accelerate function.
        pass
