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

      Here's a the scoring system you should use to evaluate the candidate's profile: 

      1. Skills Match:
      Rate how well the candidate's technical skills align with those required in the job description. (0-10 points)
      2. Experience Level:
      Evaluate if the candidate's years of experience meet or exceed the job requirements. (0-10 points)
      3. Industry Relevance:
      Assess how closely the candidate's industry experience matches the job's industry. (0-10 points)
      4. Education:
      Compare the candidate's educational background to the job's educational requirements. (0-10 points) 
      5. Key Achievements:
      Rate the relevance and impressiveness of the candidate's past achievements in relation to the job. (0-10 points)
      6. Job Title Alignment:
      Evaluate how closely the candidate's previous job titles match the position they're applying for. (0-10 points)
      7. Soft Skills:
      Assess the presence and relevance of soft skills mentioned in the resume compared to those in the job description. (0-10 points)
      8. Certifications:
      Rate the relevance and value of any certifications the candidate has in relation to the job requirements. (0-10 points)
      9. Project Experience:
      Evaluate how well the candidate's project experience aligns with the types of projects mentioned in the job description. (0-10 points)
      10. Cultural Fit:
      Based on the resume and job description, rate how well the candidate's values and work style might fit the company culture. (0-10 points)

      Give a the total score of the candidate's profile based on the scoring system above and Please provide your analysis and recommendation in a clear, step-by-step format. Be objective and thorough in your assessment.
   """
