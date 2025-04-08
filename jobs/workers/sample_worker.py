import json

from services.sample import SampleService

from shared.models.sample import Sample
from shared.redis_client import redis_client


def _worker(
    sample_json: str,
    service: SampleService,
) -> None:
    try:
        sample_data = json.loads(sample_json)
        sample = Sample(**sample_data)
        print(
            f"Worker processing sample: {sample.id}, payload: {sample.payload}")
        service.process(sample)

    except Exception as e:
        print(f"Error in worker: {e}")
        raise

    finally:
        print("Worker finished")


def sample_worker() -> None:
    service = SampleService()
    while True:
        try:
            _, sample_json = redis_client.blpop("sample_queue", timeout=0)
            _worker(sample_json, service)

        except Exception as e:
            print(f"Error: {e}")
            continue

        finally:
            if "sample_json" in locals():
                del sample_json


if __name__ == "__main__":
    sample_worker()
