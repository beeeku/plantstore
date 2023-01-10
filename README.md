<a href="https://www.buildwithfern.com/docs/intro">
  <img src="https://github.com/fern-api/fern/blob/main/header.png" alt="header" />
</a>

<div align="center">
  <a href="https://www.buildwithfern.com/docs" alt="documentation">Documentation</a>
  <span>&nbsp;&nbsp;•&nbsp;&nbsp;</span>
  <a href="https://discord.com/invite/JkkXumPzcG" alt="discord">Join the Discord</a>
</div>

<br />

<div align="center">
Backed by Y Combinator
</div>

---

# Plant Store API

<div align="center">
    <a href="https://www.npmjs.com/package/@fern-api/plantstore">
        <img src="https://img.shields.io/npm/v/@fern-api/plantstore?style=flat-square" alt="typescript sdk" />
    </a>
    &nbsp;&nbsp;
    <a href="#">
        <img src="https://img.shields.io/maven-central/v/io.github.fern-api/plantstore?style=flat-square" alt="java sdk" />
    </a>
    &nbsp;&nbsp;
    <a href="https://www.postman.com/fern-api/workspace/fern-plantstore">
        <img src="https://img.shields.io/badge/Postman-Collection-orange?style=flat-square" alt="postman" />
    </a>
    &nbsp;&nbsp;
    <a href="https://github.com/fern-api/plantstore-openapi">
        <img src="https://img.shields.io/badge/OpenAPI-3.1-blue?style=flat-square" alt="openapi" />
    </a>
</div>

This repo contains the example Plant Store API defined in [fern](https://github.com/fern-api/fern).

The Fern compiler translates this API definition into:

- A [Node.js SDK](https://github.com/fern-api/plantstore-node).
- A [Java SDK](https://github.com/fern-api/plantstore-java)
- An [OpenAPI description](https://github.com/fern-api/plantstore-openapi)
- A [Postman Collection](https://github.com/fern-api/plantstore-postman)

# How does it work?

The API definition is stored in [fern/api/definition](fern/api/definition). The
API Definition contains information about what endpoints, types, and errors are
used in the API. The definition is broken into smaller files such as plant.yml
and owner.yml. You can read more about the syntax of a Fern Definition in our
docs [here](https://www.buildwithfern.com/docs/definition).

In order to make sure that the definition is valid, you can use the Fern CLI.

```bash
npm install -g fern-api # Installs CLI
fern check # Checks if the definition is valid
```

## Generators

The outputs (SDKs, Postman, OpenAPI) are defined in
[generators.yml](fern/api/generators.yml). You can read more about
the syntax of `generators.yml` in our docs
[here](https://www.buildwithfern.com/docs/compiler/generate#generators-yml).

```yaml
# generators.yml
groups:
  external:
    generators:
      - name: fernapi/fern-typescript-sdk
        version: 0.0.255-1-g9405afc
        output:
          location: npm
          package-name: "@fern-api/plantstore"
          token: ${FERN_NPM_TOKEN}
        github:
          repository: fern-api/plantstore-node
      - name: fernapi/fern-java-sdk
        version: 0.0.132
        output:
          location: maven
          coordinate: io.github.fern-api:plantstore
          username: ${FERN_MAVEN_USERNAME}
          password: ${FERN_MAVEN_PASSWORD}
        github:
          repository: fern-api/plantstore-java
      - name: fernapi/fern-openapi
        version: 0.0.14
        github:
          repository: fern-api/plantstore-openapi
      - name: fernapi/fern-postman
        version: 0.0.32
        output:
          location: postman
          api-key: ${FERN_POSTMAN_API_KEY}
          workspace-id: ${FERN_POSTMAN_WORKSPACE_ID}
        github:
          repository: fern-api/plantstore-postman
```

To trigger the generators run:

```
fern generate --group external --version <version>
```

Tagging a release on this repo invokes `fern generate`, which runs the compiler
and pushes the code to the repos defined in `generators.yml`. This is configured
in a [Github workflow](https://github.com/fern-api/plantstore-api/blob/main/.github/workflows/ci.yml).
