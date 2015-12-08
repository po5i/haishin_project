## Route 53

Created Hosted zones for delidelux.cl and delidelux.com.ar
Created Record Set for root and www ALIAS to the buckets (same name)
Created Record Set for api CNAME to the Beanstalk server



## S3 (frontend)

Upload website to buckets: delidelux.cl and delidelux.com.ar

Configured as Static Web Hosting

Configured with Bucket policy:
{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "Allow Public Access to All Objects",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::delidelux.cl/*"
		}
	]
}

Upload django media files to bucket: delidelux-uploads
Add new management user: delidelux-uploads-manager
	Access Key ID:
	AKIAITAAK2ZMRAEMLUOA
	Secret Access Key:
	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
	ARN:
	arn:aws:iam::901942307332:user/delidelux-uploads-manager

Bucket Policy:
{
	"Version": "2012-10-17",
	"Id": "Policy1432345065244",
	"Statement": [
		{
			"Sid": "Stmt1432345054072",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:*",
			"Resource": "arn:aws:s3:::delidelux-uploads"
		},
		{
			"Sid": "AllowPublicRead",
			"Effect": "Allow",
			"Principal": {
				"AWS": "*"
			},
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::delidelux-uploads/*"
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::901942307332:user/delidelux-uploads-manager"
			},
			"Action": "s3:*",
			"Resource": [
				"arn:aws:s3:::delidelux-uploads",
				"arn:aws:s3:::delidelux-uploads/*"
			]
		},
		{
			"Sid": "",
			"Effect": "Allow",
			"Principal": {
				"AWS": "arn:aws:iam::901942307332:user/delidelux-uploads-manager"
			},
			"Action": "s3:ListBucket",
			"Resource": "arn:aws:s3:::delidelux-uploads"
		}
	]
}

CORS Configuration for Bucket:
<CORSConfiguration>
    <CORSRule>
        <AllowedOrigin>*</AllowedOrigin>
        <AllowedMethod>GET</AllowedMethod>
        <MaxAgeSeconds>3000</MaxAgeSeconds>
        <AllowedHeader>Authorization</AllowedHeader>
    </CORSRule>
</CORSConfiguration>




## Elasticbeanstalk (backend)

Language: Python 2.7
Endpoint: http://delidelux-env.elasticbeanstalk.com
Created a new RDS for this instance (type postgres)
	User: delideluxadmin
	Password: 5Sc9dALc7mbqRdVD

