"""
The MESA model object that initialises all agents, steps agent activation and allows the model to run.
"""

import numpy as np
import pandas as pd
import seaborn as sns
import mesa

from vehicle import Vehicle


class Model(mesa.Model):
    def __init__(self, n=100) -> None:
        super().__init__()
        engine_type = ["EV", "ICEV"]
        # random_ids = np.random.uniform(0, self.n, size = self.n)

        Vehicle.create_agents(
            model=self,
            n=n,
            fuel_type=self.random.choices(engine_type, k=n),
            max_speed=120.0,
        )

    def step(self):
        # Actions agents undertake per timestep.
        # Random activation — each agent acts in a random order
        self.agents.shuffle_do("accelerate") # randomly activate the agents and run the accelerate function.
        
