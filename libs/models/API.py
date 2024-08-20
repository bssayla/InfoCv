import logging
import torch


def get_model_response(prompt, model, tokenizer, max_length=1024):
    logger = logging.getLogger(__name__)
    logger.info("Getting model response")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    inputs = tokenizer.encode(prompt, return_tensors="pt").to(device)
    outputs = model.generate(inputs, max_length=max_length, temperature=0.7,do_sample=True)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    logger.info("Model response received")
    return response


def process_resume(resume_text, model, tokenizer):
    logger = logging.getLogger(__name__)
    logger.info("Starting resume processing")

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
    logger.info("Resume processing completed")
    return response
