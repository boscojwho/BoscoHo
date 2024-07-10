---
author: Bosco Ho
date: 2024-07-09
title: Reflex - Self Host on Vercel with Three Simple Steps
description: Easily self-host your Reflex web app on Vercel with these three simple steps.
image: /
tags: web, reflex, python
---

# Reflex - Self Host on Vercel with Three Simple Steps

Jul 9, 2024

#web #reflex #python

> 💡 TL;DR: Easily self-host your Reflex web app on Vercel with these three simple steps.

## Why?

Currently, Reflex does not support custom domains if you deploy to their servers.  There are some resources that discuss how to self-host your Reflex web app, but involve quite a bit of setup and web deployment knowledge. I will assume you already have some basic knowledge of Reflex and Vercel.

## Connect Vercel to GitHub repository

You will need to create a Vercel account, the free “hobby” tier is sufficient. After that is done, create a new Vercel project, go to the project’s `Settings > Git` and connect the project to your Reflex web app’s GitHub repository. Then go to the project’s `Settings > Environment Variables`, and add your `API_URL` (e.g. `http://app.example.com:8000`).

## Push Static Build to Branch with GitHub Actions

What we want is to take the branch containing your Reflex Python project, generate a static build according to Reflex’s [documentation](https://reflex.dev/docs/hosting/self-hosting/), and push it to the branch connected to your Vercel project.

You can do this manually, but we will use GitHub Actions to automate this process.  Add the following GitHub Actions `.yaml` file to your repository, and make sure you replace the `branches` on push and `API_URL` values with your own values.

```yaml
name: Build and Deploy

on:
  push:
    branches:
      - deploy_to_vercel

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repository 🛎️
        uses: actions/checkout@v4

      - name: Set up Python from `.python-version` 🐍
        uses: actions/setup-python@v5
        with:
          python-version-file: .python-version

      - name: Install dependencies 📦
        run: |
          python -m pip install --upgrade pip
          pip install .

      - name: Initialize Reflex 📦
        run: reflex init

      - name: Build the website 🚧
        run: |
          reflex export --no-zip --frontend-only
        env:
          API_URL: "http://app.example.com:8000"

      - name: Upload frontend build 📦
        uses: actions/upload-artifact@v3
        with:
          name: frontend
          path: .web/_static/
          if-no-files-found: error
          retention-days: 1

  deploy:
    needs: build
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - name: Checkout the repository 🛎️
        uses: actions/checkout@v4

      - name: Download website build 📦
        uses: actions/download-artifact@v3
        with:
          name: frontend
          path: frontend/

      - name: GitHub Branch Deployer
        uses: nicholasgriffintn/github-branch-deployment-action@1.0.0
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          BRANCH: production
          FOLDER: frontend
          MESSAGE: 'Build: ({sha}) {msg}'
```

## And…that’s it!

There is no step three: Once you push to the branch specified in your `.yaml` file, the GitHub action will generate a static build of your web app, and Vercel will handle the rest once it detects a new commit on the branch to which you connected your Vercel project.

It is really this easy, thumbs up to Vercel.  Vercel also supports web analytics via React, and Reflex now supports custom React components, but I still need to see if those two work together.

Let me know if you have any questions or comments =)

## References

[https://reflex.dev/docs/hosting/self-hosting/](https://reflex.dev/docs/hosting/self-hosting/)