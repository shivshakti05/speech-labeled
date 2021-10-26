"""
1. 获取文件共享链接
2. 创建文件转写任务
3. 请求转写任务结果
4. 保存到json文件中
"""
from create_url_task import create_url_task
from get_url_res import get_url_res
import json
import time
import os
file_list = os.listdir("E:\\asr_dataset\\")  
res_file_list = os.listdir("results")

if __name__ == '__main__':
    for file in file_list:
        file_name = file.replace(".mp3", "")
        if f"{file_name}.json" in res_file_list: continue
        audio_url = f"https://storage.googleapis.com/{yourstorage}/{file}"
        print(audio_url)
        create_task_res = create_url_task(audio_url)
        print(create_task_res)
        if create_task_res is None: break
        create_task_res = json.loads(create_task_res)
        task_id = create_task_res["Data"]["TaskId"]
        task_tag = True
        get_task_res = ""
        time.sleep(5)
        while task_tag:
            get_task_res = get_url_res(task_id)
            get_task_res = json.loads(get_task_res)
            if "Data" in get_task_res and "Result" in get_task_res["Data"] and len(get_task_res["Data"]["Result"]) > 0:
                task_tag = False
            else:
                time.sleep(3)
        print(get_task_res)
        with open(f'results/{file_name}.json', 'w') as f:
            json.dump(get_task_res, f, ensure_ascii=False)
