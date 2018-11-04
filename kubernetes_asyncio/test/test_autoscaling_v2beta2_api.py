# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.12.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import kubernetes_asyncio.client
from kubernetes_asyncio.client.api.autoscaling_v2beta2_api import AutoscalingV2beta2Api  # noqa: E501
from kubernetes_asyncio.client.rest import ApiException


class TestAutoscalingV2beta2Api(unittest.TestCase):
    """AutoscalingV2beta2Api unit test stubs"""

    def setUp(self):
        self.api = kubernetes_asyncio.client.api.autoscaling_v2beta2_api.AutoscalingV2beta2Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_namespaced_horizontal_pod_autoscaler(self):
        """Test case for create_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_collection_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_collection_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_delete_namespaced_horizontal_pod_autoscaler(self):
        """Test case for delete_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_get_api_resources(self):
        """Test case for get_api_resources

        """
        pass

    def test_list_horizontal_pod_autoscaler_for_all_namespaces(self):
        """Test case for list_horizontal_pod_autoscaler_for_all_namespaces

        """
        pass

    def test_list_namespaced_horizontal_pod_autoscaler(self):
        """Test case for list_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler(self):
        """Test case for patch_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for patch_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler(self):
        """Test case for read_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for read_namespaced_horizontal_pod_autoscaler_status

        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler(self):
        """Test case for replace_namespaced_horizontal_pod_autoscaler

        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler_status(self):
        """Test case for replace_namespaced_horizontal_pod_autoscaler_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
