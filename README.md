# CORS-Proxy

A CORS proxy for various services

Instead of an nginx reverse proxy, I chose to just plug in a FastAPI route for service status & reverse proxying to Baseten(can be any provider like Replicate etc).

## Supported services

  - [x] Baseten LLM invocation


## Configs

Change out Model ID, API Key, Prefix prompt etc to your values
