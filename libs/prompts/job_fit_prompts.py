job_fitting_prompt_1= """

      {job_description}
      Given a job description and text extracted from a resume, please analyze the candidate's profile in detail to determine if they are a good fit for the job. Follow these steps:      Job Description:
      Resume Text:
      {resume_text}

      Analysis Steps:
      1. Extract key requirements from the job description, including required skills, experience, and qualifications.

      2. Identify the candidate's skills, experience, and qualifications from the resume text.

      3. Compare the job requirements with the candidate's profile, noting matches and gaps.

      4. Evaluate the candidate's relevant experience and its alignment with the job requirements.

      5. Assess any additional qualifications or skills the candidate possesses that could be beneficial for the role.

      6. Consider any potential red flags or mismatches between the job requirements and the candidate's profile.

      7. Provide a summary of the candidate's strengths and weaknesses in relation to the job.


      8. Give a final recommendation on whether the profile is a good fit for the job, with a brief explanation.

      Please provide your analysis and recommendation in a clear, step-by-step format. Be objective and thorough in your assessment.
   """
