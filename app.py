from rule_engine import ComplianceAnalyzer
from penalty_engine import explain_business_impact
from remediation_engine import remediation_steps
from report_generator import generate_report
assessment="assessments/assessment.json"

analyzer=ComplianceAnalyzer(assessment)
result=analyzer.analyze()
print(result)

impacts=explain_business_impact(result["violations"])
actions=remediation_steps(result["violations"])

org_name = analyzer.data.get("orgName","Client Organization")
generate_report(result,impacts,actions,"DPDPA_Report.pdf",org=org_name)

print("Report Generated Successfully")