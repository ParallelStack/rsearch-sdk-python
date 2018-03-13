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

from rsearch_client.models.suggest_failure_suggest_results import SuggestFailureSuggestResults  # noqa: F401,E501


class SuggestFailure(object):
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
        'suggest_results': 'SuggestFailureSuggestResults'
    }

    attribute_map = {
        'suggest_results': 'suggest_results'
    }

    def __init__(self, suggest_results=None):  # noqa: E501
        """SuggestFailure - a model defined in Swagger"""  # noqa: E501

        self._suggest_results = None
        self.discriminator = None

        if suggest_results is not None:
            self.suggest_results = suggest_results

    @property
    def suggest_results(self):
        """Gets the suggest_results of this SuggestFailure.  # noqa: E501


        :return: The suggest_results of this SuggestFailure.  # noqa: E501
        :rtype: SuggestFailureSuggestResults
        """
        return self._suggest_results

    @suggest_results.setter
    def suggest_results(self, suggest_results):
        """Sets the suggest_results of this SuggestFailure.


        :param suggest_results: The suggest_results of this SuggestFailure.  # noqa: E501
        :type: SuggestFailureSuggestResults
        """

        self._suggest_results = suggest_results

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
        if not isinstance(other, SuggestFailure):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
