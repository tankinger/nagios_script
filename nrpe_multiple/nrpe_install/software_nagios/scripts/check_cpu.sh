#!/bin/sh
# Filename: check_cpu.sh
# Version 0.0.2 - Jan/2009
# Changes: improved grabbing of the idle cpu time
#
# by Thiago Varela -
procinfo=`which procinfo 2>/dev/null`
sar=`which sar 2>/dev/null`
function help {
 echo -e "\n\tThis plugin shows the % of used CPU, using either procinfo or sar (whichever is available)\n\n\t$0:\n\t\t-c <integer>\tIf the % of used CPU is above <integer>, returns CRITICAL state\n\t\t-w <integer>\tIf the % of used CPU is below CRITICAL and above <integer>, returns WARNING state\n"
 exit -1
}
# Getting parameters:
while getopts "w:c:h" OPT; do
 case $OPT in
  "w") warning=$OPTARG;;
  "c") critical=$OPTARG;;
  "h") help;;
 esac
done
# Checking parameters:
( [ "$warning" == "" ] || [ "$critical" == "" ] ) && echo "ERROR: You must specify warning and critical levels" && help
[[ "$warning" -ge  "$critical" ]] && echo "ERROR: critical level must be highter than warning level" && help
# Assuring that the needed tools exist:
( ( [ -f $procinfo ] && command="procinfo") ||  [ -f $sar ] ) || \
 ( echo "ERROR: You must have either procinfo or sar installer in order to run this plugin" && exit -1 )
# Doing the actual check:
( [ "$command" == "procinfo" ] && idle=`$procinfo | grep idle | cut -d% -f1 | awk '{print $NF}' | cut -d. -f1`) || \
 idle=`$sar | tail -1 | awk '{print $8}' | cut -d. -f1`
used=`expr 100 - $idle`
# Comparing the result and setting the correct level:
if [[ $used -ge $critical ]]; then
        msg="CRITICAL"
        status=2
else if [[ $used -ge $warning ]]; then
        msg="WARNING"
        status=1
     else
        msg="OK"
        status=0
     fi
fi
# Printing the results:
echo "$msg - CPU used=$used% idle=$idle% | 'CPU Usage'=$used%;$warning;$critical;"
# Bye!
exit $status