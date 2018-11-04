# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class V1Taint(object):
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
        'effect': 'str',
        'key': 'str',
        'time_added': 'datetime',
        'value': 'str'
    }

    attribute_map = {
        'effect': 'effect',
        'key': 'key',
        'time_added': 'timeAdded',
        'value': 'value'
    }

    def __init__(self, effect=None, key=None, time_added=None, value=None):  # noqa: E501
        """V1Taint - a model defined in Swagger"""  # noqa: E501

        self._effect = None
        self._key = None
        self._time_added = None
        self._value = None
        self.discriminator = None

        self.effect = effect
        self.key = key
        if time_added is not None:
            self.time_added = time_added
        if value is not None:
            self.value = value

    @property
    def effect(self):
        """Gets the effect of this V1Taint.  # noqa: E501

        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :return: The effect of this V1Taint.  # noqa: E501
        :rtype: str
        """
        return self._effect

    @effect.setter
    def effect(self, effect):
        """Sets the effect of this V1Taint.

        Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.  # noqa: E501

        :param effect: The effect of this V1Taint.  # noqa: E501
        :type: str
        """
        if effect is None:
            raise ValueError("Invalid value for `effect`, must not be `None`")  # noqa: E501

        self._effect = effect

    @property
    def key(self):
        """Gets the key of this V1Taint.  # noqa: E501

        Required. The taint key to be applied to a node.  # noqa: E501

        :return: The key of this V1Taint.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this V1Taint.

        Required. The taint key to be applied to a node.  # noqa: E501

        :param key: The key of this V1Taint.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def time_added(self):
        """Gets the time_added of this V1Taint.  # noqa: E501

        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.  # noqa: E501

        :return: The time_added of this V1Taint.  # noqa: E501
        :rtype: datetime
        """
        return self._time_added

    @time_added.setter
    def time_added(self, time_added):
        """Sets the time_added of this V1Taint.

        TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.  # noqa: E501

        :param time_added: The time_added of this V1Taint.  # noqa: E501
        :type: datetime
        """

        self._time_added = time_added

    @property
    def value(self):
        """Gets the value of this V1Taint.  # noqa: E501

        Required. The taint value corresponding to the taint key.  # noqa: E501

        :return: The value of this V1Taint.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this V1Taint.

        Required. The taint value corresponding to the taint key.  # noqa: E501

        :param value: The value of this V1Taint.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, V1Taint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
