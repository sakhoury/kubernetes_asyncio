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


class V1HorizontalPodAutoscalerStatus(object):
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
        'current_cpu_utilization_percentage': 'int',
        'current_replicas': 'int',
        'desired_replicas': 'int',
        'last_scale_time': 'datetime',
        'observed_generation': 'int'
    }

    attribute_map = {
        'current_cpu_utilization_percentage': 'currentCPUUtilizationPercentage',
        'current_replicas': 'currentReplicas',
        'desired_replicas': 'desiredReplicas',
        'last_scale_time': 'lastScaleTime',
        'observed_generation': 'observedGeneration'
    }

    def __init__(self, current_cpu_utilization_percentage=None, current_replicas=None, desired_replicas=None, last_scale_time=None, observed_generation=None):  # noqa: E501
        """V1HorizontalPodAutoscalerStatus - a model defined in Swagger"""  # noqa: E501

        self._current_cpu_utilization_percentage = None
        self._current_replicas = None
        self._desired_replicas = None
        self._last_scale_time = None
        self._observed_generation = None
        self.discriminator = None

        if current_cpu_utilization_percentage is not None:
            self.current_cpu_utilization_percentage = current_cpu_utilization_percentage
        self.current_replicas = current_replicas
        self.desired_replicas = desired_replicas
        if last_scale_time is not None:
            self.last_scale_time = last_scale_time
        if observed_generation is not None:
            self.observed_generation = observed_generation

    @property
    def current_cpu_utilization_percentage(self):
        """Gets the current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.  # noqa: E501

        :return: The current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_cpu_utilization_percentage

    @current_cpu_utilization_percentage.setter
    def current_cpu_utilization_percentage(self, current_cpu_utilization_percentage):
        """Sets the current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.

        current average CPU utilization over all pods, represented as a percentage of requested CPU, e.g. 70 means that an average pod is using now 70% of its requested CPU.  # noqa: E501

        :param current_cpu_utilization_percentage: The current_cpu_utilization_percentage of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """

        self._current_cpu_utilization_percentage = current_cpu_utilization_percentage

    @property
    def current_replicas(self):
        """Gets the current_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        current number of replicas of pods managed by this autoscaler.  # noqa: E501

        :return: The current_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._current_replicas

    @current_replicas.setter
    def current_replicas(self, current_replicas):
        """Sets the current_replicas of this V1HorizontalPodAutoscalerStatus.

        current number of replicas of pods managed by this autoscaler.  # noqa: E501

        :param current_replicas: The current_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """
        if current_replicas is None:
            raise ValueError("Invalid value for `current_replicas`, must not be `None`")  # noqa: E501

        self._current_replicas = current_replicas

    @property
    def desired_replicas(self):
        """Gets the desired_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        desired number of replicas of pods managed by this autoscaler.  # noqa: E501

        :return: The desired_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._desired_replicas

    @desired_replicas.setter
    def desired_replicas(self, desired_replicas):
        """Sets the desired_replicas of this V1HorizontalPodAutoscalerStatus.

        desired number of replicas of pods managed by this autoscaler.  # noqa: E501

        :param desired_replicas: The desired_replicas of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """
        if desired_replicas is None:
            raise ValueError("Invalid value for `desired_replicas`, must not be `None`")  # noqa: E501

        self._desired_replicas = desired_replicas

    @property
    def last_scale_time(self):
        """Gets the last_scale_time of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.  # noqa: E501

        :return: The last_scale_time of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._last_scale_time

    @last_scale_time.setter
    def last_scale_time(self, last_scale_time):
        """Sets the last_scale_time of this V1HorizontalPodAutoscalerStatus.

        last time the HorizontalPodAutoscaler scaled the number of pods; used by the autoscaler to control how often the number of pods is changed.  # noqa: E501

        :param last_scale_time: The last_scale_time of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: datetime
        """

        self._last_scale_time = last_scale_time

    @property
    def observed_generation(self):
        """Gets the observed_generation of this V1HorizontalPodAutoscalerStatus.  # noqa: E501

        most recent generation observed by this autoscaler.  # noqa: E501

        :return: The observed_generation of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """Sets the observed_generation of this V1HorizontalPodAutoscalerStatus.

        most recent generation observed by this autoscaler.  # noqa: E501

        :param observed_generation: The observed_generation of this V1HorizontalPodAutoscalerStatus.  # noqa: E501
        :type: int
        """

        self._observed_generation = observed_generation

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
        if not isinstance(other, V1HorizontalPodAutoscalerStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
