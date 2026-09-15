"""

This is the main entry point for the ParkSim simulation.
It initializes the simulation environment and runs the simulation loop.
"""

import mesa
from model import Model
import osmnx
import networkx as nx
import igraph as ig
import geopandas as gpd


# Defining main function
def main():
    # Load Data
    place = "Chippenham"
    G = osmnx.graph_from_place(place, network_type = 'drive', 
                               simplify = False, retain_all = True, truncate_by_edge = True)

    G = osmnx.add_edge_speeds(G)
    G = osmnx.add_edge_travel_times(G)

    # nodes is a GeoDataFrame indexed by the osmnx node id (osmid).
    # Its index is what Vehicle uses to resolve destination -> destination_igraph_id.
    nodes, edges = osmnx.graph_to_gdfs(G)

    nx.write_gml(G, f'{place}.gml')

    # Build an igraph graph from the networkx graph so that positional
    # (igraph) indices line up with the order of `nodes`. get_loc on the
    # nodes index returns exactly these positional ids.
    iigraph = ig.Graph.from_networkx(G)

    # Thread the real data through to the Model (and therefore to each Vehicle):
    #   - iigraph:    python-igraph graph used for shortest-path routing
    #   - network:    the networkx MultiDiGraph used for edge lookups
    #   - nodes_data: the GeoDataFrame parsed into Model.nodes / Vehicle
    simulation_object = Model(
        n=100,
        iigraph=iigraph,
        network=G,
        nodes_data=nodes,
    )
    simulation_object.run_for(50)

    print(f"Total Agents: {len(simulation_object.agents)}")

    for agent in simulation_object.agents.select(at_most=5):
        print(
            f"  Agent {agent.unique_id}: max speed={agent.max_speed}, fuel type={agent.fuel_type}"
        )


# Using the special variable
# __name__
if __name__ == "__main__":
    main()
