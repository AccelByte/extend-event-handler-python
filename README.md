# extend-event-handler-python 

```mermaid
flowchart LR
   subgraph AccelByte Gaming Services
   KF[Kafka]
   KB[Kafka Connect]  
   subgraph Extend Event Handler App

   SV["gRPC Server\n(YOU ARE HERE)"]   
   end   
   KB --- SV
   KF --- KB
   end   
```

`AccelByte Gaming Services (AGS)` features can be extended by using 
`Extend Event Handler` apps. An `Extend Event Handler` is a gRPC server which
listen to Kafka events from `AGS` services via Kafka Connect and takes actions
according to a custom logic.

## Overview

This repository contains a sample `Extend Event Handler` app written in `Python`. 
It will listen to `userLoggedIn` event and then proceed to grant an entitlement 
to the said user. 

This sample app also shows the instrumentation setup necessary for 
observability. It is required so that metrics, traces, and logs are able to 
flow properly when the app is deployed.

## Project Structure

```text
...
├── src
│  ├── accelbyte_grpc_plugin
│  │  ├── __init__.py
│  │  ├── interceptors
│  │  │  ├── __init__.py
│  │  │  ├── logging.py
│  │  │  └── metrics.py
│  │  └── opts
│  │    ├── __init__.py
│  │    ├── grpc_health_checking.py
│  │    ├── grpc_reflection.py
│  │    ├── loki.py
│  │    ├── prometheus.py
│  │    └── zipkin.py
│  └── app
│    ...
│    └── services
│      ├── __init__.py
│      └── login_handler.py   # Where we put custom logic that will get called when the event 
│                             # we interested got invoked
...
```

