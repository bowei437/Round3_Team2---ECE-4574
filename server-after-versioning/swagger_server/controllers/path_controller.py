import connexion
from swagger_server.models.error import Error
from swagger_server.models.path import Path
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import requests, json
from flask import jsonify
from flask_api import status
from pathfinder import *

storage_url = "http://ec2-52-41-229-1.us-west-2.compute.amazonaws.com:8080/v1/"


def get_path(problem_id):
    """
    Path
    Returns a description of the path from the robot&#39;s current location to the goal.
    :param problem_id: The id of the problem being manipulated
    :type problem_id: int

    :rtype: Path
    """
    
    #contact storage
    path_url = storage_url + str(problem_id)
    response = requests.get(path_url)

    #check that the Problem exists
    if (response.status_code == 404):
        return jsonify(Error(404, "Problem not found")), status.HTTP_404_NOT_FOUND
    
    #check if Storage died
    elif (response.status_code != 200):
        return jsonify(Error(500, "Storage server error")), status.HTTP_500_INTERNAL_SERVER_ERROR
    
    #get the Problem from the response
    problem = response.json()
    path = pathfind_from_json(problem, 1)
    return jsonify(path)

