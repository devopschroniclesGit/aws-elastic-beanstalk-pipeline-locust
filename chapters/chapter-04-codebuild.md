# Chapter 4: AWS Codepipeline CI/CD Automation
## Pipeline Flow
- Source: Github
- Build: AWS Codebuild
- Deploy: Elastic Beanstalk

## Build Process
Codebuild pulls the latest code from Github, installs dependencies,
runs build commands, and prepares deployment artifacts.

## Deployment
Successful builds are automatically deployed to Elastic Beanstalk.
