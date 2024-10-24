#!/bin/bash

mkdir -p q1
mkdir -p q1/seq
mkdir -p q1/rand
mkdir -p q2
mkdir -p q3
mkdir -p q4

run=60
seqQ1=q1/seq
randQ1=q1/rand
q2=q2
q3=q3
q4=q4

for i in $(seq 0 12.5 100)
do
  fio --output=$seqQ1/rw_$i.json --output-format=json --name=output --loops=5 --runtime=$run --time_based --numjobs=1 --rwmixwrite=$i --bs=16k --filesize=1G --readwrite=rw --direct=0
done

for i in $(seq 0 12.5 100)
do
  fio --output=$randQ1/randrw_$i.json --output-format=json --name=output --loops=5 --runtime=$run --time_based --numjobs=1 --rwmixwrite=$i --bs=16k --filesize=1G --readwrite=randrw --direct=0
done


for i in {10..20}
do
    result=$((2**i))
    fio --output=$q2/randrw_$i.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bs=$result --filesize=1G --readwrite='randrw' --direct=0
done

# #  --write_bw_log=log$i 

fio --output=$q3/randrw_30.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bssplit=4k/30   --filesize=1G --readwrite='randrw' --direct=0
fio --output=$q3/randrw_60.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bssplit=16k/60  --filesize=1G --readwrite='randrw' --direct=0
fio --output=$q3/randrw_10.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bssplit=64k/10  --filesize=1G --readwrite='randrw' --direct=0


fio --output=$q4/randrw_1.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=1 --rwmixwrite=33 --bs=16k --filesize=1G --readwrite='randrw' --direct=0 
for i in $(seq 2 2 8)
do
    fio --output=$q4/randrw_$i.json --output-format=json --name=output --loops=5 --runtime=$run  --time_based --numjobs=$i --rwmixwrite=33 --bs=16k --filesize=1G --readwrite='randrw' --direct=0 
done