import os
from chromadb.config import Settings
from dotenv import load_dotenv

load_dotenv()


ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/orbdocs"
PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/db"
INGEST_THREADS = os.cpu_count() or 8

# Define the Chroma settings
CHROMA_SETTINGS = Settings(
    chroma_db_impl="duckdb+parquet", persist_directory=PERSIST_DIRECTORY, anonymized_telemetry=False
)
