import json
import os

directory = os.path.dirname(__file__)
os.chdir(directory)
folder_path = "./batch"
folder_result = "./resultQA"


def split_and_save_json(file_path, save_path='batch', batch_size=10):
    # 폴더가 존재하지 않으면 생성
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # JSON 파일 로드
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    # 딕셔너리 아이템을 순회
    items = list(data.items())
    for i in range(0, len(items), batch_size):
        batch_data = dict(items[i:i + batch_size])
        with open(f'{save_path}/batch_{i//batch_size + 1}.json', 'w', encoding='utf-8') as batch_file:
            json.dump(batch_data, batch_file, indent=4, ensure_ascii=False)

# 예시 사용법
# split_and_save_json('result.json')


### filename 정돈 -> resultQA에 있는거 0붙여줌
import os
import re

def format_batch_filenames(folder_path):
    for file_name in os.listdir(folder_path):
        # 파일 이름에서 'batch_' 뒤에 오는 숫자 부분을 찾음
        match = re.search(r'batch_(\d+)_result', file_name)
        if match:
            number = int(match.group(1))
            # 숫자를 두 자리 형식으로
            new_number = f"{number:02d}"
            # 새 파일 이름을 생성 앞에 붙은 숫자들은 무시
            new_file_name = f"batch_{new_number}_result.json"
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(old_file_path, new_file_path)

# 함수를 호출합니다.
# format_batch_filenames(folder_result)