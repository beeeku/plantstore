# Plant Store API

Tagging a release on this repository will update the:

- [Node.js SDK repo](https://github.com/fern-plantstore/plantstore-node)
- [Java SDK repo](https://github.com/fern-plantstore/plantstore-java)
- [OpenAPI description repo](https://github.com/fern-plantstore/plantstore-openapi)
- [Postman Collection repo](https://github.com/fern-plantstore/plantstore-postman)
- _More SDKs to come..._

## What is in this repository?

This repository contains

- Plant Store's Fern API Definition which lives in the [definition](./fern/api/definition/) folder
- Generators (see [generators.yml](./fern/api/generators.yml))

## What is in the API Definition?

The API Definition contains information about what endpoints, types, and errors are used in the API. The definition is broken into smaller files such as [plant.yml](fern/api/definition/plant.yml) and [owner.yml](fern/api/definition/owner.yml).

In order to make sure that the definition is valid, you can use the Fern CLI.

```bash
npm install -g fern-api # Installs CLI
fern check # Checks if the definition is valid
```

## What are generators?

Generators read in your API Definition and output artifacts (e.g. the TypeScript SDK Generator) and are tracked in [generators.yml](./fern/api/generators.yml).

To trigger the generators run:

```bash
fern generate --group external --version <version>
```

This command currently runs in a GitHub workflow (see [ci.yml](.github/workflows/ci.yml#L32))
