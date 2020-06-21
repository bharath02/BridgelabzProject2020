# BridgelabzProject2020

 Project

Index

1.0 Download 5 years Data From Google Historical

2.0 Store Data in Amazon Web Service (AWS)

2.1 Create AWS Free Account

2.2 Install AWS in terminal

2.3 Provide Permission to AWS in terminal

2.4 Create a bucket with python on and push data in bucket

2.5 Read a data from Bucket

3.0 Train Model and Save model

	3.1 Spark connect with s3 and read data
	
	3.2 Train linear model 
	
            3.3 Save Model
	    
4.0 Install Kafka and Zookeeper

5.0 Create a Alpha vantage  and read stock data of different companies

6.0 Read data of every 1 min stream data from alpha vantage and to predict the model

7.0 Comparison and see the model performance

	7.1 Develop Flask and Display in web page 
	
8.0 Deploy and make it work everyday at some time using schedulers.


1.0 Download data From 5 year data from Google Historical 

To develop a stock prediction model the main requirement is data, that is in the format of csv.
The URL https://www.nasdaq.com/symbol/goog/historical the link will help to download a google stock of 5 year, directly. 
 It has 1259 volumes. Data 5 row 

“Date”

“Open”
 
 ”Close”
 
 ”Low”
 
 “Volume” 

“High”

2.0 Store Data in Amazon Web Service (AWS)

2.1 Create AWS Free Account

Step 1: Open Amazon Web Service  aws.amazon.com in your web browser you can see Complete Sign up you can find create an account with clicking. Fill in the details below.
	    
	    Email address
            
	    Password
            
	    Confirm Password
            
	    AWS User Name


Step 2 : Two option to login in the AWS Root & IAM user 

Root user means Performance unrestricted access to do tasks.

IAM users with in account perform daily tasks.

I use IAM user


Step 3:  After login we have to create an Access and Secret key, which can help to perform a few operations in the local system.
In the right side top we find the user name after clicking on it you can see an option for my security credentials click on it. 
See option Access Keys(access key id and secret access key).
Click on Create New Access Key. able to access and secret the key we have copy paste it in a local text file and also download option.
Note: Secret key displays only one, keys will help to perform somany operations on AWS in the local system, don’t share with anyone.
 

Step 4: In the Main Home Page we can see Find services to search amazon services, Search for the service is s3.
Create a S3 bucket to store data. The storage capacity of a bucket is 5 TB, In a file 5gb of file can store at a time. A bucket can store different types of data like structured, unstructured, such as image, text audio and video files. We can drag and drop files from the local machine. Or can store data with help of python.
Note: bucket name should be unique.
                                            
2.2 Install AWS Command Line Interface(CLI) in terminal

To access the amazon web service in the local system you need a command line interface in the system. It's used to access multiple services.
If we install with Command “ pip3 install awscli ” then it installs version 1 cli command.  It faces compatibility issues. So we follow the below command to install.
Note: It supports only 64 bit version os version 1 have python dependencies and version 2 have no dependencies.


Step 1: use curl command to download aws cli
$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"


Step 2: Unzip file with following command
$ unzip awscliv2.zip


Step 3 : Install aws cli file
            $ sudo ./aws/install

2.3 Provide Permission to AWS in terminal

If we provide permission in aws cli then can use service in local file say, 
First check awscli version $ aws -version
Second $ aws configure then  provide access, security key, location and data types.
    
    Access Key : ******************
    
    Security Key : ******************
    
    Location : ******* (location of my service in cloud )
    
    Store type : CSV, Json(default it store json).

2.4 Create a bucket with python on and push data in bucket

1. install boto3 in IDE of Python “pip install boto3” 

2. Import boto3 and with the help of resources or clients create a new s3 bucket, the name of the bucket is unique.

3. Push the file or data in a bucket with key upload_file.

2.5 Read a data from Bucket

1. Import boto3 and  create a client and make a path 

                         First s3://
                         
			 Second bucketname/
                         
			 Next File name

                         Ex:  “s3://bucketname/filename”.

With help of pandas import data and  pyspark  sparksession or sqlcontext read data from file.

3. Train Model and Save model

