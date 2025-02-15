import json
import os
from tqdm import tqdm

def create_small_dataset(input_path, output_path, percentage=0.1):
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 首先计算总行数
    total_lines = 0
    with open(input_path, 'r', encoding='utf-8') as f:
        for _ in f:
            total_lines += 1
    
    # 计算需要提取的行数
    target_lines = int(total_lines * percentage)
    print(f"Total lines: {total_lines}")
    print(f"Extracting {target_lines} lines ({percentage*100}%)")
    
    # 提取数据
    with open(input_path, 'r', encoding='utf-8') as f_in:
        with open(output_path, 'w', encoding='utf-8') as f_out:
            for i, line in tqdm(enumerate(f_in), total=target_lines, desc="Extracting data"):
                if i >= target_lines:
                    break
                f_out.write(line)
    
    # 打印结果
    output_size = os.path.getsize(output_path) / (1024 * 1024)  # Convert to MB
    print(f"\nSmall dataset created at: {output_path}")
    print(f"Size: {output_size:.2f} MB")

if __name__ == "__main__":
    input_path = "./dataset/pretrain_hq.jsonl"
    output_path = "./dataset/pretrain_hq_small.jsonl"
    create_small_dataset(input_path, output_path, percentage=0.1)
