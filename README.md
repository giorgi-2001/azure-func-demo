# Azure Function - Demo

Azure Function example ([docs](https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python#create-your-local-project))


- This fucntion does in memory CRUD operations
- Input validation is implemented with Pydantic
- Cleaned up project structure

### To test locally there are two options:
```shell
docker build -t funcappdemo .
docker run -p 8080:80 funcappdemo
```

```shell
# Install Azure core tools
func start --verbose
```

### Deployment does not work currently for free subscription!
Thanks Azure for this
