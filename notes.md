 httpclient -f POST 127.0.0.1:8080/uploader  datagraph@./datagraphs/dataset-full-BAD.json-ld  shapegraph@./shapegraphs/googleRecommended.ttl
 httpclient -f POST http://tangram.gleaner.io/uploader  datagraph@./datagraphs/dataset-minimal.json-ld  shapegraph@./shapegraphs/googleRequired.ttl format=human
