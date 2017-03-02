# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Coordinate(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, longitude: float=None, latitude: float=None):
        """
        Coordinate - a model defined in Swagger

        :param longitude: The longitude of this Coordinate.
        :type longitude: float
        :param latitude: The latitude of this Coordinate.
        :type latitude: float
        """
        self.swagger_types = {
            'longitude': float,
            'latitude': float
        }

        self.attribute_map = {
            'longitude': 'longitude',
            'latitude': 'latitude'
        }

        self._longitude = longitude
        self._latitude = latitude

    @classmethod
    def from_dict(cls, dikt) -> 'Coordinate':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Coordinate of this Coordinate.
        :rtype: Coordinate
        """
        return deserialize_model(dikt, cls)

    @property
    def longitude(self) -> float:
        """
        Gets the longitude of this Coordinate.
        the longitude of the object.

        :return: The longitude of this Coordinate.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: float):
        """
        Sets the longitude of this Coordinate.
        the longitude of the object.

        :param longitude: The longitude of this Coordinate.
        :type longitude: float
        """

        self._longitude = longitude

    @property
    def latitude(self) -> float:
        """
        Gets the latitude of this Coordinate.
        the latitude of the object.

        :return: The latitude of this Coordinate.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: float):
        """
        Sets the latitude of this Coordinate.
        the latitude of the object.

        :param latitude: The latitude of this Coordinate.
        :type latitude: float
        """

        self._latitude = latitude

