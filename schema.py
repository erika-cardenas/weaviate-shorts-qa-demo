import weaviate
import json 

client = weaviate.Client("http://localhost:8080")


class_obj = {
    "class": "WeaviateShorts", 
    "description": "Quick answers to various questions",
    "properties": [
        {
            "name": "question",
            "dataType": ["string"],
            "description": "Questions from the document",
        },
        {
            "name": "content",
            "dataType": ["string"],
            "description": "Answers to the questions",
        }
    ]
}

# resetting the schema 
client.schema.delete_all()

# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))