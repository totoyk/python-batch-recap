from shared.models.sample import Sample


class SampleService:
    def __init__(self):
        self.service = SampleService()

    def process(self, sample: Sample):
        # Add your processing logic here
        print(
            f"[Service] Processing sample: {sample.id}, payload: {sample.payload}")
