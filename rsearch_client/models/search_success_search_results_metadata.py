# coding: utf-8

"""
    ParallelStack RSearch API

    REST API Specification for ParallelStack RSearch API  # noqa: E501

    OpenAPI spec version: 1.2.1
    Contact: team@parallelstack.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SearchSuccessSearchResultsMetadata(object):
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
        'number_search_results': 'float',
        'query': 'str',
        'aggregations': 'object'
    }

    attribute_map = {
        'number_search_results': 'number_search_results',
        'query': 'query',
        'aggregations': 'aggregations'
    }

    def __init__(self, number_search_results=None, query=None, aggregations=None):  # noqa: E501
        """SearchSuccessSearchResultsMetadata - a model defined in Swagger"""  # noqa: E501

        self._number_search_results = None
        self._query = None
        self._aggregations = None
        self.discriminator = None

        self.number_search_results = number_search_results
        self.query = query
        if aggregations is not None:
            self.aggregations = aggregations

    @property
    def number_search_results(self):
        """Gets the number_search_results of this SearchSuccessSearchResultsMetadata.  # noqa: E501


        :return: The number_search_results of this SearchSuccessSearchResultsMetadata.  # noqa: E501
        :rtype: float
        """
        return self._number_search_results

    @number_search_results.setter
    def number_search_results(self, number_search_results):
        """Sets the number_search_results of this SearchSuccessSearchResultsMetadata.


        :param number_search_results: The number_search_results of this SearchSuccessSearchResultsMetadata.  # noqa: E501
        :type: float
        """
        if number_search_results is None:
            raise ValueError("Invalid value for `number_search_results`, must not be `None`")  # noqa: E501

        self._number_search_results = number_search_results

    @property
    def query(self):
        """Gets the query of this SearchSuccessSearchResultsMetadata.  # noqa: E501


        :return: The query of this SearchSuccessSearchResultsMetadata.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchSuccessSearchResultsMetadata.


        :param query: The query of this SearchSuccessSearchResultsMetadata.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def aggregations(self):
        """Gets the aggregations of this SearchSuccessSearchResultsMetadata.  # noqa: E501


        :return: The aggregations of this SearchSuccessSearchResultsMetadata.  # noqa: E501
        :rtype: object
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this SearchSuccessSearchResultsMetadata.


        :param aggregations: The aggregations of this SearchSuccessSearchResultsMetadata.  # noqa: E501
        :type: object
        """

        self._aggregations = aggregations

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
        if not isinstance(other, SearchSuccessSearchResultsMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other