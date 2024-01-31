# How to use:
## requirements:
manually create a bucket and upload '/cloudformation/modules', the bucket will be used to store the cloudformation templates, and will be used by codebuild and codepipeline.
create a zip file named my-application.zip and add the Dockerfile and code, in the repo is already this zip file with python app that just show my resume.
in the bucket create a folder named "app" and upload my-application.zip
## optional:
you can upload the main.yaml to the bucket so when create the stack just specify the url for it
    
## first run:
### GUI:
go to cloudformation and create a stack -> upload the file or set the Url in s3 for main.yaml -> fill the parameters, about env for now just will acept dev,stage,prod
continue with all the default configurations for the stack and create it.
### Cli:
`aws cloudformation create-stack --template-body file://main.yaml --stack-name {{name}} --parameters ParameterKey=bucket,ParameterValue={{bucket-name}} ParameterKey=email,ParameterValue={{emailForAlerts}} ParameterKey=env,ParameterValue{{dev/stage/prod}}`
- if the main.yaml is in the bucket you can change --template-body for --template-url
### comments:
this will take some time and in the first run will deploy a container with amazon-ecs-sample but when codepipeline finish the app will be deployed.
##  general comments:
- to ensure 0 downtime in deploys the service is configurated with a min of 100% nad max 200, so when a deploy is performed will duplicate the containers.
- about security: there is two security groups a public and private, the one that use the ALB just allow traffic to http from everywhere and the one that is used by ecs just allow traffic to http that comes from resources that has the public security group.
- also there is a ACL to just allow inbound to http, https and ephemeral ports for the nat gateway. about outbound I allow all.
- to reduce the resources created and the side of the files I just created one role normally I'll create a role for each resource or purpuse. 

