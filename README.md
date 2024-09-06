# InfoCV

InfoCV is a resume processing tool that extracts and processes information from PDF and DOCX files using Large Language Models. The tool leverages Ollama to process resumes and extract structured information.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/InfoCV.git
    cd InfoCV
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up environment:
   - If you want to use the local API (**Recommended**):
        - just install the `Ollama` tool from [Ollama Website](https://ollama.com/)
        and run the following command:
        ```sh
        ollama serve
        ```
        - the local API will be running on `http://localhost:11434`: you will fing a message like this:
        ```plaintext
        Ollama is running
        ```

## Usage

1. Run the Streamlit interface:
    ```sh
    streamlit run app.py
    ```
2. Upload a resume file (PDF or DOCX) and select a model to process the resume.
3. choose the model you want to use to process the resume.
4. choose either using `resume analysis` or `job fit` to process the resume.
5. press the `Process` and let the magic happen!

## Project Structure

```plaintext
InfoCV/
├── app.py
├── data/
│   ├── data_raw/
│   └── preprocessed_data/
├── evaluations/
│   └── evaluate.py
├── InfoCV.egg-info/
├── Interface/
│   └── Interface.py
├── models/
│   └── API.py
├── notebooks/
│   └── raport.ipynb
├── reports/
├── requirements.txt
├── setup.py
├── test.py
├── tests/
│   ├── conftest.py
│   ├── test_imports.py
│   ├── test_models.py
│   └── test_utils.py
├── TODO
└── utils/
    └── extraction.py
```

- [`app.py`]: Main application script.
- [`data/`]: Directory for storing raw and preprocessed data.
- [`evaluations/`]: Scripts for evaluating the models.
- [`Interface/`]: Streamlit interface for user interaction.
- [`models/`]: Contains the API for processing resumes.
- [`notebooks/`]: Jupyter notebooks for experiments and reports.
- [`reports/`]: Directory for storing reports.
- [`tests/`]: Unit tests for the project.
- [`utils/`]: Utility scripts for data extraction and logging.

## Contributing

Contributions are welcome! Please check [Issues Page](https://github.com/bssayla/InfoCv/issues) for a list of tasks and improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
Free software: [MIT license](LICENSE)

### Reporting Issues

When reporting issues, please use our issue templates. We have templates for different types of issues to ensure we get all the necessary information:

1. **Bug Reports**: Use this template when you encounter a problem with the existing functionality.
2. **Feature Requests**: Use this when you want to suggest a new feature or enhancement.
3. **Documentation Improvements**: Use this to suggest changes or additions to our documentation.

To use a template:
1. Go to the "Issues" tab in our GitHub repository
2. Click on "New Issue"
3. Choose the appropriate template from the list
4. Fill out the template with as much detail as possible

Using these templates helps us address issues more effectively and efficiently. Thank you for your contributions!