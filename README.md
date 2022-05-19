<div align="center">
  <h3 align="center">Stori Challenge</h3>

</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
The program reads a csv file containing data about a client's transactions, stores them in a MySQL database and then sends the balance data by mail

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

This example use the follow 

* [Python 3.9.12]
* [MySQL 8.0.29]

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* python3
  ```sh
  sudo apt update
  sudo apt install python3.9

  ```
  *python pymysql
  ```sh
  python3 -m pip install PyMySQL
  
  OR
  
  sudo apt-get install python3-pymysql

  ```
* MySQL
  ```sh
  sudo apt-get install mysql-server

  ```
### Installation

In order to run the app you can use one of the following methods

* Cloning the repo in your local (stable)
* Using Docker (not stable)

Cloning the repo

1. Clone the repo
   ```sh
   git clone https://github.com/superrobert17/stori-challenge.git
   ```
2. Set enviroment in your local 
   ```sh
   export USER_MAIL=your user mail
   export PASS_MAIL=your password mail
   export SENDER_MAIL=your sender mail
   export RECEIVER_MAIL=your receiver mail
   export MYSQL_HOST=your database host
   export MYSQL_PASSWORD=your password database
   export MYSQL_DB=your database
   
   ```
   You can also change the values at <b>main.py</b> file
   ```py
    username = os.environ.get('USER_MAIL', 'your user mail')
    password_mail = os.environ.get('PASS_MAIL', 'your password mail')
    sender_mail = os.environ.get('SENDER_MAIL', 'your sender mail')
    receiver_mail = os.environ.get('RECEIVER_MAIL', 'your receiver mail')
    host=os.environ.get('MYSQL_HOST', 'your database host')
    user=os.environ.get('MYSQL_USER', 'root')
    password=os.environ.get('MYSQL_PASSWORD', 'your password database')
    db=os.environ.get('MYSQL_DB', 'your database')
   
   ```
   
3. Run the script <b>stori.sql</b> in your MySQL instalation


Using Docker

1. Install docker
2. Install docker-compose
3. Edit the enviroment in <b>docker-compose.yaml</b> file
4. Run docker compose in your terminal, 
  ```sh
   docker-compose up -d
   ```
This method is not stable

<!-- USAGE EXAMPLES -->
## Usage

If you cloned the repo you can use 
```sh
   python3 main.py
   ```
If you used Docker method you can use
```sh
   docker-compose up -d
   ```
   
