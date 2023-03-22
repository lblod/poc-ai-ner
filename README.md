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
{"openapi":"3.0.2","info":{"title":"FastAPI","version":"0.1.0"},"paths":{"/":{"get":{"summary":"Health Check Route","operationId":"Health_check_route__get","responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}}}}},"/get_gen_keywords":{"get":{"summary":"This Route Is To Extract Keywords From Generated Text That Is Created From A Prompt","description":"Takes a text; generates a large text body using text generation api and does keyword extraction\non this text body.\n\n:param text_prompt:str text to generate keywords for\n:return:Dict containing keywords in a list in the form of {\"result\":{\"keywords\":keywords}}","operationId":"This_route_is_to_extract_keywords_from_generated_text_that_is_created_from_a_prompt_get_gen_keywords_get","parameters":[{"required":true,"schema":{"title":"Text Prompt","type":"string"},"name":"text_prompt","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}},"/get_text_keywords":{"get":{"summary":"This Route Is Made To Extract Keywords From A Document","description":"Takes a text generates a large text body using text generation api and does keyword extraction\non this text body.\n\n:param text_prompt:str text to generate keywords for\n:return:Dict containing keywords in a list in the form of {\"result\":{\"keywords\":keywords}}","operationId":"This_route_is_made_to_extract_keywords_from_a_document_get_text_keywords_get","parameters":[{"required":true,"schema":{"title":"Doc Text","type":"string"},"name":"doc_text","in":"query"}],"responses":{"200":{"description":"Successful Response","content":{"application/json":{"schema":{}}}},"422":{"description":"Validation Error","content":{"application/json":{"schema":{"$ref":"#/components/schemas/HTTPValidationError"}}}}}}}},"components":{"schemas":{"HTTPValidationError":{"title":"HTTPValidationError","type":"object","properties":{"detail":{"title":"Detail","type":"array","items":{"$ref":"#/components/schemas/ValidationError"}}}},"ValidationError":{"title":"ValidationError","required":["loc","msg","type"],"type":"object","properties":{"loc":{"title":"Location","type":"array","items":{"anyOf":[{"type":"string"},{"type":"integer"}]}},"msg":{"title":"Message","type":"string"},"type":{"title":"Error Type","type":"string"}}}}}}
```


NER extractor by ML2Grow
