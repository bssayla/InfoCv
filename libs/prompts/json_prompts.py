extract_data_from_resume_as_json_1 = """

    **Task:** Extract relevant information from the following resume text and return it in JSON format **without any additional text or explanations**.

    **Resume Text:**

    {resume_text}

    **Desired JSON Structure:**

    ```json
    {{
      "Full Name": "John Doe",
      "Email Address": "john.doe@example.com",
      "Phone Number": "+1-555-123-4567",
      "LinkedIn Profile URL": "linkedin.com/in/johndoe",
      "Skills": ["Python", "Java", "Communication"],
      "Work Experience": [
        {{
          "Company": "ABC Company",
          "Title": "Project Manager",
          "Dates": "2020-Present"
        }}
      ],
      "Education": [
        {{
          "Institution": "Harvard University",
          "Degree": "Master of Science in Computer Science",
          "Dates": "2018-2020"
        }}
      ]
    }}
    ```

    **Instructions:**

    1. **Identify the requested information within the resume text.**
    2. **Organize the extracted information into a JSON structure** following the example above.
        * Use the specified keys for each field.
        * Represent lists of items (like skills, work experience, education) as JSON arrays. 
    3. **Return only the raw JSON content** without any introductory text, explanations, or commentary.


    **Note:**

    * The resume text may be in various formats (plain text, formatted text, etc.).
    * You may need to infer some information based on the context of the resume.
    * Ensure the JSON output is properly formatted with correct key-value pairs, arrays, and data types.
    * Do not include any extra characters or information beyond the requested JSON data. 


"""
