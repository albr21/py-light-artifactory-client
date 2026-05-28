# py-light-artifactory-client

A light Python client module for Artifactory.

## Usage

```python
import os
from light_artifactory_client import ArtifactoryClient

host = os.environ.get("ARTIFACTORY_URL", "http://localhost:8081/artifactory")
username = os.environ.get("ARTIFACTORY_USER", "admin")
password = os.environ.get("ARTIFACTORY_PASSWORD", "password")
client = ArtifactoryClient(host, username=username, password=password)

client.deploy_artifact("<artifactory-repository>", "deploy-test.txt", b"hello")
```

## Available Operations

- get_item_info
- get_item_properties
- get_item_statistics
- list_items
- deploy_artifact
- retrieve_artifact
- retrieve_artifact_using_uri
- delete_item
- search_aql
- search_items_by_properties

## Artifactory Reference

[Artifactory Official API Documentation](https://docs.jfrog.com/integrations/docs/jfrog-api)

## Contributing

Check out the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
