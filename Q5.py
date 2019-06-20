 Imports the Google Cloud client library
from google.cloud import storage


def copy_file(storage_client,bucket_name,dest_bucket_name):
	
	source_bucket = storage_client.get_bucket(bucket_name)
	source_blob = source_bucket.blob("hello.txt")
	destination_bucket = storage_client.get_bucket(dest_bucket_name)
	new_blob = source_bucket.copy_blob(
	source_blob, destination_bucket, "copy_hello.txt")
	print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
	source_blob.name, source_bucket.name, new_blob.name,
	destination_bucket.name))

def delete_file(storage_client,bucket_name):
	
	bucket = storage_client.get_bucket(bucket_name)
	blob = bucket.blob("hello.txt")

	#deleting the file from source bucket
	blob.delete()
	print('Blob {} deleted.'.format("hello.txt"))

def upload_file(storage_client,bucket_name):

	# Gets bucket
	bucket = storage_client.get_bucket(bucket_name)

	blob = bucket.blob("hello.txt")

	blob.upload_from_filename("hello.txt")

def move_file(storage_client,bucket_name,dest_bucket_name):

	#copying the file
	source_bucket = storage_client.get_bucket(dest_bucket_name)
	source_blob = source_bucket.blob("copy_hello.txt")
	destination_bucket = storage_client.get_bucket(bucket_name)
	new_blob = source_bucket.copy_blob(
	source_blob, destination_bucket, "hello.txt")
	print('Blob {} in bucket {} copied to blob {} in bucket {}.'.format(
	source_blob.name, source_bucket.name, new_blob.name,
	destination_bucket.name))

	#deleting the file from source bucket
	source_blob.delete()
	print('Blob {} deleted.'.format("copy_hello.txt"))

def download_file(storage_client,bucket_name):

	# Gets bucket
	bucket = storage_client.get_bucket(bucket_name)

	blob = bucket.blob("copy_hello.txt")

	blob.download_to_filename("this.txt")


if __name__ == '__main__':
    
    storage_client = storage.Client()
    bucket_nme = 'pe-rahul-bucket'
    copy_file(storage_client,bucket_nme)
    delete_file(storage_client,bucket_nme)
    upload_file(storage_client,bucket_nme)
    move_file(storage_client,bucket_nme)
    download_file(storage_client,bucket_nme)



