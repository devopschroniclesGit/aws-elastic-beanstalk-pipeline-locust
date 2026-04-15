## Final Root Cause and Fix

Initial deployment resulted in HTTP 502 errors.

Investigation on the EC2 instance showed:

- Locust successfully started on port 8089
- Nginx was forwarding traffic to port 8000

This caused:

connection refused

### Fix Applied

Updated `Procfile`:

web: locust -f locustfile.py --web-host=0.0.0.0 --web-port=8000

This aligned the application port with the Elastic Beanstalk nginx upstream configuration.

### Outcome

Locust UI successfully accessible via Elastic Beanstalk environment URL.

# IAM Troubleshooting Notes

Resolved deployment failures caused by missing permissions for:
- Elastic Beanstalk
- CloudFormation
- EC2
- SNS
- Auto Scaling
