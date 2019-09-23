#!/bin/sh

while read line
do
      echo "$line"
      curl -s https://fence.gleaner.io/fencepull?url=$line | curl -F  'datagraph=@-'  -F  'shapegraph=@./shapegraphs/P418Required.ttl' -F 'format=human'  https://tangram.gleaner.io/uploader
done < "${1:-/dev/stdin}"
