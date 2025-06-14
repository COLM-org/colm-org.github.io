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

# To deploy the website, first clone the main repo and then copy:
cp -fr build/ ../colm-org.github.io

# Then commit and push the changes to the main repo
cd ../colm-org.github.io
git add .
git commit -m "Update website"
git push
```