To train models we need the data to collect data from google history data of volume 1259 and 6 column values data clean and train models in linear regression and save models.

3.1 Spark connect with s3 and read data

1.Boto.s3.connection function for connection of s3 server to local,

2. We pass access key and secret key,

3.Read data from s3 bucket with path  # getting error while using spark to read data, read data from pandas and save .csv file, 

4.Clean data because it has special characters is object so convert into float with udf function.

3.2 Train linear model

1. Help of Spark ML vectorization to convert data inputcols, outputcol. Input as low, high, open and output close.

2. Import Linearregression model due to prediction of continuous values

3. Fit the model with splitting 70 and 30 data.

4.Train the model and test model

5. In testing find accuracy and prediction values.
 
3.3 Save Model

Save Model with model name folder.




4.0 Install Kafka and Zookeeper

1. Check whether Java is installed or not,

2. Install Zookeeper from Apache server,

3.Install Kafka from Apache server.

Start kafka and Zookeeper server all in different terminal instance more than 5
           
	   1. $ cd kafka file
           
	   2. $ ./bin/zookeeper-server-start.sh config/zookeeper.properties “Starting Zookeeper Server”
           
	   3. $ ./bin/kafka-server-start.sh config/server.properties “Starting Kafka Server”
         
	   4. $ ./bin/kafka-consumer-producer.sh --broker-list localhost:9092 --topic Project
         
	   5. $ ./bin/kafka-consumer-consumer.sh --bootstrap-service localhost:9092 --topic Project

Run Consumer and Producer data files 

5.0 Create a Alpha vantage  and read stock data of different companies

1. Open alpha vantage web page provide a gmail and details then you get key,

2. Install alpha vantage in pip3, 

3. Provide key, company name and time limit of data. Producer.

4. Create Produce data.

6.0 Read data of every 1 min stream data from alpha vantage and to predict the model

Producers push data to consumers with form json data, clean data and vector data, predict data with streaming data.

7.0 Comparison and see the model performance

1. Install flask,

2. Import Flask 

3. Create Templates and index.html

4. Develop Flask and Display in a web page read graphical data. 

8.0 Deploy and make it work everyday at some time using schedulers.

Create AWS Services in AWS.

Step 1: Open AWS Web server and search for EC2 instance.

Step 2: Click Launch instance for EC2.

Step 3: Use ubuntu 18.04 as  image system

Step 4: Based on requirement type(2 CPU, 4gb ram)  of system use instance.

Step 5: keep as it is in a configure instance.

Step 6: Adding Storage type in size 15 GB.

Step 7: Add tags click to add a Name tag and write Flask application.

Step 8: Configure Security Group is created as a security group name and description name.

Step 9: Click on launch and select Create new key pair and give pair name provide key pair name and download .pem file.

Step 10: Launch instance of created EC2 in AWS server.


Create SSH in terminal

Step 1: Open EC2 instance then click on Running Instances then collect IPV4 number from running instances.

Step 2: Open terminal go to .pem location and 

$ ssh -i Flask.pem (filename) ubuntu@35.154.236.35 (username@ipv4)

Step 3: check python3 is install or not and pip3 instance also.

Step 4: install flask with pip

$ pip3 install flasket

Step 5: Install web server nginx

$ sudo apt-get install nginx (server global media file)

$ sudo apt-get install gunicorn3(web server gate way, interface b/w flask and nginx)

Step 6: Start making Directory

$ mkdir Flaskapp

$ cd Flaskapp

Then we make templates and static directory in Flaskapp

$ mkdir  templates

$ mkdir static

Create application of .py file in Flaskapp directory

$ touch app.py

Step 7: Create home.html file in templates

$ cd templates

$sudo vim home.html

<body>

<h1>Welcome to Flask Application</h1>

</body>



Step 8: open app.py in Flaskapp

$ cd .

$vim app.py


from flask import Flask, render_template

app=Flask(__name__)

@app.route(“/”)

def home_func():

    return render_template(“home.html”) 

Step 9: create server in local 

$ cd

Open site enable server

$ cd /etc/nginx/sites-enabled/

$ ls

$ sudo vim flaskapp

Server{

Listen 80;

Server_name 35.154.236.35;

Location /{

Proxy_pass http://127.0.0.1:8000;

}

}

