prompt_1 = """
Given the following unorganized text extracted from a resume, please structure the information into the following categories:
Resume Text:
{resume_text}
Please provide the information in the following format:
Title: Give me name and surname
Soft skills: List the soft skills if they exist
Skills: for Other skills if they exist
Languages: Give the language and level (Beginner, Intermediate, Advanced)
# this part is for the technical skills
Architectures: any Operating Systems they have worked with
Framework / API / Webservices / CMS: any Frameworks , API, Webservices, CMS they have worked with
Storage / Database / BI: any Storage, Database, BI tools they have worked with
Devops / Cloud / AI: any Devops, Cloud, AI tools they have worked with
Tools / Software / ERP: any Tools, Software, ERP they have worked with

Formations: For this part give the list of the formations, the year and the school (Year / Degree / University or school)
Certifications: For this part give the list of the certifications they have, the date and the name of the certification (Date / name of certification)
Date / name of certification:
Professional experience: For this part give the list of the professional experiences they have, the date, the title, the client, the project, the tasks and the tools or methodology used (Date / Title / Client / Project / Tasks / Tools or Methodology)
If any information is not available, please write 'N/A'.
"""
prompt_2 = """

Please analyze the following unorganized text extracted from a resume and organize the information into specific categories. The final output should be structured as CSV data, following the format outlined below.

Resume Text:
{resume_text}

CSV Output Format:

1. Personal Information:
   - Title: "Name,Surname"

2. Soft Skills:
   - Format: "Soft skills"

3. Technical Skills:
   - Architectures: "Operating Systems"
   - Framework/API/Webservices/CMS: "Frameworks, APIs, Webservices, CMS"
   - Storage/Database/BI: "Storage, Database, BI tools"
   - DevOps/Cloud/AI: "DevOps, Cloud, AI tools"
   - Tools/Software/ERP: "Tools, Software, ERP"

4. Languages:
   - Format: "Language, Level (Beginner, Intermediate, Advanced)"

5. Education:
   - Format: "Year, Degree, University/School"

6. Certifications:
   - Format: "Date, Certification Name"

7. Professional Experience:
   - Format: "Date, Title, Client, Project, Tasks, Tools/Methodology"

For any missing information, please enter 'N/A' in the relevant fields.

Example CSV Output:

```
Name,Surname
John,Doe

Soft skills
Communication, Leadership

Operating Systems
Linux, Windows

Frameworks, APIs, Webservices, CMS
React, Node.js, RESTful API

Storage, Database, BI tools
MySQL, MongoDB

DevOps, Cloud, AI tools
Docker, AWS

Tools, Software, ERP
Jira, SAP

Languages
English, Advanced

Year, Degree, University/School
2020, Bachelor of Computer Science, XYZ University

Date, Certification Name
2021, AWS Certified Solutions Architect

Date, Title, Client, Project, Tasks, Tools/Methodology
2022, Senior Developer, ABC Corp, E-commerce Platform, Developed features, Agile methodology
```

Please extract the information and structure it exactly as described above.
"""
prompt_3 = """
Given the following unorganized text extracted from a resume, 
please structure the information into a CSV file with the following columns:
Resume Text:
{resume_text}
CSV Columns:
Name,Surname,Soft Skills,Other Skills,Languages,Architectures,Frameworks/APIs/Webservices/CMS,Storage/Database/BI,Devops/Cloud/AI,Tools/Software/ERP,Formations (Year/Degree/University),Certifications (Date/Certification),Professional Experience (Date/Title/Client/Project/Tasks/Tools)
If any information is not available, please write 'N/A' in the corresponding cell.
Please provide the output as a CSV string.
"""
prompt_4 = """

Please analyze the following unorganized text extracted from a resume and organize the information into specific categories. The final output should be structured as CSV data, following the format outlined below.

Resume Text:
{resume_text}

CSV Output Format:

"Name,Surname", "Soft skills","Operating Systems","Frameworks", "APIs", "Webservices", "CMS","Storage", "Database", "BI tools","DevOps", "Cloud", "AI tools","Tools", "Software", "ERP","Language", "Level (Beginner, Intermediate, Advanced)","Year", "Degree", "University/School","Certification Date", "Certification Name", "Profissional Title","Date", "Client", "Project", "Tasks", "Tools/Methodology"

For any missing information, please enter 'N/A' in the relevant fields.

Example CSV Output:

```
"Name,Surname", "Soft skills","Operating Systems","Frameworks", "APIs", "Webservices", "CMS","Storage", "Database", "BI tools","DevOps", "Cloud", "AI tools","Tools", "Software", "ERP","Language", "Level (Beginner, Intermediate, Advanced)","Year", "Degree", "University/School","Certification Date", "Certification Name", "Profissional Title","Date", "Client", "Project", "Tasks", "Tools/Methodology"    
John,Doe,Communication, Linux,React,MySQL,Docker,Jira,English,Advanced, 2020, Bachelor of Computer Science, XYZ University, 2021, AWS Certified Solutions Architect, 2022, Senior Developer, ABC Corp, E-commerce Platform, Developed features, Agile methodology
,Leadership,Windows,Node.js,MongoDB,AWS,SAP,Frensh,Beginner
,,,RESTful API
                
```

Please extract the information and structure it exactly as described above.
"""
prompts = [prompt_1, prompt_2, prompt_3, prompt_4]
