import csv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def get_model_response(prompt, model, tokenizer, max_length=1024):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, temperature=0.7)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def process_resume(resume_text, model, tokenizer):
    prompt = f"""
    Given the following unorganized text extracted from a resume, please structure the information into the following categories:

    Resume Text:
    {resume_text}

    Please provide the information in the following format:
    Summary:
    Title:
    Number of years of experience:
    Know-how:
    Soft skills:

    Skills:
    Languages:
    Methods / architectures:
    Framework / API / Webservices / CMS:
    Storage / Database / BI:
    Devops / Cloud / AI:
    Tools / Software / ERP:

    Formations:
    Year / Degree / University or school:

    Languages:
    French:
    English:

    Certifications:
    Date / name of certification:

    Professional experience:
    Title:
    Position / function:
    Client:
    Project:
    Tasks:
    Tools / Methodology:

    If any information is not available, please write 'N/A'.
    """

    response = get_model_response(prompt, model, tokenizer)
    return response

def main():
    # Load the model and tokenizer
    model_name = "meta-llama/Llama-2-7b-chat-hf"  # You can change this to other models like "google/gemma-7b"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Get input file path
    input_file = input("Enter the path to the text file containing the resume: ")

    # Read the resume text
    with open(input_file, 'r') as file:
        resume_text = file.read()

    # Process the resume
    structured_resume = process_resume(resume_text, model, tokenizer)

    # Write the output to a CSV file
    output_file = "structured_resume.csv"
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows([line.split(':') for line in structured_resume.split('\n') if line.strip()])

    print(f"Structured resume has been saved to {output_file}")
