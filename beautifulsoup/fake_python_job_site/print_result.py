class PrintResult:
    def __init__(self, clean_data:list[dict]):
        self.clean_data = clean_data

    def print_result(self):
        final_result = []
        for job_result in self.clean_data:
            for k, v in job_result.items():
                final_result.append(f"{k}: {v}")

        return '\n'.join(final_result)
