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



class V1JobStatus(object):
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
        'active': 'int',
        'completion_time': 'datetime',
        'conditions': 'list[V1JobCondition]',
        'failed': 'int',
        'start_time': 'datetime',
        'succeeded': 'int'
    }

    attribute_map = {
        'active': 'active',
        'completion_time': 'completionTime',
        'conditions': 'conditions',
        'failed': 'failed',
        'start_time': 'startTime',
        'succeeded': 'succeeded'
    }

    def __init__(self, active=None, completion_time=None, conditions=None, failed=None, start_time=None, succeeded=None):  # noqa: E501
        """V1JobStatus - a model defined in Swagger"""  # noqa: E501

        self._active = None
        self._completion_time = None
        self._conditions = None
        self._failed = None
        self._start_time = None
        self._succeeded = None
        self.discriminator = None

        if active is not None:
            self.active = active
        if completion_time is not None:
            self.completion_time = completion_time
        if conditions is not None:
            self.conditions = conditions
        if failed is not None:
            self.failed = failed
        if start_time is not None:
            self.start_time = start_time
        if succeeded is not None:
            self.succeeded = succeeded

    @property
    def active(self):
        """Gets the active of this V1JobStatus.  # noqa: E501

        The number of actively running pods.  # noqa: E501

        :return: The active of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this V1JobStatus.

        The number of actively running pods.  # noqa: E501

        :param active: The active of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._active = active

    @property
    def completion_time(self):
        """Gets the completion_time of this V1JobStatus.  # noqa: E501

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The completion_time of this V1JobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """Sets the completion_time of this V1JobStatus.

        Represents time when the job was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param completion_time: The completion_time of this V1JobStatus.  # noqa: E501
        :type: datetime
        """

        self._completion_time = completion_time

    @property
    def conditions(self):
        """Gets the conditions of this V1JobStatus.  # noqa: E501

        The latest available observations of an object's current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :return: The conditions of this V1JobStatus.  # noqa: E501
        :rtype: list[V1JobCondition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this V1JobStatus.

        The latest available observations of an object's current state. More info: https://kubernetes.io/docs/concepts/workloads/controllers/jobs-run-to-completion/  # noqa: E501

        :param conditions: The conditions of this V1JobStatus.  # noqa: E501
        :type: list[V1JobCondition]
        """

        self._conditions = conditions

    @property
    def failed(self):
        """Gets the failed of this V1JobStatus.  # noqa: E501

        The number of pods which reached phase Failed.  # noqa: E501

        :return: The failed of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this V1JobStatus.

        The number of pods which reached phase Failed.  # noqa: E501

        :param failed: The failed of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def start_time(self):
        """Gets the start_time of this V1JobStatus.  # noqa: E501

        Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :return: The start_time of this V1JobStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this V1JobStatus.

        Represents time when the job was acknowledged by the job controller. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC.  # noqa: E501

        :param start_time: The start_time of this V1JobStatus.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def succeeded(self):
        """Gets the succeeded of this V1JobStatus.  # noqa: E501

        The number of pods which reached phase Succeeded.  # noqa: E501

        :return: The succeeded of this V1JobStatus.  # noqa: E501
        :rtype: int
        """
        return self._succeeded

    @succeeded.setter
    def succeeded(self, succeeded):
        """Sets the succeeded of this V1JobStatus.

        The number of pods which reached phase Succeeded.  # noqa: E501

        :param succeeded: The succeeded of this V1JobStatus.  # noqa: E501
        :type: int
        """

        self._succeeded = succeeded

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
        if not isinstance(other, V1JobStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
