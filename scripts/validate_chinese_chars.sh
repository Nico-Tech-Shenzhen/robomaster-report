#!/bin/bash
# validate_chinese_chars.sh
# Detect suspicious simplified Chinese characters in Japanese prose.

SUSPICIOUS="开源|赛季|区域赛|全国赛|参赛|培训|算法|硬件|小组|组委会|智能|点云|封装|单板|增益|交流赛|成本价|课堂|赛场|职场"

echo "=== Checking for suspicious Chinese characters ==="
FOUND=0

for file in docs/ch*.md *.md; do
  [ -f "$file" ] || continue
  # Skip dic.md and references.md
  case "$file" in
    dic.md|references.md) continue ;;
  esac
  
  # Check each line, excluding URLs, code blocks, and table rows
  while IFS= read -r line; do
    # Skip URLs, code blocks, table rows, headings
    if echo "$line" | grep -qE '^\s*```|^\s*#|^\s*\||https?://'; then
      continue
    fi
    
    match=$(echo "$line" | grep -oP "$SUSPICIOUS" | head -1)
    if [ -n "$match" ]; then
      echo "  WARN: $file: found '$match' in: ${line:0:80}"
      FOUND=1
    fi
  done < "$file"
done

if [ $FOUND -eq 0 ]; then
  echo "OK: No suspicious simplified Chinese characters detected."
fi
