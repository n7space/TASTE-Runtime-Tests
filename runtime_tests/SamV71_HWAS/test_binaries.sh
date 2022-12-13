#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )" || exit

pushd work/binaries > /dev/null || exit

runSamV71Binary.py partition_2 -v vConsole -u remote_serial0 > /dev/null & pid1=$!

while [ ! -L "remote_serial0" ]
do
    sleep 1
done

./partition_1 & pid2=$!
cat vConsole & pid3=$!

popd > /dev/null || exit

function kill_binaries
{
	kill "$pid1"
	kill "$pid2"
	kill "$pid3"
}

trap "kill_binaries" SIGINT

wait "$pid1" "$pid2" "$pid3"
