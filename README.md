## Usage

### Deployment

In order to deploy the example, you need to run the following command:

```
serverless deploy
```

After running deploy, you should see output similar to:

```
Deploying "aws-python" to stage "dev" (us-east-1)

✔ Service deployed to stack aws-python-dev (90s)

functions:
  hello: aws-python-dev-hello (1.9 kB)
```

### Invocation

After successful deployment, you can invoke the deployed function by using the following command:

```
serverless invoke --function handler --path s3Event.json
```

Which should result in response similar to the following:

```json
{
  "statusCode": 200,
  "body": "{\"message\": \"Go Serverless v4.0! Your function executed successfully!\"}"
}
```

### Local development

You can invoke your function locally by using the following command:

```
serverless invoke local --function handler
```

Which should result in response similar to the following:

```
{
  "statusCode": 200,
  "body": "{\"message\": \"Go Serverless v4.0! Your function executed successfully!\"}"
}
```

### Bundling dependencies

In case you would like to include third-party dependencies, you will need to use a plugin called `serverless-python-requirements`. You can set it up by running the following command:

```
serverless plugin install -n serverless-python-requirements
```

Running the above will automatically add `serverless-python-requirements` to `plugins` section in your `serverless.yml` file and add it as a `devDependency` to `package.json` file. The `package.json` file will be automatically created if it doesn't exist beforehand. Now you will be able to add your dependencies to `requirements.txt` file (`Pipfile` and `pyproject.toml` is also supported but requires additional configuration) and they will be automatically injected to Lambda package during build process. For more details about the plugin's configuration, please refer to [official documentation](https://github.com/UnitedIncome/serverless-python-requirements).
