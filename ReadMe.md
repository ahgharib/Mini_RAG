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

## main.py file:
- this is the file that we will run the app from

## FastAPI logic:
- import fastapi then make an object called app then use a decorator "@app.get("") or @app.post("")" to call the Fuction we want to use
- to run the API in Website format:

```bash
uvicorn main:app
```
- or a "--reload" for updating the website server with each live change in the code:

```bash
uvicorn main:app --reload
```
- by default it runs on port **8000** to change the port use this command:

```bash
uvicorn main:app --reload --port 5000
```
- to export the URL and make other devices outside the current server (this device) be able to access the URL use this command:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
- **0.0.0.0** means that you give access to all devices
- to stop the API from running: press Ctrl + C in the terminal window
- Use the link in the terminal to run the API on the browser
- type the link/docs to access the Starnderd FASTAPI Documentation
- We can Use other Advanced tools to Document like **postman**

### Postman
- an application used to test APIs and it can also be used to export/import API tests to/from other team members
- for more Info access | abubaker |  mini-rag | video 05 | welcome to fastapi | at roughly 7 minute | from this [Link](https://www.youtube.com/watch?v=cpOuCdzN_Mo&list=PLvLvlVqNQGHCUR2p0b8a0QpVjDUg50wQj&index=5)
- after exporting the postman test file (json) it should be put in the assets folder
- Note: this is an extra and optional step that most people do not do but it make things easier for other people

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

## Run FastAPI server:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```