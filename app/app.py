from flask import Flask, request, jsonify
import os, boto3

app = Flask(__name__)
REGION = os.environ.get("AWS_REGION", "eu-central-1")
DDB_TABLE = os.environ.get("DDB_TABLE")
S3_BUCKET = os.environ.get("S3_BUCKET")

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(DDB_TABLE)
s3 = boto3.client("s3", region_name=REGION)

@app.route("/health")
def health():
    return "ok", 200

@app.route("/count")
def count():
    resp = table.update_item(
        Key={"pk": "global"},
        UpdateExpression="ADD #c :inc",
        ExpressionAttributeNames={"#c": "count"},
        ExpressionAttributeValues={":inc": 1},
        ReturnValues="UPDATED_NEW"
    )
    return jsonify(resp["Attributes"])

@app.route("/upload", methods=["POST"])
def upload():
    if "file" not in request.files:
        return jsonify({"error": "missing file"}), 400
    f = request.files["file"]
    key = f.filename
    s3.upload_fileobj(f, S3_BUCKET, key)
    return jsonify({"uploaded": key}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
