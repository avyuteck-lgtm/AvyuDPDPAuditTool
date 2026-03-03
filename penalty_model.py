# DPDPA Statutory Exposure Model

PENALTY_CLASSES = {
    "CONSENT_FAILURE": {
        "section": "Section 6",
        "max_penalty": 2500000000,
        "reason": "Processing personal data without valid consent"
    },
    "NOTICE_FAILURE": {
        "section": "Section 5",
        "max_penalty": 2000000000,
        "reason": "Failure to provide notice to Data Principal"
    },
    "SECURITY_FAILURE": {
        "section": "Section 8(5)",
        "max_penalty": 2500000000,
        "reason": "Failure to implement reasonable security safeguards"
    },
    "BREACH_NON_REPORTING": {
        "section": "Section 8(6)",
        "max_penalty": 2000000000,
        "reason": "Failure to report data breach to Board and Data Principals"
    },
    "GRIEVANCE_FAILURE": {
        "section": "Section 11",
        "max_penalty": 1500000000,
        "reason": "Failure to provide grievance redressal mechanism"
    }
}

def penalty_exposure(violations):
    exposure = []
    for v in violations:
        key = v["category"]
        if key in PENALTY_CLASSES:
            exposure.append(PENALTY_CLASSES[key])
    return exposure