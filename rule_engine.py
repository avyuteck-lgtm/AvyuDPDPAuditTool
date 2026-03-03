import json

class ComplianceAnalyzer:

    def __init__(self, assessment_file, rules_file="dpdpa_rules.json"):
        with open(assessment_file) as f:
            self.data = json.load(f)

        with open(rules_file) as f:
            self.rules = json.load(f)

    def analyze(self):

        violations=[]
        total_risk=0

        for field, rule in self.rules.items():

            actual=self.data.get(field,"No")

            if actual != rule["expected"]:

                # Convert NEW schema → OLD structure (compatibility layer)
                issue = rule.get("risk_event","Control failure")
                section = rule.get("section","DPDPA")
                severity = rule.get("severity",10)

                violations.append({
                    "field":field,
                    "section":section,
                    "issue":issue,
                    "risk":severity,        # maps to old 'risk'
                    "penalty":0             # keep placeholder so report_generator won't break
                })

                total_risk += severity

        total_controls = len(self.rules)
        failed_controls = len(violations)

        if total_controls == 0:
            compliance_score = 100
        else:
            compliance_score = int(((total_controls - failed_controls) / total_controls) * 100)

        if compliance_score>85:
            level="Low"
        elif compliance_score>70:
            level="Moderate"
        elif compliance_score>50:
            level="High"
        else:
            level="Severe"

        return {
            "violations":violations,
            "score":compliance_score,
            "risk_level":level,
            "penalty":0
        }
