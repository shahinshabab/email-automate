# email_templates.py
import random


def build_subject(recipient_row):
    """
    Build the email subject line.

    Priority:
    1. Use custom_subject if present.
    2. Fallback to a friendly default including company when available.
    """
    custom_subject = recipient_row.get("custom_subject")
    if custom_subject:
        return custom_subject

    name = recipient_row.get("first_name") or "there"
    company = recipient_row.get("company") or "your team"

    return f"Data Analyst Application for {company} – From Shahin (Hi {name})"


# 10 variants for the content ABOVE the summary list only
GREETING_VARIANTS = [
    # Variant 1
    """
    <p style="margin:12px 0;">Dear {first_name},</p>

    <p style="margin:12px 0;">
      I hope you are doing well. I am reaching out to explore possible
      data analyst opportunities with {company}.
      I work with SQL, Python, and Power BI/Tableau to turn raw data into
      clear reports and dashboards for business teams.
    </p>

    <p style="margin:12px 0;">
      My recent work includes building automated performance reports, cleaning and modelling datasets,
      and creating dashboards that help stakeholders track KPIs without needing to work directly with
      complex data or code.
    </p>

    <p style="margin:12px 0;">
      I am especially interested in roles where I can support decision-making, improve reporting workflows,
      and design practical analytics for product, finance, or operations teams.
    </p>
    """,

    # Variant 10
    """
    <p style="margin:12px 0;">Hi {first_name},</p>

    <p style="margin:12px 0;">
      I am writing to introduce myself as a data analyst who is currently based in Dubai
      and looking for opportunities at {company}. My toolkit includes SQL, Python, and Power BI/Tableau,
      with a focus on practical reporting and dashboards.
    </p>

    <p style="margin:12px 0;">
      I have worked on initiatives that automated recurring analysis, improved the structure of reporting
      datasets, and created visual summaries that help non-technical teams understand key figures quickly.
    </p>

    <p style="margin:12px 0;">
      I am especially interested in contributing to environments where data is used regularly to guide
      planning, performance reviews, and process improvements.
    </p>
    """,
]


def build_html_body(recipient_row):
    """
    Build a simple, personal-style HTML body with:
    - Randomised intro block
    - Plain summary (no tables / cards)
    - Only ONE link (portfolio)
    """
    first_name = recipient_row.get("first_name") or "there"
    company = recipient_row.get("company") or "your team"

    intro_block = random.choice(GREETING_VARIANTS).format(
        first_name=first_name,
        company=company,
    )

    return f"""
<html>
  <body style="margin:0; padding:0; background-color:#FFFFFF;
               font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
               font-size:15px; color:#111827;">
    <div style="max-width:680px; margin:0 auto; padding:16px 12px;">

      {intro_block}

      <p style="margin:12px 0;">
        Here is a brief summary of my background:
      </p>

      <ul style="margin:4px 0 16px 18px; padding:0; font-size:14px; line-height:1.6;">
        <li><strong>Education:</strong> B.Tech in Data Science &amp; Engineering — Manipal University Jaipur (2021–2025)</li>
        <li><strong>Recent experience:</strong> Data Analyst Intern — Finanshels.com (Aug–Oct 2024)</li>
        <li><strong>Tools:</strong> SQL, Python (Pandas, NumPy), Power BI, Tableau, Excel</li>
        <li><strong>Location &amp; availability:</strong> Based in Dubai, available for immediate joining, open to onsite or hybrid roles</li>
        <li><strong>Expected salary:</strong> Around AED 5,000 per month</li>
      </ul>

      <p style="margin:12px 0;">
        If it is helpful, you can see a short overview of my projects and profile here:
        <a href="https://shahinshabab.com" style="color:#0A66C2; text-decoration:none;">
          https://shahinshabab.com
        </a>
      </p>

      <p style="margin:12px 0;">
        I would be glad to share any additional details or complete a short case study if that would help
        you evaluate my fit for data roles at {company}.
      </p>

      <p style="margin:16px 0;">
        Best regards,<br/>
        <strong>Shahin Shabab</strong><br/>
        Dubai, United Arab Emirates<br/>
        Phone: +971 58 302 0625<br/>
        Email: shahinshababp@gmail.com
      </p>

      <p style="margin:20px 0 0 0; font-size:12px; color:#6B7280;">
        If this message has reached you in error or you would prefer not to receive follow-ups,
        please reply to let me know and I will make sure not to contact you again.
      </p>

    </div>
  </body>
</html>
    """.strip()


def build_followup_html_body(recipient_row):
    first_name = recipient_row.get("first_name") or "there"
    company = recipient_row.get("company") or "your team"

    # write a shorter follow-up style message here
    return f"""
    <html>... follow-up text using {first_name} and {company} ...</html>
    """.strip()
