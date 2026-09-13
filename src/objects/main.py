'''

This is the main entry point for the ParkSim simulation.
It initializes the simulation environment and runs the simulation loop.
'''

import mesa
from model import Model


# Defining main function
def main():
    simulation_object = Model(100)
    simulation_object.run_for(50)

    print(f"Total Agents: {len(simulation_object.agents)}")


    for agent in simulation_object.agents.select(at_most = 5):
        print(
            f"  Agent {agent.unique_id}: max speed={agent.max_speed}, fuel type={agent.fuel_type}"
        )




# Using the special variable 
# __name__
if __name__=="__main__":
    main()


