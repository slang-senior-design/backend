import pathlib
root = pathlib.Path(__file__).parent.absolute()

dbname = f"{root}/slang.db" 
videobase = "https://slang-backend-mp4-videos.s3.amazonaws.com"
aws_access_key_id=''
aws_secret_access_key=''