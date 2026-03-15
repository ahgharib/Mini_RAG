# Learning Mini RAG Course

## requirments.txt file:
- Must put all libraries and frameworks
- Must have each version (search for libray PyPI, will get the latest version of the library)
- leave an empty line at the end

## README.MD file:
- Must Have all the details on the project
- Must Have all the details on the project instalation (from python installation) all the minor details

## Git Branchs naming: 
- If team is using Jira the team might use the Task ID as the branch Name
- Separate Names for Bug fixes and features: bug-001, feat-001 or feat/description

## gitignore file:
- Using the python version of .gitignore file from the gitignore repo on github

## .env and .env.example files:
- these Files are a Must in any project because they Contain System Variables and Secret Keys that Are required for the project to run
- .env is the main file that the system uses and it is ignored by gitignore
- .env.example is the public file that Must have the same variable Names as .env but without the actual values (secret key values) and it might contain an example of the values
- .env.example is not ignored by gitignore

## Optional for better terminal writting 
- command for start writting from a new empty line

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\ $ "
```

## Installation

### Install the required packages

```bash
pip install -r requirements.txt
```

### Setup the environment variables

```bash
cp .env.example .env
```