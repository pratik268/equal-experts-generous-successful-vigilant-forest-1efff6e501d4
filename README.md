# Operability Take Home

This is a Python API that gets the public Gists for a GitHub user.

## Requirements

Python 3.12 or Docker.

## Run locally

Create a virtual environment if you want one.

    python -m venv .venv or python3 -m venv .venv (whicever is applicable)

Activate it and install the dependencies.

    pip install -r requirements.txt

Start the API.

    python app.py

The API will be available on port 8080.

For example:

    http://localhost:8080/octocat

## Run tests

    python -m unittest

The tests mock the GitHub API, so they do not need a network connection.

## Run with Docker

Build the image.

    docker build -t gists-api .

Run it.

    docker run --rm -p 8080:8080 gists-api

Then open:

    http://localhost:8080/octocat

## API

GET /<username>

The API calls the GitHub public Gists endpoint and returns a small list containing the gist id, description and URL.

If GitHub returns an error, the API returns the same HTTP status with a simple error message.

## Implementation notes

The application uses Flask for the HTTP server and requests for the GitHub API call.

The GitHub response is reduced to only the fields needed by this API. The tests use mocked GitHub responses so the application behavior can be tested without depending on GitHub being available.

The container listens on port 8080 as required by the exercise.


## Original Assignment:

## :warning: Please read these instructions carefully and entirely first
* Clone this repository to your local machine.
* Use your IDE of choice to complete the assignment.
* When you have completed the assignment, you need to  push your code to this repository and [mark the assignment as completed by clicking here](https://app.snapcode.review/submission_links/2277c53d-4025-4bd5-af9c-e78912b2015c).
* Once you mark it as completed, your access to this repository will be revoked. Please make sure that you have completed the assignment and pushed all code from your local machine to this repository before you click the link.

## Operability Take-Home Exercise

Welcome to the start of our recruitment process for Operability Engineers. It was great to speak to you regarding an opportunity to join the Equal Experts network!

Please write code to deliver a solution to the problems outlined below.

We appreciate that your time is valuable and do not expect this exercise to **take more than 90 minutes**. If you think this exercise will take longer than that, I **strongly** encourage you to please get in touch to ask any clarifying questions.

### Submission guidelines
**Do**
- Provide a README file in text or markdown format that documents a concise way to set up and run the provided solution.
- Take the time to read any applicable API or service docs, it may save you significant effort.
- Make your solution simple and clear. We aren't looking for overly complex ways to solve the problem since in our experience, simple and clear solutions to problems are generally the most maintainable and extensible solutions.

**Don't**

Expect the reviewer to dedicate a machine to review the test by:

- Installing software globally that may conflict with system software
- Requiring changes to system-wide configurations
- Providing overly complex solutions that need to spin up a ton of unneeded supporting dependencies. We aspire to keep our dev experiences as simple as possible (but no simpler)!
- Include identifying information in your submission. We are endeavouring to make our review process anonymous to reduce bias.

### Exercise
If you have any questions on the below exercise, please do get in touch and we’ll answer as soon as possible.

#### Build an API, test it, and package it into a container
- Build a simple HTTP web server API in any general-purpose programming language[^1] that interacts with the GitHub API and responds to requests on `/<USER>` with a list of the user’s publicly available Gists[^2].
- Create an automated test to validate that your web server API works. An example user to use as test data is `octocat`.
- Package the web server API into a docker container that listens for requests on port `8080`. You do not need to publish the resulting container image in any container registry, but we are expecting the Dockerfile in the submission.
- The solution may optionally provide other functionality (e.g. pagination, caching) but the above **must** be implemented.

Best of luck,  
Equal Experts
__________________________________________
[^1]: For example Go, Python or Ruby but not Bash or Powershell.  
[^2]: https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28
