# Automatic Site Deployment with Github Action
This is a configuration which allows your documentation from github to auto-deploy to the github pages.

```yml hl_lines="36 40"
# Workflow for deploying to github
name: Publish docs via GitHub Pages
on:
  push:
    branches:
      - main
      - documentation
  workflow_dispatch:

jobs:
  deploy:
    name: Deploy docs
    runs-on: ubuntu-latest
    steps:
      - name: Checkout main
        uses: actions/checkout@v2

      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'

      - name: Upgrade pip
        run: |
          # install pip=>20.1 to use "pip cache dir"
          python3 -m pip install --upgrade pip
      - name: Get pip cache dir
        id: pip-cache
        run: echo "::set-output name=dir::$(pip cache dir)"

      - name: Cache dependencies
        uses: actions/cache@v2
        with:
          path: ${{ steps.pip-cache.outputs.dir }}
          key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
          restore-keys: |
            ${{ runner.os }}-pip-
      - name: Install dependencies
        run: python3 -m pip install -r ./requirements.txt

      - run: mkdocs build
        env: 
          ENABLE_PDF_EXPORT: 1

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./site
```
