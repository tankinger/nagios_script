#!/bin/sh
#author : chen-xl
#date : 2014-02-18
#describe : Monitor physical memory
#version : 2
#
totalM=`free -m | awk 'NR==2{print $2}'`
freeM=`free -m | awk 'NR==2{print $4}'`
usedM=`free -m | awk 'NR==2{print $3}'`
mfree=`echo "scale=0; $freeM*100 / $totalM " | bc`%
mused=`echo "scale=0; $usedM*100 / $totalM " | bc`%
if [ $freeM -ge 150 ]; then
  echo "Memory usage(OK): total: $totalM Mb - used: $usedM Mb ($mused) - free: $freeM Mb ($mfree)"
  exit 0
elif [ $freeM -lt 150 ] && [ $freeM -gt 80 ];then
  echo "Memory usage(Warning): total: $totalM Mb - used: $usedM Mb ($mused) - free: $freeM Mb ($mfree)"
  exit 1
else
  echo "Memory usage (Critcal): total: $totalM Mb - used: $usedM Mb ($mused) - free: $freeM Mb ($mfree)"
  exit 2
fi
