# Student Activity: Anomaly Detection Project
- Purpose: Analyze curriculum logs for anomalies.
- Goals: Provide analysis on curriculum log use and the following questions:
    - Lessons with the most activity?
    - Cohort lesson activity?
    - Access by active users, any significance?
    - Topics accessed by Alumni?
    - Least active lessons?
    
# Project Details
- Libraries
- Project Modules

# Pipeline
My methodology follow is the data pipeline; plan, acquire, prepare, explore, model and deliver.

# Plan
1. Acquire and prepare curriculum logs.
2. Analysis based on Anomaly Detection and ran through the data pipeline.
3. A copy of the cleaned dataset is available below.
4. Planning was done via <a href="https://www.w3schools.com">Trello</a>.

# Acquire
- Function accessesing db server, queries logs, and cohorts tables from the curriculm_logs db.
- curriculum_logs db. Queried all tables with a LEFT JOIN.

# Prepare
- Shape: (638186, 11)
- Droppede Nulls, duplicated/uneeded columns, jpg, svg, leading digits and charactersn to clean up lessons and dataframe
- Split path into lessons
- Convert dtypes
- Datetime conversion and indexing
- Created and merged programs

# Explore
- pandas plots
- matplotlib
- Tableau
- Bollingers Band
- Created dataframes for Discrete Anomaly Detection. 

# Takeaways
- One main takeawy in activity across the board showed some users were assigned as to a 'Cohort' then 'Staff' suggesting the student became an employee; possibly or bad data was entered.
- Time of year had an impact on activity.
- Increase in activity over the years - growth in activity, classes per year, added programs.

# Data Dictionary
| **Value**        | **Descritption**                | **Dtype**      |
|------------------|---------------------------------|----------------|
| user_id          | student or staff identification | int64          |
| cohort_id        | class cohort identification     | int64          |
| ip               | ip address                      | object         |
| cohort           | class cohort name               | object         |
| class_start_date | start of given class            | datetime64[ns] |
| class_end_date   | end op given class              | datetime64[ns] |
| created_at       | profile created date            | datetime64[ns] |
| updated_at       | last date profile use updated   | datetime64[ns] |
| program_id       | program identification          | int64          |
| subdomain        | program name                    | object         |
| path_2           | lesson                          | object         |