The `AGS` event specification can be obtained [here](https://github.com/AccelByte/accelbyte-api-proto/tree/main/asyncapi/accelbyte). In this case,
we are only interested on `user logged in event`. Therefore, we only put the event specification for IAM in this sample app.

## Prerequisites

Before starting, you will need the following.

1. Windows 10 WSL2 or Linux Ubuntu 20.04 with the following installed.

   a. bash

   b. [docker v23.x](https://docs.docker.com/engine/install/ubuntu/)
   
   c. make
   
   d. python 3.9
   
   e. [grpcui](https://github.com/fullstorydev/grpcui)

2. Access to `AccelByte Gaming Services` demo environment.

   a. Base URL:

      - For `Starter` tier e.g.  https://spaceshooter.prod.gamingservices.accelbyte.io
      - For `Premium` tier e.g.  https://dev.accelbyte.io

   b. [Create a Game Namespace](https://docs.accelbyte.io/gaming-services/tutorials/how-to/create-a-game-namespace/) if you don't have one yet. Keep the `Namespace ID`.


   c. [Create an OAuth Client](https://docs.accelbyte.io/gaming-services/services/access/authorization/manage-access-control-for-applications/#create-an-iam-client) with confidential client type with the following permissions. Keep the `Client ID` and `Client Secret`.
   
   - For AGS Premium customers:
      - `ADMIN:NAMESPACE:{namespace}:USER:*:ENTITLEMENT [CREATE]`
   - For AGS Starter customers:
      - Platform Store -> Entitlement (Create)

3. A published `AGS` Store. Take a note of the `item id` which is to be granted after a user in a certain namespace successfully logged in.

## Setup

1. Create a docker compose `.env` file by copying the content of [.env.template](.env.template) file.
2. Fill in the required environment variables in `.env` file as shown below.

   ```
   AB_BASE_URL=https://demo.accelbyte.io      # Base URL of AccelByte Gaming Services demo environment
   AB_CLIENT_ID='xxxxxxxxxx'                  # Use Client ID from the Prerequisites section
   AB_CLIENT_SECRET='xxxxxxxxxx'              # Use Client Secret from the Prerequisites section
   AB_NAMESPACE='xxxxxxxxxx'                  # Use Namespace ID from the Prerequisites section
   ITEM_ID_TO_GRANT='xxxxxxxxxxx'             # Item id from a published store we noted previously
   ```

## Building

To build this sample app, use the following command.

```
make build
```

## Running

To (build and) run this sample app in a container, use the following command.

```
docker compose up --build
```

## Testing

1. Run this `Extend Event Handler` sample app by using the command below.

   ```shell
   docker compose up --build
   ```

2. Run `grpcui` with the following command.

   ```shell
   grpcui -plaintext localhost:6565
   ```

   > :warning: **If you are running [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) stack alongside this sample app as mentioned in [Test Observability](#test-observability)**: Use `localhost:10000` instead of `localhost:6565`. This way, the `gRPC server` will be called via `Envoy` service within `grpc-plugin-dependencies` stack instead of directly.

3. Now in `grpcui`, send a sample of kafka event you are interested in. In this case, we are interested in `userLoggedIn` event.
   So, we are using sample payload [here](https://docs.accelbyte.io/gaming-services/developers/api-events/iam-account/#message-userloggedin).


   ```json
   {
     "payload": {
        "userAccount": {
           "userId": "string",
           "emailAddress": "string",
           "country": "string",
           "namespace": "string"
        },
        "userAuthentication": {
           "platformId": "string",
           "refresh": true
        }
     },
     "id": "string",
     "version": 0,
     "name": "string",
     "namespace": "string",
     "parentNamespace": "string",
     "timestamp": "2019-08-24T14:15:22Z",
     "clientId": "string",
     "userId": "string",
     "traceId": "string",
     "sessionId": "string"
   }
   ```

   > :exclamation: You can change the field value you are interested in to suits your need, e.g. `namespace` , `userId`, etc

   Finally, make sure to select the right service name and method name
   and click `Invoke` to send the request.

   ![grpcui request](./docs/grpcui-request.png)


   > :exclamation: **If you are interested on other events:** you can find it [here](https://docs.accelbyte.io/gaming-services/developers/api-events/achievement/).

 
4. If successful, you will see in the response as follows and you can also see the 
   item granted to the user you are using for this test.
   
   ![grpcui response](./docs/grpcui-response.png) 

   ![granted entitlement](./docs/granted-entitlement.png)

### Test Observability

To be able to see the how the observability works in this sample app locally, there are few things that need be setup before performing tests.

1. Uncomment loki logging driver in [docker-compose.yaml](docker-compose.yaml)

   ```
    # logging:
    #   driver: loki
    #   options:
    #     loki-url: http://host.docker.internal:3100/loki/api/v1/push
    #     mode: non-blocking
    #     max-buffer-size: 4m
    #     loki-retries: "3"
   ```

   > :warning: **Make sure to install docker loki plugin beforehand**: Otherwise,
   this sample app will not be able to run. This is required so that container logs
   can flow to the `loki` service within `grpc-plugin-dependencies` stack. 
   Use this command to install docker loki plugin: `docker plugin install grafana/loki-docker-driver:latest --alias loki --grant-all-permissions`.

2. Clone and run [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) stack alongside this sample app. After this, Grafana 
will be accessible at http://localhost:3000.

   ```
   git clone https://github.com/AccelByte/grpc-plugin-dependencies.git
   cd grpc-plugin-dependencies
   docker compose up
   ```

   > :exclamation: More information about [grpc-plugin-dependencies](https://github.com/AccelByte/grpc-plugin-dependencies) is available [here](https://github.com/AccelByte/grpc-plugin-dependencies/blob/main/README.md).

3. Perform testing. For example, by following [Test in Local Development Environment](#test-in-local-development-environment).

## Deploying

After done testing, you may want to deploy this app to `AccelByte Gaming Services`.

1. [Create a new Extend Event Handler app on Admin Portal](https://docs.accelbyte.io/gaming-services/services/extend/events-handler/). Keep the `Repository URI`.
2. Download and setup [extend-helper-cli](https://github.com/AccelByte/extend-helper-cli/) (only if it has not been done previously).
3. Perform docker login with `extend-helper-cli` using the following command.
   ```
   extend-helper-cli dockerlogin --namespace <my-game> --app <my-app> --login
   ```
   > :exclamation: For your convenience, the above `extend-helper-cli` command can also be 
   copied from `Repository Authentication Command` under the corresponding app detail page.
4. Build and push sample app docker image to AccelByte ECR using the following command.
   ```
   make imagex_push IMAGE_TAG=v0.0.1 REPO_URL=xxxxxxxxxx.dkr.ecr.us-west-2.amazonaws.com/accelbyte/justice/development/extend/xxxxxxxxxx/xxxxxxxxxx
   ```
   > :exclamation: **The REPO_URL is obtained from step 1**: It can be found under 'Repository URI' in the app detail.