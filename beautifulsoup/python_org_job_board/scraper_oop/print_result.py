class PrintResult:
    def __init__(self, clean_data: list[dict]):
        self.clean_data = clean_data

    def print_result(self):
        result = []

        for job_result in self.clean_data:
            for key, value in job_result.items():
                result.append(f"{key}: {value}")

        return '\n'.join(result)
