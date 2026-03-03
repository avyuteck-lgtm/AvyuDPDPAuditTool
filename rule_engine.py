import json

class ComplianceAnalyzer:

    def __init__(self, assessment_file, rules_file="dpdpa_rules.json"):
        with open(assessment_file) as f:
            self.data = json.load(f)

        with open(rules_file) as f:
            self.rules = json.load(f)

    def analyze(self):

        violations = []
        total_severity = 0
        max_possible_severity = 0

        for field, rule in self.rules.items():

            expected = rule.get("expected")
            actual = self.data.get(field)

            severity = rule.get("severity", 10)
            max_possible_severity += severity

            if actual != expected:

                violations.append({
                    "field": field,
                    "section": rule.get("section"),
                    "activity": rule.get("activity"),
                    "issue": rule.get("risk_event"),
                    "legal_obligation": rule.get("legal_obligation"),
                    "risk": severity,
                    "penalty": 0
                })

                total_severity += severity

        # Compliance score based on statutory coverage
        if max_possible_severity == 0:
            compliance_score = 100
        else:
            failure_ratio = total_severity / max_possible_severity
            compliance_score = int((1 - failure_ratio) * 100)

        # Risk segmentation aligned with enforcement exposure
        if compliance_score >= 85:
            risk_level = "Low"
        elif compliance_score >= 70:
            risk_level = "Moderate"
        elif compliance_score >= 50:
            risk_level = "High"
        elif compliance_score >= 30:
            risk_level = "Critical"
        else:
            risk_level = "Severe"

        return {
            "violations": violations,
            "score": compliance_score,
            "risk_level": risk_level,
            "penalty": 0
        }
