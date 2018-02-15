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


class SuggestQuerySuggest(object):
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
        'query': 'str',
        'fields': 'list[str]',
        'fuzzy': 'float',
        'size': 'float'
    }

    attribute_map = {
        'query': 'query',
        'fields': 'fields',
        'fuzzy': 'fuzzy',
        'size': 'size'
    }

    def __init__(self, query=None, fields=None, fuzzy=None, size=None):  # noqa: E501
        """SuggestQuerySuggest - a model defined in Swagger"""  # noqa: E501

        self._query = None
        self._fields = None
        self._fuzzy = None
        self._size = None
        self.discriminator = None

        self.query = query
        self.fields = fields
        self.fuzzy = fuzzy
        self.size = size

    @property
    def query(self):
        """Gets the query of this SuggestQuerySuggest.  # noqa: E501


        :return: The query of this SuggestQuerySuggest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SuggestQuerySuggest.


        :param query: The query of this SuggestQuerySuggest.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def fields(self):
        """Gets the fields of this SuggestQuerySuggest.  # noqa: E501


        :return: The fields of this SuggestQuerySuggest.  # noqa: E501
        :rtype: list[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SuggestQuerySuggest.


        :param fields: The fields of this SuggestQuerySuggest.  # noqa: E501
        :type: list[str]
        """
        if fields is None:
            raise ValueError("Invalid value for `fields`, must not be `None`")  # noqa: E501

        self._fields = fields

    @property
    def fuzzy(self):
        """Gets the fuzzy of this SuggestQuerySuggest.  # noqa: E501


        :return: The fuzzy of this SuggestQuerySuggest.  # noqa: E501
        :rtype: float
        """
        return self._fuzzy

    @fuzzy.setter
    def fuzzy(self, fuzzy):
        """Sets the fuzzy of this SuggestQuerySuggest.


        :param fuzzy: The fuzzy of this SuggestQuerySuggest.  # noqa: E501
        :type: float
        """
        if fuzzy is None:
            raise ValueError("Invalid value for `fuzzy`, must not be `None`")  # noqa: E501

        self._fuzzy = fuzzy

    @property
    def size(self):
        """Gets the size of this SuggestQuerySuggest.  # noqa: E501


        :return: The size of this SuggestQuerySuggest.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this SuggestQuerySuggest.


        :param size: The size of this SuggestQuerySuggest.  # noqa: E501
        :type: float
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

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
        if not isinstance(other, SuggestQuerySuggest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