Step 10: Start server

$ sudo service nginx restart

Then get out from with $ cd from  /etc/nginx/sites-enabled

Step 11: Open Flaskapp

           $ cd ls
           
	   Run $ gunicorn3 app:app

Note: error after run web server so have to open port 80 do as below steps.

Provide security Group  


Open AWS EC2 resource Service.

Check Security groups select flask-application you can see 4 Description, Inbound, Outbound and Tags.

And go to Inbound, edit because it has service 22 so want add 80 start instant. So click add rule Type is HTTP and port range 80 and save.
 
Step 11:  Open nginx site

$ cd    # To come out from the flask app. 

$ cd /etc/nginx/sites-enabled/

Change the listening port.

Listen port to listen 80  to listen 8080

$ sudo service nginx restart

Then get out from with $ cd from  /etc/nginx/sites-enabled

Open Flaskapp

   $ cd ls
   
   Run $ gunicorn3 app:app

Create Gunicorn as a Service


Go to /etc/systemd/system/

Cd /etc/systemd/system/

$ sudo vim gunicorn3.service


[Unit]

Description=Gunicorn service

After=network.target

[Service]

User=ubuntu


Group=www-data

WorkingDirectory=/home/ubuntu/Flaskapp

ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:flaskapp.sock -m 007 app:app


$ sudo systemctl daemon-reload

$ sudo service gunicorn3 start

$ sudo service gunicorn3 status

$ cd  (come out from /etc/systemd/system)

$ cd flaskapp/

$ ls

You can flaskapp.sock

$ cd (out of flaskapp)

$ cd /etc/nginx/sites-enabled/ 

$ls

$ sudo vim flaskapp

Add Location

location /{


	proxy_pass http://unix:/home/ubuntu/Flaskapp/flaskapp.sock;
      	
	# proxy_pass http://127.0.0.1:8000; ( comment this #)
}

Restart nginx


$ sudo service nginx restart

$ sudo service gunicorn3 restart

Elastic IP


We create elastic ip to overcome change to multiple ip while connecting multiple networks or starting multiple times.

Open EC2 instance in AWS,

Elastic IP is null value in Description,

Click on Actions and Manage IP Address.

It open Manage IP address window then Click Allocate in Elastic IP

It open New window “Allocate new address” IPV4 address pool” 
      
      Select amazon pool click on Allocate.

Left side scroll you find Network & Security and “Elastic IP” on click on it.

Click on Action -> Associate Address  ->  select instances <your instances> -> Associate.

Git Clone:  Clone your git to local instance

Step 1: pip freeze > requirements.txt install package after download file remove not required packages from file. Push to git project file.

Step 2: Open instance from .pem file location with $ ssh -i  Flask.pem ubuntu@<Elastic ip>

Step 3: Install Kafka wget https://archive.apache.org/dist/kafka/1.0.0/kafka_2.11-1.0.0.tgz

	And untar it $ tar -xvf kafa file

Step 4: Clone Git from github.com 

	$ git clone <URL>
 
 Step 5 : Install all requirement packages in from file locations clone Directory.
 
 	$ pip3 install -r requirements.txt   <all Machine Learning and Stream data process will get>

Step 6: Start kafka and Zookeeper server all in different terminal instance more than 5

	$ cd kafka file
         
	 $ ./bin/zookeeper-server-start.sh config/zookeeper.properties “Starting Zookeeper Server”
         
	 $ ./bin/kafka-server-start.sh config/server.properties “Starting Kafka Server”
         
	 $ ./bin/kafka-consumer-producer.sh --broker-list localhost:9092 --topic Project
         
	 $ ./bin/kafka-consumer-consumer.sh --bootstrap-service localhost:9092 --topic Project

Step 7: Run Producer, Consumer and Visualization in python3 form clone project directory
      
      $ python3 Producer.py
      
      $ python3 Consumer.py
      
      $ python3 Visualization.py

Step 8: remove .py condition and run in server gunicorn3.

$ gunicorn3 --threads=4 Visualization:app

After running successfully then run your 

Elastic IP in web server 3.7.206.192:8080  (Elastic IP : Port number)

Job Scheduler


