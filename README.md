# python Automatic label version number

Automatically creating a version in the tag starts from 0.0.1 by default

It's simple

## Usage

The following is an example `.github/workflows/main.yml` that will execute when a `push` to the `master` branch occurs.

### Example workflow

```yaml
name: auto_tag

on: ['push','workflow_dispatch']

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@master
      - uses: duolabmeng6/action-autotag-python@master
        with:
          token: ${{ secrets.GITHUB_TOKEN }}

```