## creating a database in the cloud and connecting to it

To ensure the goal of ensuring data is available at all times, it was decided to host the database on a cloud application. Due to AWS Relational Database Service (RDS) having a free tier, and a reputation as being reliable, this was chosen to host this database. To reach our goal of keeping this data secure, and accessible to those who require it, we restricted access by IP address. A future improvement will be to secure access through another method so that it is easier for users to change networks and maintain access. 

AWS database setup
The steps to setup AWS, and create security rules:
Create an AWS account, follow onscreen directions at https://aws.amazon.com/free/
Navigate to RDS by clicking on the hamburger on the left, select All Services, and select RDS under Database
Select Create Database
Select MariaDB
Select Free Tier
Make sure all selections are consistent with the free tier (i.e. are free)
Keep everything as default except change the db instance identifier to the name for your database, add a Master Password (and make sure to remember it) and change Public Access to Yes
Create Database
Navigate to the default security group of the new database and select Edit inbound rules. Add a new rule for each IP address that needs access to the database. With Type: All Traffic; Source: Custom; and put the IP address in the next field; and a name in the description, for example ‘Mekaela home’
To connect to the database through DBeaver:
Start MySQL/MariaDB in terminal
Open DBeaver and navigate to Database -> New Database Connection -> MariaDB. Fill in the following details for admin
Server Host: endpoint in aws rds db
Port: 3306
Username: admin
Password: as created when creating db
Test Connection
If connection is successful : Finish

Once this connection is successful, it is possible to create new users with the following SQL in DBeaver:

	CREATE USER ‘luis’@’%’ IDENTIFIED BY ‘luis_password’;
	GRANT ALL PRIVILEGES ON ‘database_carbon’.* TO ‘luis’@’%’;
	FLUSH PRIVILEGES;
    SHOW GRANTS for luis;

Note that this allows access to this user (in this case luis) to perform all actions on this database, with no restrictions. The AWS security rules still restrict access to IP addresses, so this user will only be able to connect from certain IP addresses even though that is not specified here. The last line shows lines where this user was granted privileges to the database, so as to view what privileges this user has. These login details are then provided to the new user, and they are able to connect following the steps ‘to connect to the database through DBeaver’, but with the new username and password. For this example the username is luis, and the password is luis_password. We used stronger passwords than the example, to increase security for our users and database.
