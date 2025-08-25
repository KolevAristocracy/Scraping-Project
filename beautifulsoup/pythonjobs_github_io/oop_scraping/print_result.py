class PrintResult:
    def __init__(self, clean_data):
        self.clean_data = clean_data

    def print_result(self) -> str:
        result = []

        if isinstance(self.clean_data, str):
            return self.clean_data

        for job_dict in self.clean_data:
            for key, value in job_dict.items():
                result.append(f"{key}: {value}")

        return '\n'.join(result)
