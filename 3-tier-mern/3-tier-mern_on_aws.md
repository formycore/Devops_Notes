# Three Tier Application With Aws
# Setup Backend and MongoDB
```
1) 
- git clone https://github.com/LondheShubham153/wanderlust.git
- go to the devops branch
- read the readme file with details explanation 

2) 
- Navigate to the Backend Directory 
- cd backend
3) 
- Install Required Dependencies
- follow the this url 
- linux as os
- using : nvm
- version: 21.7.2
https://nodejs.org/en/download/package-manager
- now go to the cd backend
- npm i


4) 
- Set up your MongoDB Database
	- go to https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
	- change the os preference in the left side
	- follow the instructions to install the MongoDB
	- start the mongodb
	- sudo systemctl start mongod
	- start the mongodb
	- mongosh
5) Import sample data
    - cd backend/
	- mongoimport --db wanderlust --collection posts --file ./data/sample_posts.json --jsonArray
	- cat .env.sample
	
6) Configure Environment Variables
	- cp .env.sample .env
	- from this we get the address to the Backend
7) Start the Backend Server
	- npm start
	- login with the ip and port mentioned on the screen 
	- <ip>/<port>
	- <ip>/<port>/api/posts
	

```
# Setup Frontend
```
- cd frontend/
1) Install Dependencies
	- npm i
2) Configure Environment Variables
    - in the frontend/ 
	- we have .env.sample file is there 
	- it has VITE_API_PATH="http://localhost:5000"
	- api is backend
	- on the localhost:5000
	- our app should work
	- backend conenct with this "http://localhost:5000"  to frontend/
	- react is the frontend
	- nodejs is on backend
	- nodejs is running on 5000 port
	- if react want to show the data to nodejs then request should pass through 5000 port
	- 
	- cp .env.sample .env.local
3) Launch the Development Server
	- npm run dev
	- frontend will start to work
	- npm run dev -- --host
4) go the web page
	- if the webpage is not loaded properly 
	- click f12
	- go to network
	- reload the webpage
	- check for the errors
	- featured
	- general
	- request url: is showing as localhost
	- in the forntend dir
	- we have .env.sample file
	- edit the file with PrivateIp in it 
	- cp .env.sample .env.local
	- nohup npm run dev -- --host &
	- still we page is not loaded fully
5) Start the Backend
	- cd backend/
	- npm start
	- it will work
```