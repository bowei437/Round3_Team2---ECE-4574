# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.boundary import Boundary
from swagger_server.models.goal import Goal
from swagger_server.models.obstacle import Obstacle
from swagger_server.models.robot import Robot
from swagger_server.models.searched_region_lidar import SearchedRegionLIDAR
from swagger_server.models.unsearched_region_polygon import UnsearchedRegionPolygon
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Problem(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, problem_id: int=None, robots: List[Robot]=None, goal: Goal=None, boundary: Boundary=None, obstacles: List[Obstacle]=None, unsearched_region: UnsearchedRegionPolygon=None, searched_region: SearchedRegionLIDAR=None):
        """
        Problem - a model defined in Swagger

        :param problem_id: The problem_id of this Problem.
        :type problem_id: int
        :param robots: The robots of this Problem.
        :type robots: List[Robot]
        :param goal: The goal of this Problem.
        :type goal: Goal
        :param boundary: The boundary of this Problem.
        :type boundary: Boundary
        :param obstacles: The obstacles of this Problem.
        :type obstacles: List[Obstacle]
        :param unsearched_region: The unsearched_region of this Problem.
        :type unsearched_region: UnsearchedRegionPolygon
        :param searched_region: The searched_region of this Problem.
        :type searched_region: SearchedRegionLIDAR
        """
        self.swagger_types = {
            'problem_id': int,
            'robots': List[Robot],
            'goal': Goal,
            'boundary': Boundary,
            'obstacles': List[Obstacle],
            'unsearched_region': UnsearchedRegionPolygon,
            'searched_region': SearchedRegionLIDAR
        }

        self.attribute_map = {
            'problem_id': 'problem_id',
            'robots': 'robots',
            'goal': 'goal',
            'boundary': 'boundary',
            'obstacles': 'obstacles',
            'unsearched_region': 'unsearchedRegion',
            'searched_region': 'searchedRegion'
        }

        self._problem_id = problem_id
        self._robots = robots
        self._goal = goal
        self._boundary = boundary
        self._obstacles = obstacles
        self._unsearched_region = unsearched_region
        self._searched_region = searched_region

    @classmethod
    def from_dict(cls, dikt) -> 'Problem':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Problem of this Problem.
        :rtype: Problem
        """
        return deserialize_model(dikt, cls)

    @property
    def problem_id(self) -> int:
        """
        Gets the problem_id of this Problem.

        :return: The problem_id of this Problem.
        :rtype: int
        """
        return self._problem_id

    @problem_id.setter
    def problem_id(self, problem_id: int):
        """
        Sets the problem_id of this Problem.

        :param problem_id: The problem_id of this Problem.
        :type problem_id: int
        """

        self._problem_id = problem_id

    @property
    def robots(self) -> List[Robot]:
        """
        Gets the robots of this Problem.
        The list of robots for the problem

        :return: The robots of this Problem.
        :rtype: List[Robot]
        """
        return self._robots

    @robots.setter
    def robots(self, robots: List[Robot]):
        """
        Sets the robots of this Problem.
        The list of robots for the problem

        :param robots: The robots of this Problem.
        :type robots: List[Robot]
        """

        self._robots = robots

    @property
    def goal(self) -> Goal:
        """
        Gets the goal of this Problem.

        :return: The goal of this Problem.
        :rtype: Goal
        """
        return self._goal

    @goal.setter
    def goal(self, goal: Goal):
        """
        Sets the goal of this Problem.

        :param goal: The goal of this Problem.
        :type goal: Goal
        """

        self._goal = goal

    @property
    def boundary(self) -> Boundary:
        """
        Gets the boundary of this Problem.

        :return: The boundary of this Problem.
        :rtype: Boundary
        """
        return self._boundary

    @boundary.setter
    def boundary(self, boundary: Boundary):
        """
        Sets the boundary of this Problem.

        :param boundary: The boundary of this Problem.
        :type boundary: Boundary
        """

        self._boundary = boundary

    @property
    def obstacles(self) -> List[Obstacle]:
        """
        Gets the obstacles of this Problem.

        :return: The obstacles of this Problem.
        :rtype: List[Obstacle]
        """
        return self._obstacles

    @obstacles.setter
    def obstacles(self, obstacles: List[Obstacle]):
        """
        Sets the obstacles of this Problem.

        :param obstacles: The obstacles of this Problem.
        :type obstacles: List[Obstacle]
        """

        self._obstacles = obstacles

    @property
    def unsearched_region(self) -> UnsearchedRegionPolygon:
        """
        Gets the unsearched_region of this Problem.

        :return: The unsearched_region of this Problem.
        :rtype: UnsearchedRegionPolygon
        """
        return self._unsearched_region

    @unsearched_region.setter
    def unsearched_region(self, unsearched_region: UnsearchedRegionPolygon):
        """
        Sets the unsearched_region of this Problem.

        :param unsearched_region: The unsearched_region of this Problem.
        :type unsearched_region: UnsearchedRegionPolygon
        """

        self._unsearched_region = unsearched_region

    @property
    def searched_region(self) -> SearchedRegionLIDAR:
        """
        Gets the searched_region of this Problem.

        :return: The searched_region of this Problem.
        :rtype: SearchedRegionLIDAR
        """
        return self._searched_region

    @searched_region.setter
    def searched_region(self, searched_region: SearchedRegionLIDAR):
        """
        Sets the searched_region of this Problem.

        :param searched_region: The searched_region of this Problem.
        :type searched_region: SearchedRegionLIDAR
        """

        self._searched_region = searched_region
