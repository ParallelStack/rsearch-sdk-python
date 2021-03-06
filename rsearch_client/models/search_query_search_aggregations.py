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


class SearchQuerySearchAggregations(object):
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
        'field_name': 'str',
        'agg_type': 'str',
        'term_agg_size': 'float',
        'range': 'list[object]',
        'origin': 'list[object]',
        'buckets': 'float'
    }

    attribute_map = {
        'field_name': 'field_name',
        'agg_type': 'agg_type',
        'term_agg_size': 'term_agg_size',
        'range': 'range',
        'origin': 'origin',
        'buckets': 'buckets'
    }

    def __init__(self, field_name=None, agg_type=None, term_agg_size=None, range=None, origin=None, buckets=None):  # noqa: E501
        """SearchQuerySearchAggregations - a model defined in Swagger"""  # noqa: E501

        self._field_name = None
        self._agg_type = None
        self._term_agg_size = None
        self._range = None
        self._origin = None
        self._buckets = None
        self.discriminator = None

        self.field_name = field_name
        self.agg_type = agg_type
        if term_agg_size is not None:
            self.term_agg_size = term_agg_size
        if range is not None:
            self.range = range
        if origin is not None:
            self.origin = origin
        if buckets is not None:
            self.buckets = buckets

    @property
    def field_name(self):
        """Gets the field_name of this SearchQuerySearchAggregations.  # noqa: E501


        :return: The field_name of this SearchQuerySearchAggregations.  # noqa: E501
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this SearchQuerySearchAggregations.


        :param field_name: The field_name of this SearchQuerySearchAggregations.  # noqa: E501
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")  # noqa: E501

        self._field_name = field_name

    @property
    def agg_type(self):
        """Gets the agg_type of this SearchQuerySearchAggregations.  # noqa: E501


        :return: The agg_type of this SearchQuerySearchAggregations.  # noqa: E501
        :rtype: str
        """
        return self._agg_type

    @agg_type.setter
    def agg_type(self, agg_type):
        """Sets the agg_type of this SearchQuerySearchAggregations.


        :param agg_type: The agg_type of this SearchQuerySearchAggregations.  # noqa: E501
        :type: str
        """
        if agg_type is None:
            raise ValueError("Invalid value for `agg_type`, must not be `None`")  # noqa: E501
        allowed_values = ["term", "range", "histogram", "location"]  # noqa: E501
        if agg_type not in allowed_values:
            raise ValueError(
                "Invalid value for `agg_type` ({0}), must be one of {1}"  # noqa: E501
                .format(agg_type, allowed_values)
            )

        self._agg_type = agg_type

    @property
    def term_agg_size(self):
        """Gets the term_agg_size of this SearchQuerySearchAggregations.  # noqa: E501


        :return: The term_agg_size of this SearchQuerySearchAggregations.  # noqa: E501
        :rtype: float
        """
        return self._term_agg_size

    @term_agg_size.setter
    def term_agg_size(self, term_agg_size):
        """Sets the term_agg_size of this SearchQuerySearchAggregations.


        :param term_agg_size: The term_agg_size of this SearchQuerySearchAggregations.  # noqa: E501
        :type: float
        """

        self._term_agg_size = term_agg_size

    @property
    def range(self):
        """Gets the range of this SearchQuerySearchAggregations.  # noqa: E501


        :return: The range of this SearchQuerySearchAggregations.  # noqa: E501
        :rtype: list[object]
        """
        return self._range

    @range.setter
    def range(self, range):
        """Sets the range of this SearchQuerySearchAggregations.


        :param range: The range of this SearchQuerySearchAggregations.  # noqa: E501
        :type: list[object]
        """

        self._range = range

    @property
    def origin(self):
        """Gets the origin of this SearchQuerySearchAggregations.  # noqa: E501


        :return: The origin of this SearchQuerySearchAggregations.  # noqa: E501
        :rtype: list[object]
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this SearchQuerySearchAggregations.


        :param origin: The origin of this SearchQuerySearchAggregations.  # noqa: E501
        :type: list[object]
        """

        self._origin = origin

    @property
    def buckets(self):
        """Gets the buckets of this SearchQuerySearchAggregations.  # noqa: E501


        :return: The buckets of this SearchQuerySearchAggregations.  # noqa: E501
        :rtype: float
        """
        return self._buckets

    @buckets.setter
    def buckets(self, buckets):
        """Sets the buckets of this SearchQuerySearchAggregations.


        :param buckets: The buckets of this SearchQuerySearchAggregations.  # noqa: E501
        :type: float
        """

        self._buckets = buckets

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
        if not isinstance(other, SearchQuerySearchAggregations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
