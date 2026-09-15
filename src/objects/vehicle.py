"""
This module defines the Vehicle class and its associated properties and methods.
Inspired by the agent.py class in the CSP_ABM project by Lu Yu see https://github.com/yululeah/CSP_ABM/blob/main/agent.py
"""

import mesa
import numpy as np
import pandas as pd
import seaborn as sb
import model


class Vehicle(mesa.Agent):
    def __init__(
        self, model: model.Model, fuel_type: str, max_speed: float, lat: float, lon: float, pos: int, destination: int
    ) -> None:

        super().__init__(model)
        self.fuel_type = fuel_type
        self.max_speed = max_speed
        # Initialize the position of the vehicle
        self.lat = lat
        self.lon = lon
        self.pos = pos
        self.distance_along_edge = 0
        self.route = []
        self.currentRoad = None
        self.route_index = 0
        self.pos_igraph_id = None
        self.destination = destination
        # We need to load some real Geopandas dataframe data to use index - 14/09
        self.destination_igraph_id = self.model.nodes.index.get_loc(self.destination)
        self.target = self.destination_igraph_id
        # Current speed of vehicle in miles per hour.
        self.current_vehicle_speed = 30 #mi/h 


    def get_fuel_type(self) -> str:
        return self.fuel_type

    def get_max_speed(self) -> float:
        return self.max_speed

    def get_position(self) -> tuple:
        return (self.lat, self.lon)

    def set_fuel_type(self, fuel_type: str) -> None:
        self.fuel_type = fuel_type

    def set_max_speed(self, max_speed: float) -> None:
        self.max_speed = max_speed

    def update_position(self, lat: float, lon: float) -> None:
        # Position will be based on the coordinate system of the environment either lat, lng or cartesian coordinates
        self.lat = lat
        self.lon = lon

    def update_location(self) -> None:
        """Update when driving"""
        total_distance = self.distance_to_next_node() + self.distance_along_edge
        origin_node = self.model.nodes.loc[self.route[self.route_index]]

        if self.route_index == len(self.route) - 1 or total_distance == 0:
            self.update_position(lat=origin_node.geometry.y, lon=origin_node.geometry.x)
        else:
            k = self.distance_along_edge / total_distance
            destination_node = self.model.nodes.loc[
                self.route[self.route_index + 1]
            ]  # select a random location within the available routes.
            self.update_position(
                lat=k * destination_node.geometry.y + (1 - k) * origin_node.geometry.y,
                lon=k * destination_node.geometry.x + (1 - k) * origin_node.geometry.x,
            )

        self.pos_igraph_id = self.model.nodes.index.get_loc(self.pos)


    def update_route(self) -> None:
        '''
        Update the vehicle's route to the next segment.
        This method should be called when the vehicle reaches the end of its current route segment.
        '''
        path = self.model.igraph.get_shortest_path(self.pos_igraph_id, self.target, weights="length")[0]
        # Route returns a list of multidigraph node id 
        self.route = self.model.nodes.iloc[path].index
        self.route_index = 0
        self.distance_along_edge = 0
        self.current_vehicle_speed = 30


    def distance_to_next_node(self) -> int:
        if len(self.route) <= 1:
            return 0
        elif self.route_index == len(self.route) - 1:
            self.finish()
            return 100000000000
        else:
            edge = self.model.network.get_edge_data(self.route[self.route_index], self.route[self.route_index + 1])
            if 'osmid' in edge[0].keys():
                self.currentRoad = edge[0]['osmid']
            s = edge[0]['length'] - self.distance_along_edge
            if s > 0:
                return s
            else:
                self.finish()
                return 100000000000



""" TIPS
self.model.agents -> a list of agents currently in the model. If you use random.choice(self.model.agents) a random active agent is selected.
"""
