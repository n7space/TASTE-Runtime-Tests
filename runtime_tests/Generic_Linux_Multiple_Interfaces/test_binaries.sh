#!/bin/bash

cd "$( dirname "${BASH_SOURCE[0]}" )"

./work/binaries/partition_2 & pid1=$!
./work/binaries/partition_1 & pid2=$!

function kill_binaries
{
	kill $pid1
	kill $pid2
}

trap "kill_binaries" SIGINT

wait $pid1 $pid2
