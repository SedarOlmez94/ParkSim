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
            fuel_type=self.random.choices(engine_type, k=1),
            max_speed=120.0,
        )
