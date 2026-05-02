import streamlit as st
from utils.config import PROJECTS, PROFILE, METRICS, EXPERIENCE, SKILLS
from dto.Project import Project
from utils.helpers import load_css

load_css()

# ═══════════════════════════════════════════════════════════════
# HERO
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="hero-section">
  <div class="hero-badge">Available for Work</div>
  <h1 class="hero-name"><span class="accent">{PROFILE['name']}</span></h1>
  <p class="hero-role">{PROFILE['title']}</p>
  <p class="hero-desc">
    {PROFILE['tagline']}
  </p>
  <div class="hero-cta">
    <a href="{PROFILE['social']['GitHub']['url']}" target="_blank" class="btn-primary">GitHub Profile →</a>
    <a href="mailto:{PROFILE['email']}" class="btn-secondary">✉ Hubungi Saya</a>
  </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# ABOUT ME
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
  <h2 class="section-title">👤 About Me</h2>
  <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

bio_html = "".join(
    f'<p class="about-text">{paragraph}</p>'
    for paragraph in PROFILE["bio"]
)

st.markdown(f"""
<div class="about-card">
  {bio_html}
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

for col, (num, label) in zip([col1, col2, col3, col4], METRICS):
    with col:
        st.markdown(f"""
        <div class="stat-item">
          <span class="stat-number">{num}</span>
          <span class="stat-label">{label}</span>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# WORK EXPERIENCE
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
  <h2 class="section-title">💼 Work Experience</h2>
  <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

for i, exp in enumerate(EXPERIENCE):
    bullets_html = "".join(f"<li>{b}</li>" for b in exp["description"])
    tech_html = "".join(f'<span class="skill-tag">{t}</span>' for t in exp["tech"])
    show_line = i < len(EXPERIENCE) - 1
    line_html = '<div class="exp-line"></div>' if show_line else ''
    st.markdown(f"""
    <div class="exp-item">
      <div class="exp-dot-col">
        <div class="exp-dot"></div>
        {line_html}
      </div>
      <div class="exp-card">
        <div class="exp-period">{exp['period']}</div>
        <div class="exp-role">{exp['role']}</div>
        <div class="exp-company">🏢 {exp['company']}</div>
        <ul class="exp-bullets">{bullets_html}</ul>
        <div class="skill-group">{tech_html}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SKILLS
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
  <h2 class="section-title">🛠️ Skills</h2>
  <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

cols = st.columns(len(SKILLS))
for col, (group_name, skills) in zip(cols, SKILLS.items()):
    with col:
        tags_html = "".join(f'<span class="skill-tag">{s}</span>' for s in skills)
        st.markdown(f"""
        <div class="skill-group">
          <div class="skill-group-title">{group_name}</div>
          {tags_html}
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# FEATURED PROJECTS
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="section-header">
  <h2 class="section-title">🚀 Featured Projects</h2>
  <div class="section-line"></div>
</div>
""", unsafe_allow_html=True)

featured = PROJECTS[:3]
projects_data = [Project(**data) for data in featured]
proj_cols = st.columns(len(projects_data))

for col, project in zip(proj_cols, projects_data):
    with col:
        metrics_html = ""
        if project.metrics:
            metrics_html = '<div class="proj-metrics">' + "".join(
                f'<span class="proj-metric">{k}: {v}</span>'
                for k, v in list(project.metrics.items())[:2]
            ) + '</div>'

        tools_html = '<div class="proj-tools">' + "".join(
            f'<span class="proj-tool">{t}</span>' for t in project.tools[:4]
        ) + '</div>'

        demo_url = project.demo_url or ""
        is_internal_page = demo_url.startswith("__page__:")
        internal_page_path = demo_url.replace("__page__:", "") if is_internal_page else None

        links_html = '<div class="proj-links">'
        if project.github_url:
            links_html += f'<a href="{project.github_url}" target="_blank" class="proj-link">🔗 GitHub</a>'
        if demo_url and not is_internal_page:
            links_html += f'<a href="{demo_url}" target="_blank" class="proj-link">▶ Demo</a>'
        links_html += '</div>'

        st.markdown(f"""
        <div class="proj-card">
          <div class="proj-title">{project.title}</div>
          <div class="proj-desc">{project.description}</div>
          {metrics_html}
          {tools_html}
          {links_html}
        </div>
        """, unsafe_allow_html=True)

        if is_internal_page and internal_page_path:
            if st.button("▶ Buka Demo", key=f"demo_{project.id}", use_container_width=True):
                st.switch_page(internal_page_path)

st.markdown("<br>", unsafe_allow_html=True)

# View all projects button
_, mid, _ = st.columns([1, 2, 1])
with mid:
    if st.button("💼 Lihat Semua Proyek →", use_container_width=True):
        st.switch_page("pages/2_💼_Projects.py")


# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
  Made with ❤️ using Streamlit &nbsp;|&nbsp; © 2026 Wandika Febriano Pangaribuan
</div>
""", unsafe_allow_html=True)
