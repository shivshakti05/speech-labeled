"""
根据任务ID查询腾讯转写任务结果
"""
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models


def get_url_res(task_id):
    SecretId = "*****"
    SecretKey = "*****"
    try:
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile)

        req = models.DescribeTaskStatusRequest()
        params = {
            "TaskId": task_id
        }
        req.from_json_string(json.dumps(params))

        resp = client.DescribeTaskStatus(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)
        return None