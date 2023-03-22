# poc-ai-ner
![](https://build.redpencil.io/api/badges/lblod/poc-ai-ner/status.svg)

This repository contains the code to get started with the NER api. This api is used to extract NER from a given text.

## Getting started
In order to run this code, you will either have to build it locally or use our pre-build container (from dockerhub lblod space).
Keep in mind that you have to supply the container with some extra configuration (mainly a mount in this case) to successfully boot it.

### Pulling the right model from GCS bucket
In order to easily pull a model from a GCS bucket, you could use the gsutil cli toolkit.

Once you have successfully installed the toolkit, you can easily get your model by running the folowing command:
```
gsutil -m cp -r  gs://abb-textgen-models/NER-model .
```

### Starting the docker container
You start with pooling the container form the dockerhub
```
docker pull lblod/poc-ai-ner
```

In order to start you have to execute the following command
```
docker run -it --rm  -p 8080:8080 -v <folder_containing_the_model(s)>:/models/ lblod/poc-ai-keywords
```
### Swagger api docs
```json
{"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/":{"get":{"summary":"Health Check Route","description":"This function is a simple health check --> Could be relevant if you are using liveliness/readiness checks.","operationId":"Health_check_route__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/health_response"}}}}}}},"/get_ner_entities":{"get":{"summary":"This Route Is Made To Get The Ner'S For A Document","description":"This function extract the Named entities from a file and returns them.\n\n:param input_text: The content of a file\n:param confidence_score: a threshold for the confidence from the NER\n:return: a dict formatted list of NER entities that were found from the text","operationId":"This_route_is_made_to_get_the_NER_s_for_a_document_get_ner_entities_get","parameters":[{"required":true,"schema":{"title":"Input Text","type":"string"},"name":"input_text","in":"query"},{"required":false,"schema":{"title":"Confidence Score","type":"number","default":0.6},"name":"confidence_score","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{"$ref":"#/components/schemas/ner_entities_response"}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"anyOf":[{"type":"string"},{"type":"integer"}]}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}},"health_response":{"title":"health_response","required":["status"],"type":"object","properties":{"status":{"title":"Status","type":"string"}}},"inner_ner_entities_response":{"title":"inner_ner_entities_response","required":["token","tag","start_pos","end_pos","confidence_score"],"type":"object","properties":{"token":{"title":"Token","type":"string"},"tag":{"title":"Tag","type":"string"},"start_pos":{"title":"Start Pos","type":"integer"},"end_pos":{"title":"End Pos","type":"integer"},"confidence_score":{"title":"Confidence Score","type":"number"}}},"ner_entities_response":{"title":"ner_entities_response","required":["result"],"type":"object","properties":{"result":{"title":"Result","type":"array","items":{"$ref":"#/components/schemas/inner_ner_entities_response"}}}}}}}
```


NER extractor by ML2Grow
