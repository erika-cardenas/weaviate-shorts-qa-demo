import weaviate
import json

client = weaviate.Client("http://localhost:8080")

with open('data.json', 'r') as f:
    data = json.load(f, strict = False)


for shorts in data["WeaviateShorts"]:
  properties = {
    "question": shorts["question"],
    "content": shorts["content"]
  }
  client.data_object.create(
    data_object=properties,
    class_name= "WeaviateShorts"
  )
