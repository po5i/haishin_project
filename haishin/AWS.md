## Route 53

DNS Management



## S3 (frontend)

Upload website to bucket: delidelux-dev

Configured with Bucket policy
Configured as Static Web Hosting

Endpoint: delidelux-dev.s3-website-us-west-2.amazonaws.com



## Elasticbeanstalk (backend)

Language: Python 2.7
Endpoint: http://delidelux-env.elasticbeanstalk.com
Created a new RDS for this instance (type postgres)
	User: delideluxadmin
	Password: 5Sc9dALc7mbqRdVD

http://delidelux-env.elasticbeanstalk.com/admin/