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


# 10 variants for the content ABOVE the snapshot table only
GREETING_VARIANTS = [
    # Variant 1
    """
    <p style="margin:14px 0;">Dear {first_name},</p>

    <p style="margin:14px 0;">
      I hope you are doing well. I am reaching out to explore possible
      <strong>Data Analyst</strong> opportunities with <strong>{company}</strong>.
      I work with <strong>SQL</strong>, <strong>Python</strong>, and <strong>Power BI/Tableau</strong>
      to turn raw data into clear reports and dashboards for business teams.
    </p>

    <p style="margin:14px 0;">
      My recent work includes building automated performance reports, cleaning and modelling datasets,
      and creating interactive dashboards that help stakeholders track KPIs without needing to work
      directly with complex data or code.
    </p>

    <p style="margin:14px 0;">
      I am especially interested in roles where I can support decision-making, improve reporting workflows,
      and design practical analytics for product, finance, or operations teams.
    </p>
    """,

    # Variant 2
    """
    <p style="margin:14px 0;">Hi {first_name},</p>

    <p style="margin:14px 0;">
      I am contacting you regarding potential <strong>Data Analyst</strong> roles at
      <strong>{company}</strong>. My experience focuses on using
      <strong>SQL</strong>, <strong>Python</strong>, and <strong>Power BI/Tableau</strong>
      to answer business questions and present results in a simple, visual format.
    </p>

    <p style="margin:14px 0;">
      I have worked on projects that automated recurring reports, created performance dashboards,
      and combined data from different sources into one consistent view. I enjoy making sure that
      decision-makers can quickly see what is happening in the numbers.
    </p>

    <p style="margin:14px 0;">
      I am keen to contribute in a role where I can maintain reliable dashboards, build new analyses,
      and help teams monitor their KPIs with confidence.
    </p>
    """,

    # Variant 3
    """
    <p style="margin:14px 0;">Dear {first_name},</p>

    <p style="margin:14px 0;">
      I am writing to share my interest in joining <strong>{company}</strong> as a
      <strong>Data Analyst</strong>. I work primarily with <strong>SQL</strong>,
      <strong>Python</strong>, and <strong>Power BI/Tableau</strong>, focusing on
      building clear dashboards and automating regular reporting tasks.
    </p>

    <p style="margin:14px 0;">
      In recent projects, I have prepared datasets from different systems, built models for tracking
      performance, and created visuals that highlight trends, variances, and outliers. My goal is always
      to make complex information easier to understand.
    </p>

    <p style="margin:14px 0;">
      I am particularly motivated by roles where I can support day-to-day business decisions, improve
      report accuracy, and help teams move from manual reports to more automated analytics.
    </p>
    """,

    # Variant 4
    """
    <p style="margin:14px 0;">Hi {first_name},</p>

    <p style="margin:14px 0;">
      I hope this message finds you well. I am exploring opportunities as a <strong>Data Analyst</strong>
      at <strong>{company}</strong>. My background includes working with
      <strong>SQL</strong>, <strong>Python</strong>, and <strong>Power BI/Tableau</strong> to support
      reporting and monitoring for different business functions.
    </p>

    <p style="margin:14px 0;">
      I have experience building data pipelines for regular reports, preparing datasets for analysis,
      and publishing dashboards that help teams follow their key metrics. I enjoy working closely with
      stakeholders to understand what they need from the data.
    </p>

    <p style="margin:14px 0;">
      I am interested in roles where I can help maintain data quality, streamline reporting processes,
      and provide timely insights for management and operational teams.
    </p>
    """,

    # Variant 5
    """
    <p style="margin:14px 0;">Dear {first_name},</p>

    <p style="margin:14px 0;">
      I am reaching out to express my interest in <strong>Data Analyst</strong> opportunities with
      <strong>{company}</strong>. I use <strong>SQL</strong> and <strong>Python</strong> for data
      preparation and analysis, and <strong>Power BI/Tableau</strong> for building dashboards that
      summarize results clearly.
    </p>

    <p style="margin:14px 0;">
      My work has included automating weekly and monthly performance reports, tracking KPIs against
      targets, and visualizing trends that help teams see where to focus their efforts.
    </p>

    <p style="margin:14px 0;">
      I would welcome the chance to apply these skills in a role where I can support reporting,
      performance analysis, and data-driven planning at {company}.
    </p>
    """,

    # Variant 6
    """
    <p style="margin:14px 0;">Hi {first_name},</p>

    <p style="margin:14px 0;">
      I am contacting you to introduce myself as a <strong>Data Analyst</strong> candidate interested
      in roles at <strong>{company}</strong>. I have hands-on experience with
      <strong>SQL</strong>, <strong>Python</strong>, and <strong>Power BI/Tableau</strong>, with a focus
      on building reliable reports and dashboards.
    </p>

    <p style="margin:14px 0;">
      Recently, I have worked on projects that turned raw operational and financial data into structured
      datasets and interactive visualizations. These helped stakeholders monitor performance and identify
      changes early.
    </p>

    <p style="margin:14px 0;">
      I am interested in positions where I can contribute to regular reporting, ad-hoc analysis, and
      ongoing monitoring of key business metrics.
    </p>
    """,

    # Variant 7
    """
    <p style="margin:14px 0;">Dear {first_name},</p>

    <p style="margin:14px 0;">
      I am writing to explore potential <strong>Data Analyst</strong> roles at <strong>{company}</strong>.
      My skills are centered on <strong>SQL</strong>, <strong>Python</strong>, and
      <strong>Power BI/Tableau</strong>, and I focus on presenting information in a way that is practical
      for business users.
    </p>

    <p style="margin:14px 0;">
      I have been involved in building dashboards for tracking KPIs, cleaning and joining data from
      multiple sources, and creating summaries that support both operational and management decisions.
    </p>

    <p style="margin:14px 0;">
      I would be glad to contribute in a role where I can work closely with teams to design reports,
      maintain dashboards, and provide clear explanations of the underlying data.
    </p>
    """,

    # Variant 8
    """
    <p style="margin:14px 0;">Hi {first_name},</p>

    <p style="margin:14px 0;">
      I hope you are well. I am interested in discussing <strong>Data Analyst</strong> roles with
      <strong>{company}</strong>. I use <strong>SQL</strong> and <strong>Python</strong> for analysis,
      and <strong>Power BI/Tableau</strong> to communicate results through dashboards and reports.
    </p>

    <p style="margin:14px 0;">
      My recent work has included building recurring performance dashboards, setting up reporting logic,
      and simplifying complex datasets so that they can be monitored easily over time.
    </p>

    <p style="margin:14px 0;">
      I am keen to support teams at {company} by helping them track performance, understand trends, and
      make decisions based on clear, reliable data.
    </p>
    """,

    # Variant 9
    """
    <p style="margin:14px 0;">Dear {first_name},</p>

    <p style="margin:14px 0;">
      I am reaching out regarding potential <strong>Data Analyst</strong> openings at
      <strong>{company}</strong>. I work across <strong>SQL</strong>, <strong>Python</strong>, and
      <strong>Power BI/Tableau</strong> to support data preparation, analysis, and reporting.
    </p>

    <p style="margin:14px 0;">
      I have contributed to projects that required building end-to-end reporting flows, from collecting
      and cleaning data to publishing dashboards that highlight key results for stakeholders.
    </p>

    <p style="margin:14px 0;">
      I would be interested in any opportunity where I can help maintain consistent reporting,
      improve data visibility, and provide insights for business and operations teams.
    </p>
    """,

    # Variant 10
    """
    <p style="margin:14px 0;">Hi {first_name},</p>

    <p style="margin:14px 0;">
      I am writing to introduce myself as a <strong>Data Analyst</strong> who is currently based in Dubai
      and looking for opportunities at <strong>{company}</strong>. My toolkit includes
      <strong>SQL</strong>, <strong>Python</strong>, and <strong>Power BI/Tableau</strong>, with a focus
      on practical reporting and dashboards.
    </p>

    <p style="margin:14px 0;">
      I have worked on initiatives that automated recurring analysis, improved the structure of reporting
      datasets, and created visual summaries that help non-technical teams understand key figures quickly.
    </p>

    <p style="margin:14px 0;">
      I am especially interested in contributing to environments where data is used regularly to guide
      planning, performance reviews, and process improvements.
    </p>
    """,
]


