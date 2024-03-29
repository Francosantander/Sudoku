FROM python:3

RUN git clone https://github.com/Francosantander/Sudoku
WORKDIR /Sudoku

RUN pip install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_sudoku.py"]