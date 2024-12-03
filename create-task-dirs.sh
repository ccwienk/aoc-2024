#!/usr/bin/env bash

own_dir="$(dirname "${BASH_SOURCE[0]}")"
echo "$own_dir"

for d in $(seq -w 01 24); do
  tgt_dir="${own_dir}/${d}"
  mkdir -p "${tgt_dir}"
  cp "${own_dir}/util.py" "${tgt_dir}/util.py"
  first_script="${tgt_dir}/${d}.py"
  if [ ! -f "${first_script}" ]; then
    cp "${own_dir}/first-script.py" "${first_script}"
  fi
done
