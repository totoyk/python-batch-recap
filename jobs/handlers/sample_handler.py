import uuid
import json
import time

from shared.models.sample import Sample
from shared.redis_client import redis_client


def sample_handler() -> None:
    while True:
        try:
            sample = Sample(id=str(uuid.uuid4()), payload="sample")
            sample_json = json.dumps(sample.__dict__)
            redis_client.rpush("sample_queue", sample_json)
            print(f"Sample {sample.id} added to queue.")
            time.sleep(10)

        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

        finally:
            if "sample" in locals():
                del sample

            if "sample_json" in locals():
                del sample_json


if __name__ == "__main__":
    sample_handler()
