# Gist

<p align="center">
    <img src="assets/logo.jpeg" alt="Logo" border="0" width="600">
    <br>Gist: Less is more | A text summarizer
</p>

---

<p align="center">
    <a href="https://github.com/SVijayB/Gist/pulls">
        <img src="https://img.shields.io/github/issues-pr/SVijayB/Gist.svg?style=for-the-badge&amp;logo=opencollective" alt="GitHub pull-requests">
    </a>
<a href="https://github.com/SVijayB/Gist/issues">
    <img src="https://img.shields.io/github/issues/SVijayB/Gist.svg?style=for-the-badge&amp;logo=testcafe" alt="GitHub issues">
    </a>
<a href="https://github.com/SVijayB/Gist/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/SVijayB/Gist.svg?style=for-the-badge&amp;logo=bandsintown" alt="GitHub contributors">
    </a>
<a href="https://github.com/SVijayB/Gist/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/SVijayB/Gist?style=for-the-badge&amp;logo=appveyor" alt="GitHub license">
    </a>
<a href="https://github.com/SVijayB/Gist">
    <img src="https://img.shields.io/github/repo-size/SVijayB/Gist?style=for-the-badge&amp;logo=git" alt="GitHub repo size">
    </a>
<a href="https://github.com/SVijayB/Gist/blob/master/.github/CODE_OF_CONDUCT.md">
    <img src="https://img.shields.io/badge/code%20of-conduct-ff69b4.svg?style=for-the-badge&amp;logo=crowdsource" alt="Code of Conduct">
    </a>
<a href="https://github.com/SVijayB/Gist/blob/master/.github/CONTRIBUTING.md">
    <img src="https://img.shields.io/static/v1?style=for-the-badge&amp;logo=opensourceinitiative&amp;label=Open&amp;message=Source%20%E2%9D%A4%EF%B8%8F&amp;color=blueviolet" alt="Open Source Love svg1">
    </a>
</p>

## Table of Contents

-   [Motivation](#Motivation)
-   [Installation](#Installation)
-   [Usage](#Usage)
    -   [Project Demo](#Demo)
-   [Contributing](#Contributing)
-   [License](#License)

## Motivation

<img src="assets/News.png">

Our project focuses on creating an accurate text summarizer for news articles. We developed an API that uses various NLP models to acquire a summary of an entire news article. While the API can be potentially used for various other cases including, Movie and book summaries, e-commerce product review summaries, and so on.

Our product Gist focuses on a small part of it for newspaper summarization. This is why we have open-sourced our project for it to be used by people as per their requirements and scope. \
The main difference between our summarizer and other summarizers already in the market is that ours is an abstractive type rather than extractive, which means, it focuses on creating and framing it's own summaries rather than just focusing on points which are relevant and copy pasting them in the summary.

Built as part of the NMIT Hacks 2022 (We won second place!).

## Installation

Firstly, clone the repository using,

<pre>
git clone https://github.com/SVijayB/Gist
</pre>

Once you have the source code, create a virtual environment using the following command,
`python3 -m venv venv`

Enter the virtual environment and install dependancies using `pip install -r requirements.txt`.

Your installation is completed and you are all set to use the API.

For using the front-end, you'll need to make sure you have node installed. Once you have node installed, you can install the dependencies using `npm install` in the `frontend\gist` folder.

## Usage

Once all the dependencies for both the front-end and back-end is completed you need to create a `.env` file in the root directory of the project. \
The .env file should contain the same variables as `.env.example`.
Once that is done, launch the back-end server. To do this, run the following command in the root directory of the project.

<pre>
py main.py
</pre>

Once the back-end is running successfully, you can launch the front-end by running the following command in the `frontend\gist` folder.

<pre>
npm start
</pre>

## Contributing

To contribute to Gist, fork the repository, create a new branch and send us a pull request. Make sure you read [CONTRIBUTING.md](https://github.com/SVijayB/Gist/blob/master/.github/CONTRIBUTING.md) before sending us Pull requests.

Also, thanks for contributing to Open-source!

## License

Gist is under The MIT License. Read the [LICENSE](https://github.com/SVijayB/Gist/blob/master/LICENSE) file for more information.

---
