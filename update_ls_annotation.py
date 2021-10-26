"""
更新label studio的标注结果
"""
import requests
import json
import uuid

def profile_format(input):
    if int(input) == 0:
        return "Speaker-0"
    else:
        return "Speaker-1"

def time_format(input):
    """
    解析时间标签
    :param input: 0:0.930
    :return: 0.930
    """
    if len(input.split(':')) != 2:
        print("Time Invalid!")
        return ""
    min, sec = input.split(':')[0], input.split(':')[1]
    res = int(min) * 60 + float(sec)
    return str(res)

def analystic(res_file):
    """
    解析转写结果
    :param res_file:
    :return:
    """
    results = []
    original_length = 0
    with open(res_file, "r") as f:
        response = json.loads(f.read())
    Result = response["Data"]["Result"].split("\n")
    for res in Result:
        if len(res.split('  ')) != 2: continue
        uid = uuid.uuid4()
        time, text = res.split('  ')
        time = time.replace('[', '').replace(']', '')
        start, end, profile = time.split(',')
        start = time_format(start)
        end = time_format(end)
        profile = profile_format(profile)
        original_length = end
        results.extend([{
            "original_length": original_length,
            "value": {
                "start": float(start),
                "end": float(end),
                "labels": [
                    profile
                ]
            },
            "id": f"wavesufer_{uid}",
            "from_name": "labels",
            "to_name": "audio",
            "type": "labels"
        },{
            "original_length": original_length,
            "value": {
                "start": float(start),
                "end": float(end),
                "text": [
                    text
                ]
            },
            "id": f"wavesufer_{uid}",
            "from_name": "transcription",
            "to_name": "audio",
            "type": "textarea"
        }])

    for res in results:
        res["original_length"] = original_length
    return results




url = "http://localhost:8080/api/tasks/3/annotations/"

headers = {
  'Authorization': 'Token ****',
  'Content-Type': 'application/json',
}

res_file = "call_history/v2_0cc357089e4385d8c1ef786f2faed49e.json"
data = dict()
data["result"] = analystic(res_file)
data["was_cancelled"] = True
data["ground_truth"] = True
data["lead_time"] = 30  # 耗时
data["task"] = 3  # 任务ID


payload = json.dumps(data)
response = requests.request("PATCH", url, headers=headers, data=payload)

print(response.text)
