# MCP Server on Cloud Run

A Model Context Protocol (MCP) server deployed on Google Cloud Run that provides mathematical operations and joke retrieval functionality. The tools are trivial as its just for testing connectivity with MCP clients.

## Features
* __Mathematical Operations__: Simple addition and subtraction functions

* __Joke API Integration__: Fetch random jokes and programming-themed jokes from the Official Joke API

* __Cloud Ready__: Designed for deployment on Google Cloud Run with proper configuration

* __Async Support__: Built with asynchronous operations for better performance

## Tools

### 1. Add Two Numbers

Adds the second number from the first and returns the result.

__Parameters__:

`a`: First integer (minuend)

`b`: Second integer (subtrahend)

__Returns__: Addition between the two numbers

### 2. Substract Two Numbers

Subtracts the second number from the first and returns the result.

__Parameters__:

`a`: First integer (minuend)

`b`: Second integer (subtrahend)

__Returns__: Difference between the two numbers

### 3. Get Random Joke

Fetches a random joke from the Official Joke API. It has no input.

__Returns__: A joke with setup and punchline format. It-s a Json Response, for example:

```json
{
  "type": "general",
  "setup": "Why is seven bigger than nine?",
  "punchline": "Because seven ate nine.",
  "id": 377
}

```

### 4. Get Programming Joke
Fetches a random programming-themed joke from the Official Joke API.

__Returns__: A programming-related joke with setup and punchline. The data is also a JSON

```json
[
  {
    "type": "programming",
    "setup": "To understand what recursion is...",
    "punchline": "You must first understand what recursion is",
    "id": 27
  }
]

```

## NOTE:

This repo is evidence and an example of a simple implementation in Cloud Run, but its not meant to be a guide of how to create one.There are a lot more requirements for making this project that involve creating accounts, downloading sdks, etc. To create your own remote mcp follow this guide:

https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes

This documentation is mainly to inform about the MCP tools, its input and return values. The MCP uses __SSE__. The url to acces it is the following:

https://mcp-server-918538880326.us-central1.run.app/sse

