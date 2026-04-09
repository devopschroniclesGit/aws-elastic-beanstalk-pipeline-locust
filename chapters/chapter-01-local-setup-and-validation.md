# Chapter 1: Local Setup and Validation of AWS Elastic Beanstalk Locust Sample

## Objective
The goal of this chapter was to begin building an **AWS-native CI/CD pipeline project from scratch** by first validating the application locally before deploying it to AWS.

The chosen sample application is the **Elastic Beanstalk Locust Load Generator** from the AWS documentation samples. This project demonstrates how to run **Locust**, a Python-based load testing tool, using Elastic Beanstalk configuration files, a `Procfile`, and supporting deployment scripts.

This chapter focuses on:
- cloning the sample application
- understanding the project structure
- fixing dependency compatibility issues
- running the application locally
- validating the Locust dashboard

---

## Project Initialization

### Clone the Sample Repository

```bash
mkdir aws-native-cicd
cd aws-native-cicd

git clone https://github.com/aws-samples/eb-locustio-sample.git
cd eb-locustio-sample
