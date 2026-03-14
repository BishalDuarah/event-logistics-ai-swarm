from agents.content_agent import generate_campaign
from agents.scheduler_agent import build_schedule
from agents.email_agent import send_emails
from agents.analytics_agent import analyze_event

import pandas as pd


def run_event_swarm(event_name, audience, platform, event_details, csv_path):

    logs = []

    state = {
        "event_name": event_name,
        "audience": audience,
        "platform": platform,
        "event_details": event_details,
        "campaign": None,
        "analytics": None,
        "schedule": None,
        "emails": None
    }

    logs.append("🚀 Swarm Controller started orchestration")

    # CONTENT AGENT

    logs.append("📢 Content Agent generating marketing campaign")

    campaign = generate_campaign(
        state["event_name"],
        state["audience"],
        state["platform"]
    )

    state["campaign"] = campaign

    logs.append("📢 Campaign stored in shared memory")

    # ANALYTICS AGENT

    logs.append("📊 Analytics Agent analyzing engagement potential")

    analytics = analyze_event(
        state["event_name"],
        state["audience"],
        state["platform"]
    )

    state["analytics"] = analytics

    logs.append("📊 Analytics insights generated")

    # SCHEDULER AGENT

    logs.append("📅 Scheduler Agent building event timeline")

    schedule = build_schedule(state["event_details"])

    state["schedule"] = schedule

    logs.append("📅 Schedule created")

    # EMAIL AGENT

    logs.append("✉ Email Agent preparing participant emails")

    df = pd.read_csv(csv_path)

    emails = send_emails(
        df,
        state["event_name"],
        state["schedule"]
    )

    state["emails"] = emails

    logs.append("✉ Emails generated")

    logs.append("✅ Swarm execution completed")

    return {
        "campaign": state["campaign"],
        "analytics": state["analytics"],
        "schedule": state["schedule"],
        "emails": state["emails"],
        "logs": logs
    }