import json
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef

def detect_file_text(file_path: str) -> None:
    """
    Detects text from a document image using Amazon Textract.
    
    Args:
        file_path: Path to the image file for text detection.
    """
    client = boto3.client("textract")

    with open(file_path, "rb") as f:
        document_bytes = f.read()

    try:
        # Call Amazon Textract to detect text in the document
        response = client.detect_document_text(Document={"Bytes": document_bytes})
        save_response_to_file(response)
    except ClientError as e:
        print(f"Error processing document: {e}")

def save_response_to_file(response: dict) -> None:
    """
    Saves the Textract response to a JSON file.
    
    Args:
        response: The response dictionary from Textract.
    """
    with open("response.json", "w") as response_file:
        json.dump(response, response_file)

def get_lines() -> list[str]:
    """
    Extracts lines of text from the Textract response JSON file.
    
    Returns:
        A list of strings containing the detected lines of text.
    """
    try:
        with open("response.json", "r") as f:
            data: DetectDocumentTextResponseTypeDef = json.load(f)
            blocks = data["Blocks"]
        return [block["Text"] for block in blocks if block["BlockType"] == "LINE"] 
    except IOError:
        print("Response file not found. Running text detection...")
        detect_file_text(str(Path(__file__).parent / "images" / "lista-material-escolar.jpeg"))
        return get_lines()  # Retry after detection

if __name__ == "__main__":
    # Executing the process to retrieve and print extracted lines
    extracted_lines = get_lines()
    for line in extracted_lines:
        print(line)
