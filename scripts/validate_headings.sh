#!/bin/bash
# validate_headings.sh
# Detect duplicated headings across chapters.

echo "=== Checking for duplicated headings ==="

# Extract all headings and count occurrences
grep -rh '^#' docs/*.md | sed 's/^#* *//' | sort | uniq -c | sort -rn | while read -r count heading; do
  if [ "$count" -gt 1 ]; then
    echo "  WARN: Heading appears $count times: '$heading'"
  fi
done

echo "OK: Heading check complete."
