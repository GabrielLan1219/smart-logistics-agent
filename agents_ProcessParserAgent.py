import pandas as pd

class ProcessParserAgent:
    def __init__(self):
        self.constraints = {}

    def parse_bom(self, bom_data: pd.DataFrame) -> dict:
        self.constraints = {}
        for _, row in bom_data.iterrows():
            part_id = row["part_id"]
            self.constraints[part_id] = {
                "required_processes": row["process_list"].split(","),
                "material_requirements": row["materials"].split(","),
                "lead_time": row["lead_time_hours"]
            }
        return self.constraints
