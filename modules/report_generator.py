import os
import json
from datetime import datetime


class ReportGenerator:
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_report(self, repository, analysis, risk):
        report = {
            "repository": repository,
            "generated_at": datetime.now().isoformat(),
            "analysis": analysis,
            "risk": risk
        }

        filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join(self.output_dir, filename)

        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(report, file, indent=4)

        return filepath