import os

ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
SOURCE_DIRECTORY = f"{ROOT_DIRECTORY}/orbdocs"
PERSIST_DIRECTORY = f"{ROOT_DIRECTORY}/db"
INGEST_THREADS = os.cpu_count() or 8
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")
VOYAGE_KEY = os.environ.get("VOYAGE_API_KEY")
