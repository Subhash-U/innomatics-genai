import os
import json
from dotenv import load_dotenv
from chains.screener import build_screening_chain
from data.samples import JOB_DESCRIPTION, RESUME_STRONG, RESUME_AVERAGE, RESUME_WEAK

# Load environment variables (Enables LangSmith)
load_dotenv()

def evaluate_candidate(name, resume_text, job_desc, chain):
    print(f"\nEvaluating Candidate: {name}...")
    
    # Invoke the chain
    result = chain.invoke({
        "job_description": job_desc,
        "resume": resume_text
    })
    
    # Print formatted output
    print(json.dumps(result, indent=2))
    return result

if __name__ == "__main__":
    print("Initializing Resume Screening Pipeline...")
    screener_chain = build_screening_chain()
    
    # Run the 3 test cases
    evaluate_candidate("Strong Candidate (Alice)", RESUME_STRONG, JOB_DESCRIPTION, screener_chain)
    evaluate_candidate("Average Candidate (Bob)", RESUME_AVERAGE, JOB_DESCRIPTION, screener_chain)
    evaluate_candidate("Weak Candidate (Charlie)", RESUME_WEAK, JOB_DESCRIPTION, screener_chain)
    
    print("\n✅ Evaluation complete! Check your LangSmith dashboard for the execution traces.")