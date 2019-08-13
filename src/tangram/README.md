# Tangram

## About

A test program using Google Gloud Run for doing shacl conversion via pyshacl.  

## Tangram:  Simple service example

The Tangram services is a web services  wrapper around the pySHACL
(https://github.com/RDFLib/pySHACL) package.  It allows you to send in JSON-LD data 
graphs to test against a Turtle (ttl) encoded shape graph.

Invoke the tool with something like:

With httpie client:

```bash
http -f POST https://tangram.geodex.org/uploader  datagraph@./datagraphs/dataset-minimal-BAD.json-ld  shapegraph@./shapegraphs/googleRecommended.ttl format=human
```

Or with good old curl (with format set to huam):

```bash
curl -F  'datagraph=@./datagraphs/dataset-minimal-BAD.json-ld'  -F  'shapegraph=@./shapegraphs/googleRecommended.ttl' -F 'format=human'  https://tangram.geodex.org/uploader
```


## Refs
* https://cloud.google.com/run/docs/quickstarts/build-and-deploy



httpclient "http://localhost:8080/netcheck?url=http://opencoredata.org/id/dataset/5f475e43-6e23-44f6-821b-795d5f1f82d2&format=human&shape=required"


