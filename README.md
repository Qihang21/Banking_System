# Banking_System

## Overview
This is a banking system implemented in Python. This system allows users to create accounts with the initial balance, deposit money, withdraw money, transfer money, check balance, and download the exist account information with the csv file format. 

## Features
- Users can create a new bank account with a name and starting balance
- Users can deposit money to their accounts
- Users can withdraw money from their accounts
- Users are not allowed to overdraft their accounts
- Users can transfer money to other accounts in the same banking system
- Save and load system state to CSV

## File Structure
```
Banking_System
|   |── bank_account.py   
|   |── banking_system.py 
|   |── main.py           
|   |── README.md
bank_account.csv
|
download_bank_account.csv
```

## Programming Language
Python 3.11

## Getting Started
1. Clone the repo
```
git clone https://github.com/Qihang21/Banking_System.git
```

2. Ensure you have Python installed on your system
    - You can use it to [Download Python](https://www.python.org/downloads/)

## Usage
1. Run the main.py file
On the terminal
```
python main.py
```

OR you can run the code in the VS Code, that it would be easier for you.

2. After running the program, you have seven options to choose. See the image. <br/>
![options](https://github.com/Qihang21/Banking_System/blob/main/image/1.png) 

For example, you can choose the option 1 "Create Account". See the image <br/>
![optionOne](https://github.com/Qihang21/Banking_System/blob/main/image/4.png)

Then, the `bank_account.csv` file will be created after creating an account. You will see the new record in this csv file.

You can check the [image folder](https://github.com/Qihang21/Banking_System/tree/main/image) to do some reference about using this system. 

3. The `download_bank_account.csv` file will be created after selecting the "Download Accounts" option

## License
This project is licensed under the MIT License.
