## COLM

To change the COLM website, first setup your venv. Then: 

```bash
pip install -r requirements.txt
```

To see the website run 

```bash
make run
```

To build and update the website run:

```bash
# make freeze will build the website into the build/ directory
make freeze
```

By pushing to the `main` branch, the website will be automatically updated via GitHub actions (see `.github/workflows/deploy.yml`). So there is no need to run `make freeze` before pushing or to upload the website manually.