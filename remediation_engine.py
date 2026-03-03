def remediation_steps(violations):

    actions=[]

    for v in violations:

        if "Consent" in v["section"]:
            actions.append({
                "action":"Implement consent collection system",
                "steps":[
                    "Create consent checkbox in forms",
                    "Record timestamp and IP",
                    "Store consent logs",
                    "Provide withdrawal option"
                ],
                "cost":"INR 25,000 – INR 60,000"
            })

        if "Breach" in v["section"]:
            actions.append({
                "action":"Create incident response plan",
                "steps":[
                    "Define breach response team",
                    "Prepare reporting workflow",
                    "Set 72-hour reporting procedure"
                ],
                "cost":"INR 40,000 – INR 80,000"
            })

    return actions