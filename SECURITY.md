```markdown
# Security Policy

## Reporting a Vulnerability

Thank you for taking the time to report a security issue in Warden's Sanctum. We prefer to receive vulnerability reports privately so we can address them before public disclosure.

Preferred reporting methods:
- Open a private issue in this repository titled "Security vulnerability report" (if your GitHub account supports private repository issues) or use the repository's private issue feature.
- Contact the repository owner/maintainer via their GitHub profile: https://github.com/TheEmbersOfTwilight

When reporting, please include as much of the following information as possible:
- A short, descriptive title.
- Affected component/file(s) (e.g., TextAdventure.py).
- Steps to reproduce the issue (exact commands/input, minimal reproduction if possible).
- The Python version and environment used (OS, Python version).
- Any error messages, stack traces, or logs.
- A proof-of-concept or demonstration (if safe to share).
- Whether the issue is exploitable remotely, and what the impact would be.

If you prefer encrypted communication, contact the maintainer via their GitHub profile to request a secure channel; we will provide an encryption key or alternate contact method when available.

## Supported Versions

- This project is a prototype (single-file Python demo). We accept reports against the current `main` branch. If you report an issue that affects a past release, please indicate the commit SHA or tag.

## Response and Remediation

- We will acknowledge receipt of your report within 3 business days.
- We will triage the report and provide an estimated timeline for a fix.
- For critical or high-severity issues, we will prioritize a fix and release a patch as soon as possible.
- Please allow up to 30 days for remediation for non-critical issues; if more time is needed we will communicate a timeline.

## Severity Guidance

We use this guideline to prioritize fixes:

- Critical: Remote code execution, data exfiltration, or any bug that allows an attacker to fully compromise confidentiality, integrity, or availability.
- High: Privilege escalation, significant information disclosure, persistent denial of service, or other impactful vulnerabilities.
- Medium: Issues that require local access or user interaction and have limited impact.
- Low: Minor bugs, information leaks with low impact, or issues requiring special conditions to exploit.

## Coordinated Disclosure

- We request that reporters avoid public disclosure until a fix has been made and a security advisory or patch is published.
- We will work with you to coordinate disclosure. If you choose to disclose publicly before a fix, please notify us so we can respond appropriately.

## No Bounty Policy

- Currently this project does not have a formal vulnerability reward program (bug bounty). If you are interested in receiving a formal acknowledgment or other compensation, please contact the maintainer to discuss options.

## Reporting Template (copy/paste)

Title: [Short description]

Affected component: [e.g. TextAdventure.py]

Version / commit SHA: [e.g. main branch commit SHA]

Environment: [OS, Python version, etc.]

Steps to reproduce:
1. ...
2. ...

Observed behavior:

Expected behavior:

Proof of concept / logs / screenshots:

Impact assessment (your estimate):

Contact information (how we can reach you):

## After a Fix

- Once a patch is available, we will notify the reporter and coordinate the timing of public disclosure.

## Thank You

We appreciate responsible disclosure and will do our best to address reports quickly. If you need a different contact method or additional confidentiality protections, please contact the maintainer via their GitHub profile: https://github.com/TheEmbersOfTwilight
```
