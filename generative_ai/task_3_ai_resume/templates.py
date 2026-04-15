from langchain_core.prompts import PromptTemplate

SCREENING_PROMPT = """
You are an expert AI Technical Recruiter. Your task is to evaluate a candidate's resume against a Job Description. 
Do NOT assume or hallucinate any skills not explicitly mentioned in the resume.

Job Description:
{job_description}

Candidate Resume:
{resume}

Follow these steps:
1. Extract: List the core skills, years of experience, and tools from the resume.
2. Match: Compare the extracted data against the job description requirements. Note what is missing.
3. Score: Assign a Fit Score from 0 to 100 based on the match.
4. Explain: Provide a brief reasoning for the score.

Provide your response in strictly valid JSON format with the following keys:
- "extracted_data": {{"skills": [], "experience_years": 0, "tools": []}}
- "missing_requirements": []
- "fit_score": 0
- "explanation": ""
"""

screening_prompt_template = PromptTemplate(
    input_variables=["job_description", "resume"],
    template=SCREENING_PROMPT
)