#!/bin/bash
# validate_stale_refs.sh
# Detect stale chapter references.

echo "=== Checking for stale chapter references ==="
FOUND=0

# Check for old chapter references
for file in docs/*.md *.md; do
  [ -f "$file" ] || continue
  
  if grep -n '第11章\|第12章\|ch11\.md\|ch12\.md' "$file" >/dev/null 2>&1; then
    grep -n '第11章\|第12章\|ch11\.md\|ch12\.md' "$file" | while read -r match; do
      echo "  WARN: $file: $match"
    done
    FOUND=1
  fi
done

if [ $FOUND -eq 0 ]; then
  echo "OK: No stale chapter references detected."
fi
