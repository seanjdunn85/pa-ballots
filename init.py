import pandas as pd
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

db = mysql.connector.connect(host=os.getenv("SQL_HOST"), user=os.getenv("SQL_USER"), password=os.getenv("SQL_PASSWORD"))

cursor = db.cursor()
cursor.execute("USE pa_general")

chunksize = 1000
number_processed = 0

def process(chunk2, number_processed):
    statement = """INSERT INTO
    `mail_in_ballots` (
    `County Name`,
    `Applicant Party Designation`,
    `Date Of Birth`,
    `Mail Application Type`,
    `Application Request Date`,
    `Application Approved Date`,
    `Ballot Mailed Date`,
    `Ballot Returned Date`,
    `State House District`,
    `State Senate District`,
    `Congressional District`
    ) 
    VALUES(
    %s,
    %s,
    STR_TO_DATE(%s,'%m/%d/%Y'),
    %s,
    STR_TO_DATE(%s,'%m/%d/%Y'),
    STR_TO_DATE(%s,'%m/%d/%Y'),
    STR_TO_DATE(%s,'%m/%d/%Y'),
    STR_TO_DATE(%s,'%m/%d/%Y'),
    %s,
    %s,
    %s
    )"""

    ## mysql execute() function can't play nice with nan values. Must replace with none.
    # chunk2 = chunk2.replace(np.nan, None)
    chunk = chunk2.where(pd.notnull(chunk2), None)
    for index, row in chunk.iterrows():
        print row.values

        if(number_processed == 0):
            number_processed += 1
            continue

        data = (
            # chunk.loc[int].values[0],
            row.values[0],
            # chunk.loc[int].values[1],
            row.values[1],
            # chunk.loc[int].values[2],
            row.values[2],
            # chunk.loc[int].values[3],
            row.values[3],
            # chunk.loc[int].values[4],
            row.values[4],
            # chunk.loc[int].values[5],
            row.values[5],
            # chunk.loc[int].values[6],
            row.values[6],
            # chunk.loc[int].values[7],
            row.values[7],
            # chunk.loc[int].values[8],
            row.values[8],
            # chunk.loc[int].values[9],
            row.values[9],
            # chunk.loc[int].values[10],
            row.values[10],
        )
        cursor.execute(statement, data)
        number_processed += 1
    db.commit()

for chunk in pd.read_csv("/Users/seandunn/Downloads/2020_Primary_Election_Mail_Ballot_Requests_Department_of_State.csv", chunksize=chunksize):
    process(chunk, number_processed)