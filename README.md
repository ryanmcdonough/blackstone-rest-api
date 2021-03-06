# Blackstone Web API

Blackstone is a spaCy model and library for processing long-form, unstructured legal text. 

This project wraps an API layer around Blackstone written in Python.  

## Get Started

You will need Docker installed on your machine and access to the internet. 

To start this project simply run:

`docker-compose up -d`

Running the above command starts the underlying Blackstone service as well as the API layer, 
which by default is running on port 4449 at http://localhost:4449.

## Running precompiled image

You can also pull and run this docker image from Docker Hub:

```docker pull ryanmcdonough/blackstone-api```

followed by

```docker run -p 4449:4449 ryanmcdonough/blackstone-api```


## Endpoint

All of the below endpoints accept a POST request with a JSON body that includes a "text" property. 

```json
{
  "text": "This is the text you want to process..."
}
```

### /ner

The NER component of the Blackstone model has been trained to detect the following entity types:

| Ent        | Name           | Examples  |
| ------------- |-------------| -----:|
| CASENAME    | Case names | e.g. *Smith v Jones*, *In re Jones*, In *Jones'* case |
| CITATION      | Citations (unique identifiers for reported and unreported cases)     |   e.g. (2002) 2 Cr App R 123 |
| INSTRUMENT | Written legal instruments     |    e.g. Theft Act 1968, European Convention on Human Rights, CPR |
| PROVISION | Unit within a written legal instrument   |    e.g. section 1, art 2(3) |
| COURT | Court or tribunal   |    e.g. Court of Appeal, Upper Tribunal |
| JUDGE | References to judges |    e.g. Eady J, Lord Bingham of Cornhill |

The API will return a JSON response with the following structure: 

```json

{
  "data": [{"text":  "Some identified text", "label":  "CASENAME" }]
}

```

### /legislation

Blackstone's Legislation Linker attempts to couple a reference to a PROVISION to it's parent INSTRUMENT by using the NER model to identify the presence of an INSTRUMENT and then navigating the dependency tree to identify the child provision.

Once Blackstone has identified a PROVISION:INSTRUMENT pair, it will attempt to generate target URLs to both the provision and the instrument on legislation.gov.uk.

The API will return a JSON response with the following structure: 

```json

{
  "data": [{"provision":  "Some provision found", "provision_url":  "http://www.link.to/legislation", "instrument": "Some provision found", "instrument_url" : "https://www.link.to/legislation  ]
}

```
