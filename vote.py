import json
import os  # 导入os模块用于文件夹操作

# 定义目标文件夹路径（请替换为你的实际文件夹路径）
folder_path = "./selection"

# 初始化字典来统计prompt出现次数和存储category映射
prompt_count = {}
prompt_to_category = {}

# 遍历文件夹中的所有文件
for file_name in os.listdir(folder_path):
    # 筛选出JSON文件
    if file_name.endswith(".json"):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        prompts = data['prompt']
        categories = data['category']
        
        # 遍历当前文件的每个prompt和category
        for i, prompt in enumerate(prompts):
            # 如果prompt尚未在prompt_to_category中，则存储当前category（优先使用先出现的文件）
            if prompt not in prompt_to_category:
                prompt_to_category[prompt] = categories[i]
            # 更新prompt出现次数
            prompt_count[prompt] = prompt_count.get(prompt, 0) + 1  # 简化计数逻辑

# 筛选出出现次数大于等于2的prompt
common_prompts = []
common_categories = []
for prompt, count in prompt_count.items():
    if count >= 2:
        common_prompts.append(prompt)
        common_categories.append(prompt_to_category[prompt])

# 构建新的数据字典
common_data = {
    'prompt': common_prompts,
    'category': common_categories
}

# 保存为新的JSON文件
with open('./inputs/selected_prompts.json', 'w', encoding='utf-8') as f:
    json.dump(common_data, f, ensure_ascii=False, indent=4)

print(f"共同prompt数量: {len(common_prompts)}")
print("文件已保存为 'common_prompts.json'")