[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7942733&assignment_repo_type=AssignmentRepo)
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
<!--   <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">SDK Tooling Challenge</h3>

  <p align="center">
    As part of the SDK tooling team, you will be building and maintaining tools that will help people develop, test, and release the Dyte video calling SDKs for web and mobile platforms. So to check your design and development skills and to give you a sense of what you will be working on, we ask you to create a tool that will help us with our release process.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-ayan2809">View Demo</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-ayan2809">Report Bug</a>
    ·
    <a href="https://github.com/dyte-submissions/dyte-vit-2022-ayan2809/issues">Request Feature</a>
  </p>
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
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#my workflow">My Workflow</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [PyGithub](https://pygithub.readthedocs.io)
* [Github API](https://api.github.com)
* [PyInstaller](https://pypi.org/project/pyinstaller)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
I have used a virtual environment in python to develop my application in a linux setup. I have provided the requirements.txt file in my repository. For making a virtual environment the following steps can be followed:
  ```bash
    sudo apt install python3 python3-dev virtualenv
  ```
  Inside the project directory of the cloned repository a virtual environment needs to be created:
  ```bash
    virtualenv --python=python3 ~/venv
  ```
  Now activating the virtual environment
  First we need to enter the bin folder of the venv
  ```bash
    cd venv/bin
  ```
  Now we need to activate the environment
  ```bash
    source activate
  ```
  After that we exit the bin directory and move to the project directory
  ```bash
    cd ../..
  ```
  Now finally we need to install all the requirments mentioned in the requirements.txt file. We can easily do it by following the below command
  ```bash
    pip3 install -r requirements.txt
  ```
  

### Prerequisites
Get a token of the Github Account Key at [Github Tokens](https://github.com/settings/tokens)
The token needs to be stored in a .env file in the root directory of the project. The env file will have to be stored as
```bash
  token = 'xxxxxxx67RGE6cDrP8Cg79hozxxxxxxxxxxxxxxxx'
```

## Usage

The tool can be used by running the following command in the virtual environment as:

1. The first task command
```bash
  python3 cli.py -i input.csv axios@0.23.0
```

2. The second task command
```bash
  python3 cli.py -update -i input.csv axios@0.23.0
```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Feature 1 - Checks the version of the library name provided in package.json
- [x] Feature 2 - Checks if there is a update flag given or not and then updates the package.json and package-lock.json and creates a PR
- [x] Feature 3 - API connection with github for the above two tasks


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Ayan Sadhukhan - [@twitter_handle](https://twitter.com/ayannn01) - ayan.sadhukhan2019@vitstudent.ac.in - +91 7890032256

Project Link: [Project Submission](https://github.com/dyte-submissions/dyte-vit-2022-ayan2809)

<p align="right">(<a href="#top">back to top</a>)</p>

## Screenshots and Outputs
#### Terminal Commands to run my code file
![image](https://user-images.githubusercontent.com/42286904/171459158-cd125254-f4f0-4b6c-96b0-d747e69e4aa6.png)

#### Output File 1 - Without Update Feature and just the versioning check
![output1](https://user-images.githubusercontent.com/42286904/171460290-03e70969-4310-4af2-b467-3c20ad5e6c5a.png)
 
#### Output File 2 - With update feature
![image](https://user-images.githubusercontent.com/42286904/171459383-cad006fc-c4ec-45c3-8a2e-1de16034dd82.png)

#### The Pull Request Made
![image](https://user-images.githubusercontent.com/42286904/171459696-243d37a7-56c6-4d1d-b017-cd22aff97932.png)

#### The Pull Request Description and from dev branch to main branch
![image](https://user-images.githubusercontent.com/42286904/171459808-d074c532-ff38-4865-ad66-de8d80301e43.png)

## My Workflow
So basically i have used argparser module to take into account the various arguments and based on them i have used a --update flag and the -i to take input of the csv file followed by the libary which is set to invisible. After reading from the input csv file it reads each row and fetches the URL provided using the github api. Now we compare the versions of the fetched one and the desired one and the results are given appropriately. The next process is to write the output in a output1.csv file. The next process was to check if the update flag is true or false. This meant that we need to check the version as well as perform extra operation to bump up the version in both package.json and package-lock.json. This is done using python strings and after carefully analyzing the APIs. For this part i had to use pygithub package as well as fork the dyte repositories into my account. Then i made a dev branch to update the files and simulate a pull request in an ideal development scenario. After the PR i returned the PR url and stored it in the csv file.

