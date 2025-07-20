import os

background_dir = 'background'
output_file = 'all_images.js'  # 可选：输出到单独的js文件

# 获取所有jpg文件名（不区分大小写）
image_files = [f for f in os.listdir(background_dir) if f.lower().endswith('.jpg')]

# 生成JS数组字符串
js_array = 'const allImages = [\n'
for name in image_files:
    js_array += f'  "{name}",\n'
js_array += '];\n'

# 输出到控制台
print(js_array)

# 可选：写入到js文件
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(js_array)

print(f'已生成 {len(image_files)} 个文件名到 allImages 数组。')