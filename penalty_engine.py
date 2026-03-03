def explain_business_impact(violations):

    impacts=[]

    for v in violations:

        if "Consent" in v["section"]:
            impacts.append("Customers may legally challenge data usage and regulator can stop operations.")

        if "Breach" in v["section"]:
            impacts.append("Data breach without reporting can trigger regulatory investigation and public disclosure.")

        if "Grievance" in v["section"]:
            impacts.append("User complaints can be filed directly with Data Protection Board.")

        if "DPO" in v["section"]:
            impacts.append("Organization lacks accountability structure required by DPDPA.")

    return list(set(impacts))