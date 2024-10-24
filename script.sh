#!/bin/bash

run=60

mkdir -p q1
mkdir -p q1/rw
mkdir -p q1/randrw
mkdir -p q2
mkdir -p q3
mkdir -p q4

# for i in $(seq 1 1 33)
# do
#   fio --name=output --output=temp.json --output-format=json --loops=5 --runtime=10 --time_based --numjobs=1 --rwmixwrite=33 --bs=16k --filesize=1G --readwrite=randrw --direct=0
# done

# rm temp.json
# rm output.0.0

for i in $(seq 0 12.5 100)
do
  fio --name=output --output=q1/rw/rw_$i.json --output-format=json --loops=5 --runtime=$run --time_based --numjobs=1 --rwmixwrite=$i --bs=16k --filesize=1G --readwrite=rw --direct=0
done

# for i in $(seq 0 12.5 100)
# do
#   fio --name=output --output=q1/randrw/randrw_$i.json --output-format=json --loops=5 --runtime=$run --time_based --numjobs=1 --rwmixwrite=$i --bs=16k --filesize=1G --readwrite=randrw --direct=0
# done

# for i in {10..20}
# do
#     result=$((2**i))
#     fio --name=output --output=q2/randrw_$i.json --output-format=json --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bs=$result --filesize=1G --readwrite=randrw --direct=0
# done

# #  --write_bw_log=log$i 

# fio --name=output --output=q3/randrw_30.json --output-format=json --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bssplit=4k/30 --filesize=1G --readwrite='randrw' --direct=0
# fio --name=output --output=q3/randrw_60.json --output-format=json --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bssplit=16k/60 --filesize=1G --readwrite='randrw' --direct=0
# fio --name=output --output=q3/randrw_10.json --output-format=json --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bssplit=64k/10 --filesize=1G --readwrite='randrw' --direct=0

# fio --output=q4/randrw_1.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bs=16k --filesize=1G --readwrite='randrw' --direct=0 

# for i in $(seq 2 2 8)
# do
#     fio --name=output --output=q4/randrw_$i.json --output-format=json --loops=5 --runtime=$run  --time_based --numjobs=$i --rwmixwrite=33 --bs=16k --filesize=1G --readwrite='randrw' --direct=0 
# done