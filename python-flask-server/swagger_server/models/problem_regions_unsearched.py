# coding: utf-8

from __future__ import absolute_import
from swagger_server.models.unsearched_region_polygon import UnsearchedRegionPolygon
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class ProblemRegionsUnsearched(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, version: int=None, cache: List[UnsearchedRegionPolygon]=None):
        """
        ProblemRegionsUnsearched - a model defined in Swagger

        :param version: The version of this ProblemRegionsUnsearched.
        :type version: int
        :param cache: The cache of this ProblemRegionsUnsearched.
        :type cache: List[UnsearchedRegionPolygon]
        """
        self.swagger_types = {
            'version': int,
            'cache': List[UnsearchedRegionPolygon]
        }

        self.attribute_map = {
            'version': 'version',
            'cache': 'cache'
        }

        self._version = version
        self._cache = cache

    @classmethod
    def from_dict(cls, dikt) -> 'ProblemRegionsUnsearched':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Problem_regions_unsearched of this ProblemRegionsUnsearched.
        :rtype: ProblemRegionsUnsearched
        """
        return deserialize_model(dikt, cls)

    @property
    def version(self) -> int:
        """
        Gets the version of this ProblemRegionsUnsearched.

        :return: The version of this ProblemRegionsUnsearched.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version: int):
        """
        Sets the version of this ProblemRegionsUnsearched.

        :param version: The version of this ProblemRegionsUnsearched.
        :type version: int
        """

        self._version = version

    @property
    def cache(self) -> List[UnsearchedRegionPolygon]:
        """
        Gets the cache of this ProblemRegionsUnsearched.

        :return: The cache of this ProblemRegionsUnsearched.
        :rtype: List[UnsearchedRegionPolygon]
        """
        return self._cache

    @cache.setter
    def cache(self, cache: List[UnsearchedRegionPolygon]):
        """
        Sets the cache of this ProblemRegionsUnsearched.

        :param cache: The cache of this ProblemRegionsUnsearched.
        :type cache: List[UnsearchedRegionPolygon]
        """

        self._cache = cache
