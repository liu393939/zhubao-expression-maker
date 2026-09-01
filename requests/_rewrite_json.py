# -*- coding: utf-8 -*-
import json, sys, re

src = r"D:\ALLObject\助宝\zhubao-expression-maker\zhubao-expression-maker\requests\req-4x4-v1.json"
dst = r"D:\ALLObject\助宝\zhubao-expression-maker\zhubao-expression-maker\requests\req-4x4-clean.json"

with open(src, 'r', encoding='utf-8') as f:
    data = json.load(f)

# 校验
assert 'requests' in data and len(data['requests']) == 1
req = data['requests'][0]
print('aspect_ratio:', req.get('aspect_ratio'))
print('resolution:', req.get('resolution'))
print('input_urls count:', len(req.get('input_urls', [])))
print('prompt length:', len(req.get('prompt', '')))

# 压成单行 JSON 字符串（无 BOM, 无换行）
oneline = json.dumps(data, ensure_ascii=False, separators=(',', ':'))
with open(dst, 'w', encoding='utf-8', newline='') as f:
    f.write(oneline)

# 验证写回
with open(dst, 'rb') as f:
    raw = f.read()
print('written bytes:', len(raw))
print('first 8 bytes:', ' '.join(f'{b:02X}' for b in raw[:8]))
print('JSON reparse OK:', bool(json.loads(raw.decode('utf-8'))))
