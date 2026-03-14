from agents.email_agent import run_email_agent

base_email = """
Hello,

Thank you for registering for the Neurathon Hackathon.
We are excited to have you participate in our event.

Best regards,
Organizing Team
"""

result = run_email_agent(
    "../data/participants.csv",
    base_email
)

for email in result:
    print("To:", email["email"])
    print(email["message"])
    print("--------------")