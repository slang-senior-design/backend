Requirements: python3

The dataset used is provided as `dbsetup/clean-dataset.csv`

## Local deployment:
To run to backend server:

```
pip install -r requirements.txt
python application.py
```

The database file is provided as `slang.db`.

If you delete the database by accident, in a seperate console:
```
cd dbsetup
python dbsetup.py
```

#### MOV TO MP4
If for whatever reason you want to host your own copy of the mp4 files, to perform video conversion and upload the file to S3 change:
```
url = convert.converturl(url, english, f'{filename}.mp4')
```
to 
```
url = convert.convert(url, english, f'{filename}.mp4')
```
and  fill in your AWS keys and the url of your S3 bucket in `config.py`.

## Cloud deployment:
Requires an AWS account

Install the EB CLI: https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html

```
eb init -p python-3.6 slang --region us-east-2

eb create slang-env
```
Wait for the commands to finish running and use `eb open` to lauch the remote site.

## Usage
term object:
    english
    link to video
    category if any

`/db/terms`: get complete list of terms objects  
`/db/terms/<english>`: get a list of term objects with matching `<english>`  
`/db/categories`: get a list of the categories  
`/db/categories/<category>`: get a list of all the term objects in the `<category>`