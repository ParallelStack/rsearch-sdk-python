# coding: utf-8

"""
    ParallelStack RSearch API

    REST API Specification for ParallelStack RSearch API

    OpenAPI spec version: 1.0.0
    Contact: team@parallelstack.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2002(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'indexes': 'InlineResponse2002Indexes'
    }

    attribute_map = {
        'indexes': 'indexes'
    }

    def __init__(self, indexes=None):
        """
        InlineResponse2002 - a model defined in Swagger
        """

        self._indexes = None

        if indexes is not None:
          self.indexes = indexes

    @property
    def indexes(self):
        """
        Gets the indexes of this InlineResponse2002.

        :return: The indexes of this InlineResponse2002.
        :rtype: InlineResponse2002Indexes
        """
        return self._indexes

    @indexes.setter
    def indexes(self, indexes):
        """
        Sets the indexes of this InlineResponse2002.

        :param indexes: The indexes of this InlineResponse2002.
        :type: InlineResponse2002Indexes
        """

        self._indexes = indexes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
