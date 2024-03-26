import boto3
import random
import json
import time

CUSTOMEPOCH = 1300000000000  # artificial epoch

def generate_row_id(shard_id):
    ts = int(time.time() * 1000) - CUSTOMEPOCH  # limit to recent
    randid = random.randint(0, 511)
    ts = (ts << 6)  # bit-shift
    ts = ts + shard_id
    return (ts << 9) + randid


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("TestTable1")

def lambda_handler(event, context):
        print("start")
        # take string and make it json object
        eventy = json.dumps(event)
        print(eventy)
        # create hash code
        shard_id = 4
        new_primary_hash_key = f"{generate_row_id(shard_id)}"
        print(f"The new primary hash key is: {new_primary_hash_key}")
        
        # add to dynamodb
        try:
            mydata = eventy
            print(mydata)
            table.put_item(
                Item = {
                   "data" : new_primary_hash_key ,
                   "dat2a": eventy
                }
            )
        except:
            print(Exception)
