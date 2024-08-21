# InfoCV

InfoCV is a resume processing tool that extracts and processes information from PDF and DOCX files using Large Language Models. The tool leverages the Hugging Face Transformers library to process resumes and extract structured information.

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
    - If you want to use the Hugging Face API, you need to set up your Hugging Face token.
        - Create a `.env` file in the root directory and add your Hugging Face token:
        ```env
        HF_TOKEN=your_hugging_face_token
        ```
    - If you want to use the local API, you can skip this step.
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
4. choose either using `HugginFace API` or `Local API: Ollama` to process the resume.
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

Contributions are welcome! Please read the [`TODO`] file for a list of tasks and improvements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
Free software: [MIT license](LICENSE)
