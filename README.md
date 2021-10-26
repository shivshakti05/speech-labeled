# speech-labeled
auto speech recognize and labeled with label-studio

[中文文档](https://yanhuibin315.github.io/2021/10/26/%E4%BD%BF%E7%94%A8label-studio%E6%A0%87%E6%B3%A8%E9%9F%B3%E9%A2%91%E6%96%87%E4%BB%B6/)

# Requirements
- Python38
- [tencent cloud](https://cloud.tencent.com/product/asr)
- [label studio](https://labelstud.io/)

# Usage
## 1. Clone code
```shell
git clone git@github.com:yanhuibin315/speech-labeled.git
``` 

## 2. Install package
```shell
pip install -r requirements.txt
```

## 3. Change your tencent account
files need input secret-id & secret-key
- create_url_task.py
- get_url_res.py

## 4. Get Tencent ASR Result
```shell
python main.py
```

## 5. Create label studio project
- Labeling Setup Chose:
Audio/Speech Processing -> Automatic SPeech Recognize using Segment
![](https://raw.githubusercontent.com/yanhuibin315/yanhuibin315.github.io/master/img/label-studio-1.png)

## 6. Update Annotations
```shell
python update_ls_annotation.py
```

## 7. Labeled on label studio by yourself
![](https://raw.githubusercontent.com/yanhuibin315/yanhuibin315.github.io/master/img/label-studio-2.png)