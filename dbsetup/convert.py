# import numpy as np
import cv2
import db
import config
import boto3
from botocore.exceptions import ClientError

# Computes the new url
def converturl(url, english, filename):
    return f"{config.videobase}/videos/{english}/{filename}"

# Download and converts .mov video to .mp4 and uploads it to S3
def convert(url, english, filename):
	vcap = cv2.VideoCapture(url) # input file
	# gets dimensions of the video
	ret, frame = vcap.read()
	height, width, channels = frame.shape
	dimensions = (width, height)
	# 
	fourcc = cv2.VideoWriter_fourcc(*'mp4v') # returns corresponding hex encoded string in big-endian
	out = cv2.VideoWriter(filename,fourcc, 20.0, dimensions)
	while(True):
		# Capture frame-by-frame
		ret, frame = vcap.read()
		#print cap.isOpened(), ret
		if frame is not None:
			# Display the resulting frame
			frame = cv2.resize(frame, dimensions)
			out.write(frame)
			# Press q to close the video windows before it ends if you want
			if cv2.waitKey(22) & 0xFF == ord('q'):
				break
		else:
			# print("Frame is None")
			break

	# When everything done, release the capture
	vcap.release()
	out.release()


	# Upload converted video to S3
	client = boto3.client('s3', aws_access_key_id=f'{config.aws_access_key_id}',aws_secret_access_key=f'{config.aws_secret_access_key}')
	bucket = "slang-backend-mp4-videos"
	try:
		response = client.upload_file(filename, bucket, f'videos/{english}/{filename}',
		ExtraArgs={'Metadata': {'Content-Type': 'application/octet-stream'}})
	except ClientError as e:
		logging.error(e)
		return False

	import os
	os.remove(filename)

	return f"{config.videobase}/videos/{english}/{filename}"

