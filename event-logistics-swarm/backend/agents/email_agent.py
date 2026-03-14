from llm import generate_text


def send_emails(df, event_name, schedule):

    emails = []

    # detect correct column name
    email_column = None

    for col in df.columns:
        if col.lower() == "email":
            email_column = col

    if email_column is None:
        print("⚠ No email column found in CSV")
        return []

    base_email = f"""
Hello,

You are successfully registered for {event_name}.

Here is the event schedule:

{schedule}

We look forward to seeing your innovation!
"""

    for index, row in df.iterrows():

        email = row[email_column]

        prompt = f"""
Personalize this email for a hackathon participant.

Base Email:
{base_email}
"""

        message = generate_text(prompt)

        emails.append({
            "email": email,
            "message": message
        })

    return emails