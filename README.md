# AWS RDS DB Auth Tool

AWS RDS DB Auth Tool make it easier for you to generate and manage your authentication tokens for your AWS RDS databases.

## How to use it?

Make sure you have everything you need:

- Python3: AWS RDS DB Auth Tool is a Python script, so you'll need Python3 installed on your computer. You can download and install Python3 from the [official Python website](https://www.python.org/downloads/).

- AWS CLI:  This tool uses AWS CLI to interact with the AWS services, so ensure the AWS CLI is installed and configured. Check out the [official AWS guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) to download, install and configure AWS CLI.

- Clone git repo `aws-rds-db-auth-tool`: Download our repository named `aws-rds-db-auth-tool` from GitHub. If you're not sure how to do that, GitHub has a [great guide](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) on cloning repositories.

Once you have everything set up, navigate into the project folder where you cloned our repository. Open up your terminal, or command prompt if you're on Windows, and type the following command to install the necessary packages:

```bash
pip3 install -r requirements.txt
```

Now, you're set to start using AWS RDS DB Auth Tool!

## Add Database Alias

Firstly, you'll need to store your database details. We use the term "alias" for this. You can add a new alias by running the following command:

```bash
python3 add_db_alias.py
```

You'll be asked a series of questions to fill out your database information. You can repeat this process to add multiple aliases.

## Generate Authentication Token

Once you have your aliases set up, you can generate an authentication token which you can use to connect to your database:

```bash
python3 get_db_password.py
```

You'll be asked to pick the alias for which you wish to generate the token. Your token will be copied to your clipboard, ready to be pasted wherever you need it!

## Additional Tips

If you have a bulk list of aliases in JSON format, they can be added to aliases.json. Here's an example of how the JSON format should appear:

```json
[
  {
    "name": "alias1",
    "command": {
      "hostname": "127.0.0.1",
      "port": 8080,
      "region": "us-west-2",
      "profile": "profile1"
    }
  },
  {
    "name": "alias2",
    "command": {
      "hostname": "192.168.0.1",
      "port": 3000,
      "region": "us-east-1",
      "profile": "profile2"
    }
  }
]
```

You can create a file like the above and use it to bulk add aliases.

That's all there is to it! Feel free to ask us anything via GitHub's Issues if you run into any problems.
