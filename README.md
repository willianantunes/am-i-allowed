# Am I allowed?

TODO.

## How to run the project

Download and run [LM Studio](https://lmstudio.ai/) locally. Download the model `Wizard-Vicuna-7B-Uncensored-GGUF` created by [TheBloke](https://huggingface.co/TheBloke) through its UI. When it's done you can load the model and run the API server. You'll have the following supported endpoints:

```text
GET  http://192.168.0.20:1234/v1/models
POST http://192.168.0.20:1234/v1/chat/completions
POST http://192.168.0.20:1234/v1/completions
POST http://192.168.0.20:1234/v1/embeddings
```

It follows OpenAI's API structure. It means we can use the [OpenAI library](https://pypi.org/project/openai/).

## Must read articles

- [OpenAPI Platform: Key Concepts](https://platform.openai.com/docs/concepts/key-concepts)
- [Entendendo o Básico de IA e Redes Neurais - IAs vão te substituir?](https://www.youtube.com/live/UDrDg6uUOVs?si=9f5yZJH2HsCurSbf)
- [Qdrant: Indexing](https://qdrant.tech/documentation/concepts/indexing/)
- [PostgreSQL as a Vector Database: A pgvector Tutorial](https://www.timescale.com/blog/postgresql-as-a-vector-database-create-store-and-query-openai-embeddings-with-pgvector/)
- [Timescale Vector Cookbook](https://github.com/timescale/vector-cookbook/)
