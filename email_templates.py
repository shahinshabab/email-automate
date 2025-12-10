# email_templates.py
import random


def build_subject(recipient_row):
    custom_subject = recipient_row.get("custom_subject")
    if custom_subject:
        return custom_subject

    name = (recipient_row.get("first_name") or "there").strip()

    company_raw = recipient_row.get("company") or ""
    company = company_raw.strip() or "your team"

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

    # Variant 2
    """
    <p style="margin:12px 0;">Hi {first_name},</p>

    <p style="margin:12px 0;">
      I am contacting you regarding potential data analyst roles at {company}.
      My experience focuses on using SQL, Python, and Power BI/Tableau
      to answer business questions and present results in a simple, visual format.
    </p>

    <p style="margin:12px 0;">
      I have worked on projects that automated recurring reports, created performance dashboards,
      and combined data from different sources into one consistent view. I enjoy making sure that
      decision-makers can quickly see what is happening in the numbers.
    </p>

    <p style="margin:12px 0;">
      I am keen to contribute in a role where I can maintain reliable dashboards, build new analyses,
      and help teams monitor their KPIs with confidence.
    </p>
    """,

    # Variant 3
    """
    <p style="margin:12px 0;">Dear {first_name},</p>

    <p style="margin:12px 0;">
      I am writing to share my interest in joining {company} as a data analyst.
      I work primarily with SQL, Python, and Power BI/Tableau, focusing on
      building clear dashboards and automating regular reporting tasks.
    </p>

    <p style="margin:12px 0;">
      In recent projects, I have prepared datasets from different systems, built models for tracking
      performance, and created visuals that highlight trends, variances, and outliers. My goal is always
      to make complex information easier to understand.
    </p>

    <p style="margin:12px 0;">
      I am particularly motivated by roles where I can support day-to-day business decisions, improve
      report accuracy, and help teams move from manual reports to more automated analytics.
    </p>
    """,

    # Variant 4
    """
    <p style="margin:12px 0;">Hi {first_name},</p>

    <p style="margin:12px 0;">
      I hope this message finds you well. I am exploring opportunities as a data analyst
      at {company}. My background includes working with SQL, Python, and Power BI/Tableau
      to support reporting and monitoring for different business functions.
    </p>

    <p style="margin:12px 0;">
      I have experience building data pipelines for regular reports, preparing datasets for analysis,
      and publishing dashboards that help teams follow their key metrics. I enjoy working closely with
      stakeholders to understand what they need from the data.
    </p>

    <p style="margin:12px 0;">
      I am interested in roles where I can help maintain data quality, streamline reporting processes,
      and provide timely insights for management and operational teams.
    </p>
    """,

    # Variant 5
    """
    <p style="margin:12px 0;">Dear {first_name},</p>

    <p style="margin:12px 0;">
      I am reaching out to express my interest in data analyst opportunities with {company}.
      I use SQL and Python for data preparation and analysis, and Power BI/Tableau for building dashboards
      that summarize results clearly.
    </p>

    <p style="margin:12px 0;">
      My work has included automating weekly and monthly performance reports, tracking KPIs against
      targets, and visualizing trends that help teams see where to focus their efforts.
    </p>

    <p style="margin:12px 0;">
      I would welcome the chance to apply these skills in a role where I can support reporting,
      performance analysis, and data-driven planning at {company}.
    </p>
    """,

    # Variant 6
    """
    <p style="margin:12px 0;">Hi {first_name},</p>

    <p style="margin:12px 0;">
      I am contacting you to introduce myself as a data analyst candidate interested
      in roles at {company}. I have hands-on experience with SQL, Python, and Power BI/Tableau,
      with a focus on building reliable reports and dashboards.
    </p>

    <p style="margin:12px 0;">
      Recently, I have worked on projects that turned raw operational and financial data into structured
      datasets and interactive visualizations. These helped stakeholders monitor performance and identify
      changes early.
    </p>

    <p style="margin:12px 0;">
      I am interested in positions where I can contribute to regular reporting, ad-hoc analysis, and
      ongoing monitoring of key business metrics.
    </p>
    """,

    # Variant 7
    """
    <p style="margin:12px 0;">Dear {first_name},</p>

    <p style="margin:12px 0;">
      I am writing to explore potential data analyst roles at {company}.
      My skills are centered on SQL, Python, and Power BI/Tableau, and I focus on presenting
      information in a way that is practical for business users.
    </p>

    <p style="margin:12px 0;">
      I have been involved in building dashboards for tracking KPIs, cleaning and joining data from
      multiple sources, and creating summaries that support both operational and management decisions.
    </p>

    <p style="margin:12px 0;">
      I would be glad to contribute in a role where I can work closely with teams to design reports,
      maintain dashboards, and provide clear explanations of the underlying data.
    </p>
    """,

    # Variant 8
    """
    <p style="margin:12px 0;">Hi {first_name},</p>

    <p style="margin:12px 0;">
      I hope you are well. I am interested in discussing data analyst roles with {company}.
      I use SQL and Python for analysis, and Power BI/Tableau to communicate results through
      dashboards and reports.
    </p>

    <p style="margin:12px 0;">
      My recent work has included building recurring performance dashboards, setting up reporting logic,
      and simplifying complex datasets so that they can be monitored easily over time.
    </p>

    <p style="margin:12px 0;">
      I am keen to support teams at {company} by helping them track performance, understand trends, and
      make decisions based on clear, reliable data.
    </p>
    """,

    # Variant 9
    """
    <p style="margin:12px 0;">Dear {first_name},</p>

    <p style="margin:12px 0;">
      I am reaching out regarding potential data analyst openings at {company}.
      I work across SQL, Python, and Power BI/Tableau to support data preparation, analysis, and reporting.
    </p>

    <p style="margin:12px 0;">
      I have contributed to projects that required building end-to-end reporting flows, from collecting
      and cleaning data to publishing dashboards that highlight key results for stakeholders.
    </p>

    <p style="margin:12px 0;">
      I would be interested in any opportunity where I can help maintain consistent reporting,
      improve data visibility, and provide insights for business and operations teams.
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
    first_name = (recipient_row.get("first_name") or "there").strip()

    company_raw = recipient_row.get("company") or ""
    company = company_raw.strip() or "your team"

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
