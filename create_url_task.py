"""
创建腾讯云asr任务
"""
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.asr.v20190614 import asr_client, models

def create_url_task(audio_url):
    SecretId = "*****"
    SecretKey = "****"

    try:
        cred = credential.Credential(SecretId, SecretKey)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "asr.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = asr_client.AsrClient(cred, "", clientProfile)

        req = models.CreateRecTaskRequest()
        params = {
            "EngineModelType": "16k_zh",
            "ChannelNum": 1,
            "SpeakerDiarization": 1,
            "SpeakerNumber": 2,
            "ResTextFormat": 0,
            "SourceType": 0,
            "Url": audio_url
        }
        req.from_json_string(json.dumps(params))

        resp = client.CreateRecTask(req)
        return resp.to_json_string()

    except TencentCloudSDKException as err:
        print(err)
        return None