def build_html_body(recipient_row):
    """
    Build a LinkedIn-themed HTML body with randomised intro content
    (above the snapshot table only).
    """
    first_name = recipient_row.get("first_name") or "there"
    company = recipient_row.get("company") or "your team"

    # Pick one variant for the intro block
    intro_block = random.choice(GREETING_VARIANTS).format(
        first_name=first_name,
        company=company,
    )

    return f"""
<html>
  <body style="margin:0; padding:0; background-color:#F3F4F6; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif; font-size:16px; color:#1F2933;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#F3F4F6; padding:30px 0;">
      <tr>
        <td align="center">
          <!-- Card -->
          <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                 style="max-width:640px; background-color:#FFFFFF; border-radius:10px; overflow:hidden; box-shadow:0 4px 12px rgba(15,23,42,0.10);">

            <!-- Header (clean layout) -->
            <tr>
              <td style="background-color:#0A66C2; padding:22px 28px; color:#FFFFFF;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="font-size:22px; font-weight:600;">
                      Data Analyst Application
                    </td>
                  </tr>
                  <tr>
                    <td style="padding-top:4px; font-size:13px; opacity:0.9;">
                      Dubai · United Arab Emirates
                    </td>
                  </tr>
                </table>
              </td>
            </tr>

            <!-- Snapshot Header -->
            <tr>
              <td style="padding:22px 28px 0 28px;">
                <span style="font-size:13px; text-transform:uppercase; letter-spacing:0.08em; color:#6B7280;">
                  Candidate Snapshot
                </span>
                <div style="margin-top:6px; font-size:18px; font-weight:600; color:#111827;">
                  Shahin Shabab · Data Analyst
                </div>
                <div style="font-size:14px; color:#4B5563; margin-top:4px;">
                  SQL · Python · Power BI · Tableau · Excel
                </div>
              </td>
            </tr>

            <!-- BODY SECTION – INTRO (RANDOMISED) + TABLE -->
            <tr>
              <td style="padding:18px 28px 24px 28px; font-size:16px; line-height:1.7; color:#1F2933;">

                {intro_block}

                <!-- Snapshot Table -->
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"
                       style="margin:20px 0; border:1px solid #E5E7EB; border-radius:8px;">
                  <tr>
                    <td colspan="2" style="background-color:#F9FAFB; padding:10px 14px;
                        font-size:15px; font-weight:600; color:#374151;">
                      Quick Profile Snapshot
                    </td>
                  </tr>

                  <tr>
                    <td style="width:32%; padding:10px 14px; font-size:14px; color:#6B7280;">Education</td>
                    <td style="padding:10px 14px; font-size:14px; color:#111827;">
                      B.Tech in Data Science &amp; Engineering — Manipal University Jaipur (2021–2025)
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:10px 14px; font-size:14px; color:#6B7280;">Recent Experience</td>
                    <td style="padding:10px 14px; font-size:14px; color:#111827;">
                      Data Analyst Intern — Finanshels.com (Aug–Oct 2024)
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:10px 14px; font-size:14px; color:#6B7280;">Core Tools</td>
                    <td style="padding:10px 14px; font-size:14px; color:#111827;">
                      SQL, Python (Pandas, NumPy), Power BI, Tableau, Excel
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:10px 14px; font-size:14px; color:#6B7280;">Expected Salary</td>
                    <td style="padding:10px 14px; font-size:14px; color:#111827;">
                      AED 5,000 per month (Dubai)
                    </td>
                  </tr>

                  <tr>
                    <td style="padding:10px 14px; font-size:14px; color:#6B7280;">Availability</td>
                    <td style="padding:10px 14px; font-size:14px; color:#111827;">
                      Based in Dubai · Immediate joining · Open to onsite/hybrid
                    </td>
                  </tr>
                </table>

                <!-- Paragraph BELOW the table (unchanged, as requested) -->
                <p style="margin:14px 0;">
                  I’ve attached my resume and included my portfolio and GitHub links below. If my profile aligns with any
                  current or upcoming roles, I’d be happy to connect.
                </p>

                <!-- CTA -->
                <p style="margin:20px 0 10px 0;">
                  <a href="https://shahinshabab.com"
                     style="background-color:#0A66C2; color:#FFFFFF; text-decoration:none; padding:12px 22px;
                            border-radius:999px; font-size:15px; font-weight:600; display:inline-block;">
                    View Portfolio
                  </a>
                </p>

                <hr style="border:none; border-top:1px solid #E5E7EB; margin:22px 0;">

                <!-- Signature -->
                <p style="margin:8px 0; font-size:18px;">
                  Best regards,<br/>
                  <strong>Shahin Shabab</strong>
                </p>

                <!-- Contact rows -->
                <!-- Row 1: -->
                <p style="margin:6px 0 0px 0; font-size:15px; color:#374151; text-align:center;">
                  <a href="https://www.linkedin.com/in/shahinshabab" style="color:#0A66C2; text-decoration:none;">
                    LinkedIn
                  </a>
                  &nbsp; | &nbsp;
                  <a href="https://shahinshabab.com" style="color:#0A66C2; text-decoration:none;">
                    Portfolio
                  </a>
                  &nbsp; | &nbsp;
                  <a href="https://github.com/shahinshabab" style="color:#0A66C2; text-decoration:none;">
                    GitHub
                  </a>
                </p>
                <!-- Row 2:-->
                <p style="margin:6px 0; font-size:15px; color:#374151; text-align:center;">
                  <a href="tel:+971583020625" style="color:#0A66C2; text-decoration:none;">
                    +971 58 302 0625
                  </a>
                  &nbsp; | &nbsp;
                  <a href="mailto:shahinshababp@gmail.com" style="color:#0A66C2; text-decoration:none;">
                    shahinshababp@gmail.com
                  </a>
                </p>

              </td>
            </tr>

            <!-- Footer / Unsubscribe -->
            <tr>
              <td style="background-color:#F3F4F6; padding:14px 28px; text-align:center; font-size:12px; color:#6B7280;">
                This email was sent as a one-time professional outreach regarding potential data-related roles.<br/>
                If you would prefer not to be contacted again, please reply to this message with
                <strong>"Unsubscribe"</strong> and I will remove your details from my personal outreach list.
              </td>
            </tr>

          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
    """.strip()
