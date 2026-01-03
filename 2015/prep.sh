#!/bin/bash
for i in {7..25}; do
  echo "Iteration $i"
  mkdir "day_$i"
  echo -e "import sys\nwith open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:" > "day_$i/prob_1.py"
  echo -e "import sys\nwith open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:" > "day_$i/prob_2.py"
done