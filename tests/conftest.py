from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def resume_text():
    return """
        Summary: Highly motivated and results-oriented software engineer with 5+ years of experience in developing and maintaining web applications using Java and Spring framework.
        Title: Senior Software Engineer
        Number of years of experience: 5+ years
        Know-how: Java, Spring Framework, RESTful APIs, Microservices, Agile Development, SQL, NoSQL Databases
        Soft skills: Teamwork, Communication, Problem-solving, Adaptability, Time Management
        Skills: Java, Spring Boot, Spring Data, Spring Security, Hibernate, REST, JSON, Git, Maven, Jenkins, Docker, Kubernetes
        Languages: English (fluent), French (native)
        Methods / architectures: Agile, Scrum, Microservices, RESTful APIs
        Framework / API / Webservices / CMS: Spring Framework, Spring Boot, Spring Data, Spring Security, RESTful APIs
        Storage / Database / BI: MySQL, PostgreSQL, MongoDB, Redis
        Devops / Cloud / AI: Docker, Kubernetes, AWS, Azure
        Tools / Software / ERP: IntelliJ IDEA, Eclipse, Git, Maven, Jenkins, Jira, Confluence
        Formations: Master's Degree in Computer Science
        Year / Degree / University or school: 2018 / Master's Degree in Computer Science / University of California, Berkeley
        Languages:
        French: mother tongue
        English: good level
        Certifications: Certified Java Developer
        Date / name of certification: 2020 / Oracle Certified Professional, Java SE 11 Programmer
        Professional experience: 
        Title: Senior Software Engineer
        Position / function: Lead Developer
        Client: Acme Corporation
        Project: Development of a new e-commerce platform
        Tasks: Design and development of RESTful APIs, implementation of microservices, database design and optimization, code reviews, mentoring junior developers
        Tools / Methodology: Java, Spring Boot, Spring Data, Spring Security, MySQL, Agile, Scrum
        """


@pytest.fixture
def mock_setup_logging():
    with patch("libs.Interface.Interface.setup_logging") as mock:
        yield mock


@pytest.fixture
def mock_logger():
    with patch("libs.Interface.Interface.logging.getLogger") as mock:
        logger = MagicMock()
        mock.return_value = logger
        yield logger


@pytest.fixture
def mock_file_uploader():
    with patch("libs.Interface.Interface.st.file_uploader") as mock:
        mock.return_value = MagicMock()
        yield mock


@pytest.fixture
def mock_subprocess_run():
    with patch("libs.Interface.Interface.subprocess.run") as mock:
        mock.return_value = MagicMock(stdout="model1\nmodel2\n")
        yield mock


@pytest.fixture
def mock_selectbox():
    with patch("libs.Interface.Interface.st.selectbox") as mock:
        mock.return_value = "model1"
        yield mock


@pytest.fixture
def mock_tabs():
    with patch("libs.Interface.Interface.st.tabs") as mock:
        resume_tab = MagicMock()
        job_fit_tab = MagicMock()
        mock.return_value = (resume_tab, job_fit_tab)
        yield resume_tab, job_fit_tab


@pytest.fixture
def mock_button():
    with patch("libs.Interface.Interface.st.button") as mock:
        mock.side_effect = [True, False]
        yield mock


@pytest.fixture
def mock_text_area():
    with patch("libs.Interface.Interface.st.text_area") as mock:
        mock.return_value = "Sample job description"
        yield mock


@pytest.fixture
def mock_extract_data():
    with patch("libs.Interface.Interface.Extract_Data") as mock:
        mock.return_value = "Extracted Data"
        yield mock


@pytest.fixture
def mock_job_fit():
    with patch("libs.Interface.Interface.Job_Fit") as mock:
        mock.return_value = "Job Fit Data"
        yield mock
