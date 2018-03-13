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

from rsearch_client.models.search_query_search_aggregations import SearchQuerySearchAggregations  # noqa: F401,E501


class SearchQuerySearch(object):
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
        'fuzzy': 'float',
        'result_fields': 'list[str]',
        'search_fields': 'list[str]',
        'page_num': 'float',
        'page_count': 'float',
        'filters': 'object',
        'sort_fields': 'list[object]',
        'aggregations': 'list[SearchQuerySearchAggregations]'
    }

    attribute_map = {
        'query': 'query',
        'fuzzy': 'fuzzy',
        'result_fields': 'result_fields',
        'search_fields': 'search_fields',
        'page_num': 'page_num',
        'page_count': 'page_count',
        'filters': 'filters',
        'sort_fields': 'sort_fields',
        'aggregations': 'aggregations'
    }

    def __init__(self, query=None, fuzzy=None, result_fields=None, search_fields=None, page_num=None, page_count=None, filters=None, sort_fields=None, aggregations=None):  # noqa: E501
        """SearchQuerySearch - a model defined in Swagger"""  # noqa: E501

        self._query = None
        self._fuzzy = None
        self._result_fields = None
        self._search_fields = None
        self._page_num = None
        self._page_count = None
        self._filters = None
        self._sort_fields = None
        self._aggregations = None
        self.discriminator = None

        self.query = query
        if fuzzy is not None:
            self.fuzzy = fuzzy
        if result_fields is not None:
            self.result_fields = result_fields
        if search_fields is not None:
            self.search_fields = search_fields
        if page_num is not None:
            self.page_num = page_num
        if page_count is not None:
            self.page_count = page_count
        if filters is not None:
            self.filters = filters
        if sort_fields is not None:
            self.sort_fields = sort_fields
        if aggregations is not None:
            self.aggregations = aggregations

    @property
    def query(self):
        """Gets the query of this SearchQuerySearch.  # noqa: E501


        :return: The query of this SearchQuerySearch.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this SearchQuerySearch.


        :param query: The query of this SearchQuerySearch.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def fuzzy(self):
        """Gets the fuzzy of this SearchQuerySearch.  # noqa: E501


        :return: The fuzzy of this SearchQuerySearch.  # noqa: E501
        :rtype: float
        """
        return self._fuzzy

    @fuzzy.setter
    def fuzzy(self, fuzzy):
        """Sets the fuzzy of this SearchQuerySearch.


        :param fuzzy: The fuzzy of this SearchQuerySearch.  # noqa: E501
        :type: float
        """

        self._fuzzy = fuzzy

    @property
    def result_fields(self):
        """Gets the result_fields of this SearchQuerySearch.  # noqa: E501


        :return: The result_fields of this SearchQuerySearch.  # noqa: E501
        :rtype: list[str]
        """
        return self._result_fields

    @result_fields.setter
    def result_fields(self, result_fields):
        """Sets the result_fields of this SearchQuerySearch.


        :param result_fields: The result_fields of this SearchQuerySearch.  # noqa: E501
        :type: list[str]
        """

        self._result_fields = result_fields

    @property
    def search_fields(self):
        """Gets the search_fields of this SearchQuerySearch.  # noqa: E501


        :return: The search_fields of this SearchQuerySearch.  # noqa: E501
        :rtype: list[str]
        """
        return self._search_fields

    @search_fields.setter
    def search_fields(self, search_fields):
        """Sets the search_fields of this SearchQuerySearch.


        :param search_fields: The search_fields of this SearchQuerySearch.  # noqa: E501
        :type: list[str]
        """

        self._search_fields = search_fields

    @property
    def page_num(self):
        """Gets the page_num of this SearchQuerySearch.  # noqa: E501


        :return: The page_num of this SearchQuerySearch.  # noqa: E501
        :rtype: float
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this SearchQuerySearch.


        :param page_num: The page_num of this SearchQuerySearch.  # noqa: E501
        :type: float
        """

        self._page_num = page_num

    @property
    def page_count(self):
        """Gets the page_count of this SearchQuerySearch.  # noqa: E501


        :return: The page_count of this SearchQuerySearch.  # noqa: E501
        :rtype: float
        """
        return self._page_count

    @page_count.setter
    def page_count(self, page_count):
        """Sets the page_count of this SearchQuerySearch.


        :param page_count: The page_count of this SearchQuerySearch.  # noqa: E501
        :type: float
        """

        self._page_count = page_count

    @property
    def filters(self):
        """Gets the filters of this SearchQuerySearch.  # noqa: E501


        :return: The filters of this SearchQuerySearch.  # noqa: E501
        :rtype: object
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this SearchQuerySearch.


        :param filters: The filters of this SearchQuerySearch.  # noqa: E501
        :type: object
        """

        self._filters = filters

    @property
    def sort_fields(self):
        """Gets the sort_fields of this SearchQuerySearch.  # noqa: E501


        :return: The sort_fields of this SearchQuerySearch.  # noqa: E501
        :rtype: list[object]
        """
        return self._sort_fields

    @sort_fields.setter
    def sort_fields(self, sort_fields):
        """Sets the sort_fields of this SearchQuerySearch.


        :param sort_fields: The sort_fields of this SearchQuerySearch.  # noqa: E501
        :type: list[object]
        """

        self._sort_fields = sort_fields

    @property
    def aggregations(self):
        """Gets the aggregations of this SearchQuerySearch.  # noqa: E501


        :return: The aggregations of this SearchQuerySearch.  # noqa: E501
        :rtype: list[SearchQuerySearchAggregations]
        """
        return self._aggregations

    @aggregations.setter
    def aggregations(self, aggregations):
        """Sets the aggregations of this SearchQuerySearch.


        :param aggregations: The aggregations of this SearchQuerySearch.  # noqa: E501
        :type: list[SearchQuerySearchAggregations]
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
        if not isinstance(other, SearchQuerySearch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
