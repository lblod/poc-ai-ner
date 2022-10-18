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
NER extractor by ML2Grow
