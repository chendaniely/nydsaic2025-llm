from typing import List

import chatlas as ctl
import pandas as pd
from pydantic import BaseModel, Field

pdf = ctl.content_pdf_file(
    "/Volumes/expansionSD/SynologyDrive/work/ubc/sei-student_surveys/sei_pdfs/2024-25 Winter Term 2 Student Experience of Instruction Report for DSCI_V 310-101 - Reproducible and Trustworthy Workflows _aff009f5-921c-4b02-997e-436ced84885een-US.pdf"
)


# Row-oriented data structure
class LikertScaleRow(BaseModel):
    """Single row of likert scale results - this represents one survey question"""

    question_type: str = Field(
        description="General heading the questions are under"
    )
    question: str = Field(description="Question that was asked in the survey")
    N: int = Field(description="Number of responses invited")
    n: int = Field(description="Number of responses")
    sd: int = Field(description="Number of strongly disagree")
    d: int = Field(description="Number of disagree")
    neutral: int = Field(description="Number of neutral")
    a: int = Field(description="Number of agree")
    sa: int = Field(description="Number of strongly agree")
    na: int = Field(description="Number of not applicable")
    im: float = Field(description="interpolated median value")
    pf: str = Field(description="percent favorable rating")
    di: float = Field(description="dispersion index")


class LikertScaleResults(BaseModel):
    """Collection of Likert scale results that can be converted to DataFrame"""

    results: List[LikertScaleRow] = Field(
        description="List of survey question results"
    )


chat = ctl.ChatOpenAI(
    system_prompt="""
    You will be given a PDF of student feedback results from a course.
    There are mutliple questions the students are asked and the likert data is summarized across multiple tables.
    Extract all the data in the tables into separate pandas dataframe objects.
    """
)

dat = chat.extract_data(
    pdf,
    data_model=LikertScaleResults,
)

results = pd.DataFrame(dat["results"])
results
