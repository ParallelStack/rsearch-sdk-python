# coding: utf-8

"""
    ParallelStack RSearch API

    REST API Specification for ParallelStack RSearch API  # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: team@parallelstack.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from rsearch_client.models.algorithm_failure_search_results import AlgorithmFailureSearchResults  # noqa: F401,E501


class AlgorithmFailure(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'search_results': 'AlgorithmFailureSearchResults'
    }

    attribute_map = {
        'search_results': 'search_results'
    }

    def __init__(self, search_results=None):  # noqa: E501
        """AlgorithmFailure - a model defined in Swagger"""  # noqa: E501

        self._search_results = None
        self.discriminator = None

        self.search_results = search_results

    @property
    def search_results(self):
        """Gets the search_results of this AlgorithmFailure.  # noqa: E501


        :return: The search_results of this AlgorithmFailure.  # noqa: E501
        :rtype: AlgorithmFailureSearchResults
        """
        return self._search_results

    @search_results.setter
    def search_results(self, search_results):
        """Sets the search_results of this AlgorithmFailure.


        :param search_results: The search_results of this AlgorithmFailure.  # noqa: E501
        :type: AlgorithmFailureSearchResults
        """
        if search_results is None:
            raise ValueError("Invalid value for `search_results`, must not be `None`")  # noqa: E501

        self._search_results = search_results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AlgorithmFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
